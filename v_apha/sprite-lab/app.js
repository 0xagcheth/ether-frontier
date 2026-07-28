const ASSET_ROOT = "../assets/sprite-atlases/goblin-spearman/animations/runtime-384";
const SOURCE_FRAME = 384;
const BUILDING_ASSET_VERSION = "27";

const atlas = {
  idle: { file: "idle-directions-384-alpha.png", frames: 1, rows: 1, duration: 700, loop: true },
  walk: { file: "walk-384-alpha.png", frames: 8, rows: 4, duration: 90, loop: true },
  attack: { file: "attack-384-alpha.png", frames: 8, rows: 4, duration: 80, loop: false },
  spawn: { file: "spawn-384-alpha.png", frames: 8, rows: 1, duration: 100, loop: false, upOnly: true },
  breach: { file: "breach-384-alpha.png", frames: 8, rows: 1, duration: 90, loop: false, upOnly: true },
  death: { file: "death-384-alpha.png", frames: 8, rows: 4, duration: 110, loop: false },
};

const directions = {
  up: { row: 0, degrees: 0, label: "UP" },
  down: { row: 1, degrees: 180, label: "DOWN" },
  left: { row: 2, degrees: 270, label: "LEFT" },
  right: { row: 3, degrees: 90, label: "RIGHT" },
};

const state = { animation: "walk", direction: "up", frame: 0, playing: true, speed: 1, lastTime: 0 };
const sprite = document.querySelector("#sprite");
const framesRoot = document.querySelector("#frames");
const playPause = document.querySelector("#playPause");
const directionRune = document.querySelector(".direction-rune");

function config() { return atlas[state.animation]; }
function effectiveRow() { return config().upOnly ? 0 : directions[state.direction].row; }

function applySprite(target, frame, displaySize = SOURCE_FRAME) {
  const item = config();
  const row = state.animation === "idle" ? 0 : effectiveRow();
  const column = state.animation === "idle" ? directions[state.direction].row : frame;
  const scale = displaySize / SOURCE_FRAME;
  target.style.backgroundImage = `url("${ASSET_ROOT}/${item.file}")`;
  target.style.backgroundSize = `${item.frames === 1 ? 4 * SOURCE_FRAME * scale : 8 * SOURCE_FRAME * scale}px ${item.rows * SOURCE_FRAME * scale}px`;
  target.style.backgroundPosition = `${-column * SOURCE_FRAME * scale}px ${-row * SOURCE_FRAME * scale}px`;
}

function renderTimeline() {
  const count = config().frames;
  framesRoot.replaceChildren();
  for (let index = 0; index < count; index += 1) {
    const button = document.createElement("button");
    button.type = "button";
    button.className = `frame${index === state.frame ? " active" : ""}`;
    button.dataset.label = String(index + 1).padStart(2, "0");
    button.setAttribute("aria-label", `Кадр ${index + 1}`);
    const preview = document.createElement("span");
    preview.className = "frame-sprite";
    applySprite(preview, index, 64);
    button.append(preview);
    button.addEventListener("click", () => { state.frame = index; state.playing = false; sync(); });
    framesRoot.append(button);
  }
}

function sync({ rebuild = false } = {}) {
  state.frame = Math.min(state.frame, config().frames - 1);
  applySprite(sprite, state.frame, sprite.clientWidth || SOURCE_FRAME);
  sprite.classList.remove("is-switching");
  requestAnimationFrame(() => sprite.classList.add("is-switching"));
  document.querySelector("#stateReadout").textContent = state.animation.toUpperCase();
  document.querySelector("#directionReadout").textContent = `${directions[state.direction].label} / ${String(directions[state.direction].degrees).padStart(3, "0")}°`;
  document.querySelector("#frameReadout").textContent = `${String(state.frame + 1).padStart(2, "0")} / ${String(config().frames).padStart(2, "0")}`;
  document.querySelector("#timelineName").textContent = `${state.animation.toUpperCase()} · ${directions[state.direction].label}`;
  directionRune.style.transform = `rotate(${directions[state.direction].degrees}deg)`;
  playPause.textContent = state.playing ? "PAUSE" : "PLAY";
  document.querySelectorAll("[data-animation]").forEach(button => button.classList.toggle("active", button.dataset.animation === state.animation));
  document.querySelectorAll("[data-direction]").forEach(button => {
    button.classList.toggle("active", button.dataset.direction === state.direction);
    button.disabled = config().upOnly && button.dataset.direction !== "up";
  });
  if (rebuild) renderTimeline();
  else document.querySelectorAll(".frame").forEach((frame, index) => frame.classList.toggle("active", index === state.frame));
}

