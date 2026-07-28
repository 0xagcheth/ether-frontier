const ATLAS_SIZE = 2048;
const CELL_SIZE = 256;
const FRAME_COUNT = 8;

const animations = [
  { id: "walk_up", label: "Ходьба вверх", row: 0, duration: 100, loop: true },
  { id: "walk_down", label: "Ходьба вниз", row: 1, duration: 100, loop: true },
  { id: "walk_left", label: "Ходьба влево", row: 2, duration: 100, loop: true },
  { id: "walk_right", label: "Ходьба вправо", row: 3, duration: 100, loop: true },
  { id: "spawn", label: "Появление", row: 4, duration: 120, loop: false },
  { id: "breach", label: "Прорыв в замок", row: 5, duration: 120, loop: false },
  { id: "death", label: "Смерть", row: 6, duration: 120, loop: false },
];

const sprite = document.querySelector("#sprite");
const stage = document.querySelector("#stage");
const stageLabel = document.querySelector("#stageLabel");
const activeName = document.querySelector("#activeName");
const animationList = document.querySelector("#animationList");
const frameStrip = document.querySelector("#frameStrip");
const frameNumber = document.querySelector("#frameNumber");
const playPause = document.querySelector("#playPause");
const speed = document.querySelector("#speed");
const speedValue = document.querySelector("#speedValue");

let active = animations[0];
let frame = 0;
let playing = true;
let lastFrameAt = performance.now();

function positionFor(column, row) {
  return `${-column * CELL_SIZE}px ${-row * CELL_SIZE}px`;
}

function renderFrame() {
  sprite.style.backgroundPosition = positionFor(frame, active.row);
  frameNumber.textContent = String(frame + 1);
  document.querySelectorAll(".frame-cell").forEach((cell, index) => {
    cell.classList.toggle("active", index === frame);
  });
}

function renderStrip() {
  frameStrip.replaceChildren();
  for (let index = 0; index < FRAME_COUNT; index += 1) {
    const cell = document.createElement("button");
    cell.className = "frame-cell";
    cell.type = "button";
    cell.setAttribute("aria-label", `Кадр ${index + 1}`);
    cell.style.setProperty("--column", index);
    cell.style.setProperty("--row", active.row);
    cell.innerHTML = `<span>${String(index + 1).padStart(2, "0")}</span>`;
    cell.style.background = "#192321";
    const preview = document.createElement("i");
    preview.style.cssText = `position:absolute;inset:0;background-image:var(--atlas);background-size:800% 700%;background-position:${index / 7 * 100}% ${active.row / 6 * 100}%;background-repeat:no-repeat;`;
    cell.prepend(preview);
    cell.addEventListener("click", () => {
      frame = index;
      playing = false;
      playPause.textContent = "Старт";
      renderFrame();
    });
    frameStrip.append(cell);
  }
  renderFrame();
}

function selectAnimation(next) {
  active = next;
  frame = 0;
  playing = true;
  speed.value = String(next.duration);
  speedValue.textContent = `${next.duration} мс`;
  playPause.textContent = "Пауза";
  stageLabel.textContent = next.label;
  activeName.textContent = next.label;
  stage.dataset.animation = next.id;
  document.querySelectorAll(".animation-button").forEach((button) => {
    button.classList.toggle("active", button.dataset.animation === next.id);
  });
  renderStrip();
}

animations.forEach((animation) => {
  const button = document.createElement("button");
  button.type = "button";
  button.className = "animation-button";
  button.dataset.animation = animation.id;
  button.innerHTML = `<span>${animation.label}</span><small>8 FR</small>`;
  button.addEventListener("click", () => selectAnimation(animation));
  animationList.append(button);
});

playPause.addEventListener("click", () => {
  if (!playing && !active.loop && frame === FRAME_COUNT - 1) frame = 0;
  playing = !playing;
  playPause.textContent = playing ? "Пауза" : "Старт";
  lastFrameAt = performance.now();
  renderFrame();
});

document.querySelector("#prevFrame").addEventListener("click", () => {
  playing = false;
  playPause.textContent = "Старт";
  frame = (frame - 1 + FRAME_COUNT) % FRAME_COUNT;
  renderFrame();
});

document.querySelector("#nextFrame").addEventListener("click", () => {
  playing = false;
  playPause.textContent = "Старт";
  frame = (frame + 1) % FRAME_COUNT;
  renderFrame();
});

speed.addEventListener("input", () => {
  speedValue.textContent = `${speed.value} мс`;
});

function tick(now) {
  if (playing && now - lastFrameAt >= Number(speed.value)) {
    if (frame === FRAME_COUNT - 1 && !active.loop) {
      playing = false;
      playPause.textContent = "Повтор";
    } else {
      frame = (frame + 1) % FRAME_COUNT;
      renderFrame();
    }
    lastFrameAt = now;
  }
  requestAnimationFrame(tick);
}

selectAnimation(active);
requestAnimationFrame(tick);
