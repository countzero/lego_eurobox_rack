// Asks the render loop for a new frame; the loop takes the request once.
let wanted = true;

export function redraw() {
  wanted = true;
}

export function take() {
  const was = wanted;
  wanted = false;
  return was;
}