document.querySelector("#animationControls").addEventListener("click", event => {
  const button = event.target.closest("[data-animation]");
  if (!button) return;
  state.animation = button.dataset.animation;
  if (config().upOnly) state.direction = "up";
  state.frame = 0;
  state.playing = true;
  sync({ rebuild: true });
});

document.querySelector("#directionControls").addEventListener("click", event => {
  const button = event.target.closest("[data-direction]");
  if (!button || button.disabled) return;
  state.direction = button.dataset.direction;
  state.frame = 0;
  sync({ rebuild: true });
});

playPause.addEventListener("click", () => { state.playing = !state.playing; sync(); });
document.querySelector("#previousFrame").addEventListener("click", () => { state.playing = false; state.frame = (state.frame - 1 + config().frames) % config().frames; sync(); });
document.querySelector("#nextFrame").addEventListener("click", () => { state.playing = false; state.frame = (state.frame + 1) % config().frames; sync(); });
document.querySelector("#speed").addEventListener("input", event => {
  state.speed = Number(event.target.value);
  document.querySelector("#speedValue").textContent = `${state.speed.toFixed(2)}×`;
});

function tick(time) {
  if (state.playing && time - state.lastTime >= config().duration / state.speed) {
    const last = state.frame === config().frames - 1;
    state.frame = last ? (config().loop ? 0 : state.frame) : state.frame + 1;
    if (last && !config().loop) state.playing = false;
    state.lastTime = time;
    sync();
  }
  requestAnimationFrame(tick);
}

renderTimeline();
sync();
requestAnimationFrame(tick);

const environmentCatalog = [
  { id: "tree-oak", label: "TREE OAK", type: "grow", file: "../assets/sprite-atlases/tree-oak/runtime-384/tree-oak-grow-384-alpha.png" },
  { id: "tree-pine", label: "TREE PINE", type: "grow", file: "../assets/sprite-atlases/tree-pine/runtime-384/tree-pine-grow-384-alpha.png" },
  { id: "rock-a", label: "ROCK A", type: "grow", file: "../assets/sprite-atlases/rock-a/runtime-384/rock-a-grow-384-alpha.png" },
  { id: "rock-b", label: "ROCK B", type: "static", file: "../assets/sprite-atlases/rock-b/runtime-384/rock-b-idle-384-alpha.png" },
  { id: "rock-c", label: "ROCK C", type: "static", file: "../assets/sprite-atlases/rock-c/runtime-384/rock-c-idle-384-alpha.png" },
  { id: "res-gold", label: "GOLD", type: "resource", file: "../assets/sprite-atlases/res-gold/runtime-384/res-gold-idle-384-alpha.png" },
  { id: "res-wood", label: "WOOD", type: "resource", file: "../assets/sprite-atlases/res-wood/runtime-384/res-wood-idle-384-alpha.png" },
  { id: "res-stone", label: "STONE", type: "resource", file: "../assets/sprite-atlases/res-stone/runtime-384/res-stone-idle-384-alpha.png" },
];

const environmentState = { selected: "tree-oak", frame: 7, growthPlaying: true, elapsed: 0 };
const environmentRoot = document.querySelector("#environmentAssets");

function renderEnvironmentCatalog() {
  environmentRoot.replaceChildren();
  environmentCatalog.forEach((asset) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = `asset-token${asset.id === environmentState.selected ? " active" : ""}`;
    button.dataset.asset = asset.id;
    button.setAttribute("aria-label", asset.label);
    const visual = document.createElement("span");
    visual.className = "asset-visual";
    visual.style.backgroundImage = `url("${asset.file}")`;
    if (asset.type === "grow") {
      visual.style.backgroundSize = "800% 100%";
      visual.style.backgroundPosition = `${environmentState.frame * (100 / 7)}% 0`;
    }
    const label = document.createElement("span");
    label.className = "asset-label";
    label.textContent = asset.label;
    button.append(visual, label);
    button.addEventListener("click", () => {
      environmentState.selected = asset.id;
      if (asset.type === "grow") environmentState.growthPlaying = !environmentState.growthPlaying;
      document.querySelector("#assetName").textContent = asset.label;
      document.querySelector("#assetType").textContent = asset.type === "grow" ? "GROW · 08F" : asset.type.toUpperCase();
      renderEnvironmentCatalog();
    });
    environmentRoot.append(button);
  });
}

function stepEnvironment(ms) {
  if (!environmentState.growthPlaying) return;
  environmentState.elapsed += ms;
  if (environmentState.elapsed < 150) return;
  environmentState.elapsed %= 150;
  environmentState.frame = (environmentState.frame + 1) % 8;
  document.querySelectorAll(".asset-token").forEach((token) => {
    const asset = environmentCatalog.find((item) => item.id === token.dataset.asset);
    if (asset?.type === "grow") token.querySelector(".asset-visual").style.backgroundPosition = `${environmentState.frame * (100 / 7)}% 0`;
  });
}

