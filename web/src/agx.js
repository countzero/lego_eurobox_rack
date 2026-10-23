// Blender's view transform, AgX with the look "AgX - Punchy" (build_rack.py
//  render settings), in place of three.js's AgX: that is Troy Sobotka's
// earlier AgX without looks and renders the boxes washed out beside Blender.
// The image formation is ported from the scripts that generate Blender's AgX
// LUTs (github.com/EaryChow/AgX_LUT_Gen); the look from Blender's config.ocio,
// where Punchy is OpenColorIO's GradingTone shadows and a CDL power in
// "AgX Log". Blender applies the formation and the Rec.2020 guard rail as 3D
// LUTs, and their tetrahedral interpolation shifts saturated colours by up to
// 16/255 against the exact curves; so the shader evaluates the curves at the
// LUTs' grid points and interpolates as OpenColorIO does. That keeps it within
// 1/255 of Blender's output (sRGB display) without shipping the LUT files.
import { CustomToneMapping, ShaderChunk } from "three";

const HOOK = "vec3 CustomToneMapping( vec3 color ) { return color; }";

const GLSL = /* glsl */`
const mat3 AGX_REC709_TO_REC2020 = mat3(
  0.6274038959, 0.0690972894, 0.0163914389,
  0.3292830384, 0.9195403951, 0.0880133079,
  0.0433130657, 0.0113623156, 0.8955952532 );
const mat3 AGX_REC2020_TO_EGAMUT = mat3(
  0.8883977553, 0.0259563870, 0.0743368988,
  0.0029163564, 0.8342565186, 0.0704715777,
  0.1086634334, 0.1397792728, 0.8550648945 );
const mat3 AGX_EGAMUT_TO_REC2020 = mat3(
  1.1375888732, -0.0190871649, -0.0973256263,
  0.0083505022, 1.2153160486, -0.1008882371,
  -0.1459322452, -0.1962446567, 1.1983626363 );
const mat3 AGX_INSET = mat3(
  0.8566271533, 0.1373189729, 0.1118982130,
  0.0951212405, 0.7612419906, 0.0767994186,
  0.0482516061, 0.1014390365, 0.8113023684 );
const mat3 AGX_INSET_INV = mat3(
  1.1974410769, -0.1964746263, -0.1465574171,
  -0.1442615127, 1.3540951315, -0.1082840588,
  -0.0531795642, -0.1576205051, 1.2548414759 );
// The outset (Rec.2020 primaries pulled toward white) and the way back to Rec.709.
const mat3 AGX_OUTSET_TO_REC709 = mat3(
  1.9648873855, -0.2993133532, -0.1643527331,
  -0.8559884787, 1.3263979451, -0.2381839628,
  -0.1088989068, -0.0270845919, 1.4025366958 );
// Rec.2020 luminance from CIE 2015 colour matching functions, as the guard rails use.
const vec3 AGX_LUMA = vec3( 0.2589235356, 0.6104985346, 0.1305779298 );
// Log2 range -10 to +6.5 stops about 0.18; sigmoid slope 2.4, powers 1.5.
const float AGX_PIVOT_X = 0.6060606061;
const float AGX_PIVOT_Y = 0.4894370896;
const float AGX_TOE_SCALE = -0.5656756067;
const float AGX_SHOULDER_SCALE = 0.7151982863;
// "AgX Log", where the looks run: log2 from -12.47393 over 25 stops.
const float AGX_LOG_MIN = -12.47393;
const float AGX_LOG_RANGE = 25.0;

float agxSigmoid( float x ) {
  float s = x < AGX_PIVOT_X ? AGX_TOE_SCALE : AGX_SHOULDER_SCALE;
  float t = 2.4 * ( x - AGX_PIVOT_X ) / s;
  return s * t / pow( 1.0 + pow( t, 1.5 ), 1.0 / 1.5 ) + AGX_PIVOT_Y;
}

vec3 agxHsv( vec3 c ) {
  float mx = max( c.r, max( c.g, c.b ) );
  float d = mx - min( c.r, min( c.g, c.b ) );
  float h = 0.0;
  if ( d > 0.0 ) {
    if ( mx == c.r ) h = ( c.g - c.b ) / d;
    else if ( mx == c.g ) h = 2.0 + ( c.b - c.r ) / d;
    else h = 4.0 + ( c.r - c.g ) / d;
    h = fract( h / 6.0 );
  }
  return vec3( h, mx > 0.0 ? d / mx : 0.0, mx );
}

vec3 agxRgb( vec3 hsv ) {
  vec3 k = mod( vec3( 5.0, 3.0, 1.0 ) + hsv.x * 6.0, 6.0 );
  return hsv.z - hsv.z * hsv.y * clamp( min( k, 4.0 - k ), 0.0, 1.0 );
}

// Rec.2020 lower guard rail: lifts negative channels, keeping the luminance.
vec3 agxGuard( vec3 c ) {
  float lo = min( c.r, min( c.g, c.b ) );
  if ( lo >= 0.0 ) return c;
  float y = dot( c, AGX_LUMA );
  return ( c - lo ) * ( 2.0 * y - lo ) / max( 2.0 * y - 2.0 * lo, 1e-10 );
}

// The luminance of the guard rail for Rec.709, which also counts the
// opponent colour so that a negative luminance still gets lifted.
float agxGuardY( vec3 c ) {
  vec3 inv = max( c.r, max( c.g, c.b ) ) - c;
  float y = dot( AGX_REC709_TO_REC2020 * c, AGX_LUMA );
  float yc = max( inv.r, max( inv.g, inv.b ) ) - dot( AGX_REC709_TO_REC2020 * inv, AGX_LUMA ) + y;
  return mix( yc, y, clamp( pow( max( y, 0.0 ), 0.08 ), 0.0, 1.0 ) );
}

// Rec.709 lower guard rail of the sRGB formation, after the outset: the
// formed colour can leave Rec.709 even when the scene colour is inside it.
vec3 agxGuard709( vec3 c ) {
  float y = agxGuardY( c );
  vec3 o = c + max( -min( c.r, min( c.g, c.b ) ), 0.0 );
  float yn = agxGuardY( o );
  return yn > y ? o * ( y / max( yn, 1e-30 ) ) : o;
}

// Log2 from -10 to +15 stops about 0.18 in E-Gamut: the domain of both LUTs.
vec3 agxLutIn( vec3 c2020 ) {
  return clamp( ( log2( max( AGX_REC2020_TO_EGAMUT * c2020, 1e-10 ) / 0.18 ) + 10.0 ) / 25.0, 0.0, 1.0 );
}

vec3 agxLutOut( vec3 p ) {
  return AGX_EGAMUT_TO_REC2020 * ( 0.18 * exp2( p * 25.0 - 10.0 ) );
}

// One grid point of a LUT: 0 the Rec.2020 guard rail (37 points), 1 the sRGB
// formation (57 points), whose output is Rec.709 encoded with power 2.4.
vec3 agxNode( int lut, vec3 n ) {
  if ( lut == 0 ) return agxLutIn( agxGuard( agxLutOut( n / 36.0 ) ) );
  vec3 c = AGX_INSET * agxGuard( agxLutOut( n / 56.0 ) );
  float h0 = agxHsv( c ).x;
  vec3 x = ( log2( max( c, 1e-10 ) / 0.18 ) + 10.0 ) / 16.5;
  c = pow( max( vec3( agxSigmoid( x.r ), agxSigmoid( x.g ), agxSigmoid( x.b ) ), 0.0 ), vec3( 2.4 ) );
  // 40 % of the per-channel hue shift kept, the shorter way round.
  vec3 hsv = agxHsv( c );
  float dh = hsv.x - h0;
  hsv.x -= dh > 0.5 ? 1.0 : dh < -0.5 ? -1.0 : 0.0;
  hsv.x = fract( h0 + 0.4 * ( hsv.x - h0 ) );
  c = agxGuard709( AGX_OUTSET_TO_REC709 * agxRgb( hsv ) );
  return pow( clamp( c, 0.0, 1.0 ), vec3( 1.0 / 2.4 ) );
}

vec3 agxTetra( int lut, vec3 p, float size ) {
  vec3 f = p * ( size - 1.0 );
  vec3 i = min( floor( f ), size - 2.0 );
  vec3 d = f - i;
  vec3 a, b;
  vec3 w;
  if ( d.r > d.g ) {
    if ( d.g > d.b ) { a = vec3( 1, 0, 0 ); b = vec3( 1, 1, 0 ); w = d.rgb; }
    else if ( d.r > d.b ) { a = vec3( 1, 0, 0 ); b = vec3( 1, 0, 1 ); w = d.rbg; }
    else { a = vec3( 0, 0, 1 ); b = vec3( 1, 0, 1 ); w = d.brg; }
  } else {
    if ( d.b > d.g ) { a = vec3( 0, 0, 1 ); b = vec3( 0, 1, 1 ); w = d.bgr; }
    else if ( d.b > d.r ) { a = vec3( 0, 1, 0 ); b = vec3( 0, 1, 1 ); w = d.gbr; }
    else { a = vec3( 0, 1, 0 ); b = vec3( 1, 1, 0 ); w = d.grb; }
  }
  vec3 c0 = agxNode( lut, i ), ca = agxNode( lut, i + a );
  vec3 cb = agxNode( lut, i + b ), c1 = agxNode( lut, i + 1.0 );
  return c0 + w.x * ( ca - c0 ) + w.y * ( cb - ca ) + w.z * ( c1 - cb );
}

// OCIO's GradingTone shadows, forward, for a value below 1: a quadratic from
// the pivot 0.1 (slope m) to the start 0.4 (slope 1), linear below the pivot.
vec3 agxShadows( vec3 t, float m ) {
  const float x0 = 0.1, x1 = 0.25, x2 = 0.4;
  float y1 = ( 0.5 / ( x2 - x0 ) ) * ( ( 2.0 * x0 + m * ( x1 - x0 ) ) * ( x2 - x1 )
    + ( 2.0 * x2 - ( x2 - x1 ) ) * ( x1 - x0 ) );
  vec3 tL = ( t - x0 ) / ( x1 - x0 );
  vec3 tR = ( t - x1 ) / ( x2 - x1 );
  vec3 fL = x0 * ( 1.0 - tL * tL ) + y1 * tL * tL + m * ( 1.0 - tL ) * tL * ( x1 - x0 );
  vec3 fR = y1 * ( 1.0 - tR ) * ( 1.0 - tR ) + x2 * ( 2.0 - tR ) * tR + ( tR - 1.0 ) * tR * ( x2 - x1 );
  vec3 r = mix( fL, fR, step( x1, t ) );
  r = mix( ( t - x0 ) * m + x0, r, step( x0, t ) );
  return mix( r, t, step( x2, t ) );
}

vec3 CustomToneMapping( vec3 color ) {
  color *= toneMappingExposure;
  vec3 c = agxLutIn( AGX_REC709_TO_REC2020 * color );
  c = AGX_INSET * agxLutOut( agxTetra( 0, c, 37.0 ) );
  // The look: shadows 0.2 per channel, then 0.35 on all, then power 1.0912
  // (a CDL without clamp leaves negative values alone).
  vec3 x = ( log2( max( c, 1e-10 ) ) - AGX_LOG_MIN ) / AGX_LOG_RANGE;
  x = agxShadows( agxShadows( x, 0.2 ), 0.35 );
  x = mix( x, pow( max( x, 0.0 ), vec3( 1.0912 ) ), step( 0.0, x ) );
  c = AGX_INSET_INV * exp2( x * AGX_LOG_RANGE + AGX_LOG_MIN );
  // Rec.1886 out of the LUT, back to linear for the sRGB encoding of OutputPass.
  return pow( clamp( agxTetra( 1, agxLutIn( c ), 57.0 ), 0.0, 1.0 ), vec3( 2.4 ) );
}
`;

if (!ShaderChunk.tonemapping_pars_fragment.includes(HOOK)) {
  throw new Error("agx.js: three.js's CustomToneMapping hook not found");
}
// Patched at import, before any shader compiles: the materials and the
// composers' OutputPass all take their tone mapping from this chunk.
ShaderChunk.tonemapping_pars_fragment = ShaderChunk.tonemapping_pars_fragment.replace(HOOK, GLSL);

export const BlenderAgXToneMapping = CustomToneMapping;