let environmentLastTime = performance.now();
function environmentTick(time) {
  stepEnvironment(time - environmentLastTime);
  environmentLastTime = time;
  requestAnimationFrame(environmentTick);
}

window.advanceTime = (ms) => { stepEnvironment(ms); };
window.render_game_to_text = () => JSON.stringify({
  view: "sprite-lab",
  unit: { animation: state.animation, direction: state.direction, frame: state.frame, playing: state.playing },
  environment: { selected: environmentState.selected, growthFrame: environmentState.frame, playing: environmentState.growthPlaying },
  coordinateSystem: "DOM preview; origin upper-left; x right; y down",
});

renderEnvironmentCatalog();
requestAnimationFrame(environmentTick);

const buildingAtlas = {
  idle: { file: "watchtower-idle-384-alpha.png", frames: 5, duration: 180, loop: true },
  attack: { file: "watchtower-attack-384-alpha.png", frames: 4, duration: 90, loop: false },
  destroy: { file: "watchtower-destroy-384-alpha.png", frames: 5, duration: 130, loop: false },
  spawn: { file: "watchtower-spawn-384-alpha.png", frames: 5, duration: 180, loop: false },
  pulse: { file: "watchtower-pulse-384-alpha.png", frames: 4, duration: 140, loop: false },
};
const buildingCatalog = {
  watchtower: { name: "WARDEN'S<br />POST", description: "Rebuilt as a low cardboard crossbow post: flat board-token footprint, exposed paper edge and locked 255px scale." },
  ranger: { name: "GARRISON<br />RANGER", description: "The same 255px production contract, refitted with a rapid crossbow, arrow rack and hunting optics." },
  tracker: { name: "CROWN<br />TRACKER", description: "Royal long-range upgrade with a scanning rune-optics ring, precise launcher and shared ranger bolt." },
  assassin: { name: "SHADOW<br />ARCHER", description: "Low stealth-crit perch with shrouded stonework, one heavy sniper bolt and a restrained violet-amber charge." },
  ballista: { name: "FORTRESS<br />BALLISTA", description: "Heavy anti-air platform with a steel-and-wood swivel, amber ether lens, armored bolt and metallic impact." },
  scorpion: { name: "SKY<br />SCORPION", description: "Single-shot ether-harpoon upgrade with a segmented tail counterweight, locked 255px body scale and shared Ballista projectile family." },
  hailstorm: { name: "HAILSTORM<br />BALLISTA", description: "Anti-swarm repeater with a fan-loaded bolt rack, spinning string drum and a compact amber volley impact." },
  cannon: { name: "FIELD<br />CANNON", description: "Volatile dark-bronze siege cannon with alchemical breech glow, recoil rails, heated shot and a compact debris-ring impact." },
  mortar: { name: "SIEGE<br />MORTAR", description: "High-angle heavy artillery with a reinforced short tube, armor-piercing shells, arcing projectile and broad amber ground-burst." },
  grapeshot: { name: "GRAPESHOT<br />BATTERY", description: "Seven-barrel scatter battery with a synchronized fan volley, heated bronze pellets and a wide low impact spread." },
  palisade: { name: "LIVING<br />PALISADE", description: "Living-wood thorn emplacement with green-amber sap channels, launched stake and splinter-vine impact." },
  obelisk: { name: "VOID<br />OBELISK", description: "Captured-void anti-machine tower with a levitating violet monolith, gold rune bands and controlled arc-shatter discharge." },
  beacon: { name: "SUN<br />BEACON", description: "Radiant anti-air focus with a pale-stone solar platform, warm gold lens, compact sun-bolt and controlled halo impact." },
  sawmill: { name: "TIMBER<br />SAWMILL", description: "Economic timber mill with locked 255px body scale, subtle saw-wheel idle and contained collapse frames.", actions: ["idle", "destroy"] },
  quarry: { name: "STONE<br />QUARRY", description: "Stone economy rig with a pulley pick-arm, stable quarry pit footprint and contained rubble collapse.", actions: ["idle", "destroy"] },
  castle: { name: "GRIMHOLD<br />FORTRESS", description: "Player base keep with a pulsing seal-crystal, locked fortress footprint and ten-frame breach collapse.", actions: ["idle", "destroy"], actionConfig: { destroy: { frames: 10, duration: 160 } } },
  "spawn-cave": { name: "VOID CAVE", description: "Enemy portal ring with locked 255px footprint, slow vortex idle and contained spawn flare.", actions: ["idle", "spawn"], actionConfig: { idle: { duration: 720 } } },
  "pal-ward": { name: "PALADIN<br />WARD", description: "Holy seal platform with stable stone footprint and contained pulse flare.", actions: ["idle", "pulse", "destroy"] },
  "pal-censer": { name: "PALADIN<br />CENSER", description: "Radiant support tower with four braziers, gold burst attack and clean projectile/impact set." },
  "pal-reliquary": { name: "PALADIN<br />RELIQUARY", description: "Fortified relic dais with amber core, locked idle scale and contained burst attack." },
  "mage-frost": { name: "FROST<br />FOCUS", description: "Mage frost platform with blue crystal core, stable circular footprint and compact frost impact." },
  "mage-tesla": { name: "TESLA<br />COIL", description: "Mage lightning conduit with copper ringwork, locked core scale and contained electrical discharge." },
  "hunt-snare": { name: "HUNTER<br />SNARE", description: "Living bramble trap ring with stable vine footprint and contained net-impact action." },
};
const buildingState = { id: "watchtower", action: "idle", frame: 0, playing: true, elapsed: 0 };
const buildingSprite = document.querySelector("#buildingSprite");

function buildingConfig() {
  return { ...buildingAtlas[buildingState.action], ...buildingCatalog[buildingState.id].actionConfig?.[buildingState.action] };
}

function renderBuilding() {
  const item = buildingConfig();
  const root = `../assets/sprite-atlases/${buildingState.id}/runtime-384`;
  const file = item.file.replace("watchtower", buildingState.id);
  buildingSprite.style.backgroundImage = `url("${root}/${file}?v=${BUILDING_ASSET_VERSION}")`;
  buildingSprite.style.backgroundSize = `${item.frames * 100}% 100%`;
  buildingSprite.style.backgroundPosition = `${buildingState.frame * (100 / Math.max(1, item.frames - 1))}% 0`;
  document.querySelector("#buildingAction").textContent = buildingState.action.toUpperCase();
  document.querySelector("#buildingFrame").textContent = `${String(buildingState.frame + 1).padStart(2, "0")} / ${String(item.frames).padStart(2, "0")}`;
  const availableActions = buildingCatalog[buildingState.id].actions || ["idle", "attack", "destroy"];
  document.querySelectorAll("[data-building-action]").forEach((button) => {
    const available = availableActions.includes(button.dataset.buildingAction);
    button.disabled = !available;
    button.classList.toggle("active", button.dataset.buildingAction === buildingState.action);
  });
  document.querySelectorAll("[data-building]").forEach((button) => button.classList.toggle("active", button.dataset.building === buildingState.id));
  document.querySelector("#buildingName").innerHTML = buildingCatalog[buildingState.id].name;
  document.querySelector("#buildingDescription").textContent = buildingCatalog[buildingState.id].description;
}

document.querySelector("#buildingSelector").addEventListener("click", (event) => {
  const button = event.target.closest("[data-building]");
  if (!button) return;
  buildingState.id = button.dataset.building;
  buildingState.action = "idle";
  buildingState.frame = 0;
  buildingState.elapsed = 0;
  buildingState.playing = true;
  renderBuilding();
});

document.querySelector("#buildingControls").addEventListener("click", (event) => {
  const button = event.target.closest("[data-building-action]");
  if (!button || button.disabled) return;
  buildingState.action = button.dataset.buildingAction;
  buildingState.frame = 0;
  buildingState.elapsed = 0;
  buildingState.playing = true;
  renderBuilding();
});

function stepBuilding(ms) {
  if (!buildingState.playing) return;
  const item = buildingConfig();
  buildingState.elapsed += ms;
  if (buildingState.elapsed < item.duration) return;
  buildingState.elapsed %= item.duration;
  if (buildingState.frame === item.frames - 1) {
    if (item.loop) buildingState.frame = 0;
    else buildingState.playing = false;
  } else buildingState.frame += 1;
  renderBuilding();
}

let buildingLastTime = performance.now();
function buildingTick(time) {
  stepBuilding(time - buildingLastTime);
  buildingLastTime = time;
  requestAnimationFrame(buildingTick);
}

const previousAdvanceTime = window.advanceTime;
window.advanceTime = (ms) => { previousAdvanceTime(ms); stepBuilding(ms); };
window.render_game_to_text = () => JSON.stringify({
  view: "sprite-lab",
  unit: { animation: state.animation, direction: state.direction, frame: state.frame, playing: state.playing },
  environment: { selected: environmentState.selected, growthFrame: environmentState.frame, playing: environmentState.growthPlaying },
  building: { id: buildingState.id, action: buildingState.action, frame: buildingState.frame, playing: buildingState.playing },
  coordinateSystem: "DOM preview; origin upper-left; x right; y down",
});

renderBuilding();
requestAnimationFrame(buildingTick);
