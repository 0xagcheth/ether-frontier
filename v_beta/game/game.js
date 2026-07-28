let cachedRect = null;
const SPRITE_VER = 20;
const ATLAS_VER = 1;
const GAME_ATLAS = window.GAME_SPRITE_ATLAS || null;
const BUILDING_ATLASES = window.BUILDING_SPRITE_ATLASES || null;
const GAME_ATLAS_IMAGE = `../assets/runtime/atlases/game_atlas.png?v=${ATLAS_VER}`;
const BUILDING_ATLAS_DIR = "../assets/runtime/atlases/buildings";

function atlasRule(selector, frameName, boxW, boxH, alignY = "center") {
  const entry = GAME_ATLAS?.frames?.[frameName];
  const atlasSize = GAME_ATLAS?.meta?.size;
  if (!entry || !atlasSize) return "";

  const source = entry.sourceSize;
  const offset = entry.spriteSourceSize;
  const frame = entry.frame;
  const scale = Math.min(boxW / source.w, boxH / source.h);
  const padX = (boxW - source.w * scale) / 2;
  const padY = alignY === "bottom" ? boxH - source.h * scale : (boxH - source.h * scale) / 2;
  const posX = padX - (frame.x - offset.x) * scale;
  const posY = padY - (frame.y - offset.y) * scale;

  return `${selector}{background-image:url('${GAME_ATLAS_IMAGE}')!important;background-size:${atlasSize.w * scale}px ${atlasSize.h * scale}px!important;background-position:${posX}px ${posY}px!important;background-repeat:no-repeat!important;}`;
}

function atlasStripRule(selector, animName, boxW, boxH, alignY = "bottom") {
  const anim = GAME_ATLAS?.animations?.[animName];
  if (!anim?.frames?.length) return "";
  return atlasRule(selector, anim.frames[0], boxW, boxH, alignY);
}

function buildingAtlasRule(selector, building, action, boxW, boxH, alignY = "bottom") {
  const atlas = BUILDING_ATLASES?.[building];
  const anim = atlas?.animations?.[action];
  const atlasSize = atlas?.meta?.size;
  if (!anim?.frames?.length || !atlasSize) return "";

  const firstEntry = atlas.frames?.[anim.frames[0]];
  if (!firstEntry) return "";
  const source = firstEntry.sourceSize;
  const scale = Math.min(boxW / source.w, boxH / source.h);
  const image = `${BUILDING_ATLAS_DIR}/${atlas.meta.image}?v=${ATLAS_VER}`;
  const keyframeName = `building-${building}-${action}`;
  const frameCss = anim.frames.map((frameName, index) => {
    const entry = atlas.frames?.[frameName];
    if (!entry) return "";
    const offset = entry.spriteSourceSize;
    const frame = entry.frame;
    const padX = (boxW - entry.sourceSize.w * scale) / 2;
    const padY = alignY === "bottom" ? boxH - entry.sourceSize.h * scale : (boxH - entry.sourceSize.h * scale) / 2;
    const posX = padX - (frame.x - offset.x) * scale;
    const posY = padY - (frame.y - offset.y) * scale;
    const start = (index / anim.frames.length) * 100;
    const end = ((index + 1) / anim.frames.length) * 100 - 0.01;
    return `${start.toFixed(3)}%,${Math.max(start, end).toFixed(3)}%{background-position:${posX}px ${posY}px;}`;
  }).filter(Boolean).join("");
  const lastEntry = atlas.frames?.[anim.frames[anim.frames.length - 1]];
  const lastOffset = lastEntry.spriteSourceSize;
  const lastFrame = lastEntry.frame;
  const lastPadX = (boxW - lastEntry.sourceSize.w * scale) / 2;
  const lastPadY = alignY === "bottom" ? boxH - lastEntry.sourceSize.h * scale : (boxH - lastEntry.sourceSize.h * scale) / 2;
  const lastPosX = lastPadX - (lastFrame.x - lastOffset.x) * scale;
  const lastPosY = lastPadY - (lastFrame.y - lastOffset.y) * scale;
  const duration = anim.durationMs * anim.frames.length;
  const loop = anim.loop ? "infinite" : "1 forwards";

  return `@keyframes ${keyframeName}{${frameCss}100%{background-position:${lastPosX}px ${lastPosY}px;}}${selector}{background-image:url('${image}')!important;background-size:${atlasSize.w * scale}px ${atlasSize.h * scale}px!important;background-repeat:no-repeat!important;animation:${keyframeName} ${duration}ms steps(1,end) ${loop}!important;}`;
}

function injectAtlasStyles() {
  if (!GAME_ATLAS) return;
  const rules = [
    atlasRule(".atlas-res-gold", "res_gold", 18, 18),
    atlasRule(".atlas-res-wood", "res_wood", 18, 18),
    atlasRule(".atlas-res-stone", "res_stone", 18, 18),
    atlasRule(".grid-cell.tree::after", "tree_pine", 48, 64, "bottom"),
    atlasRule('.grid-cell.tree[data-tree="oak"]::after', "tree_oak", 48, 64, "bottom"),
    atlasRule(".grid-cell.stone::before", "rock_a", 40, 34),
    atlasRule('.grid-cell.stone[data-rock="b"]::before', "rock_b", 40, 34),
    atlasRule('.grid-cell.stone[data-rock="c"]::before', "rock_c", 40, 34),
    ...[0, 1, 2, 3, 4].map((frame) => atlasRule(`.grid-cell.stone[data-grow-frame="${frame}"]::before`, `rock_grow_0${frame}`, 40, 40)),
    ...[0, 1, 2, 3, 4].map((frame) => atlasRule(`.grid-cell.tree[data-grow-frame="${frame}"]::after`, `tree_pine_grow_0${frame}`, 48, 64, "bottom")),
    ...[0, 1, 2, 3, 4].map((frame) => atlasRule(`.grid-cell.tree[data-tree="oak"][data-grow-frame="${frame}"]::after`, `tree_oak_grow_0${frame}`, 48, 64, "bottom")),
    buildingAtlasRule(".tower.fire:not([data-spec])::before", "watchtower", "idle", 48, 64),
    buildingAtlasRule(".tower.fire:not([data-spec]).is-attacking::before", "watchtower", "attack", 48, 64),
    buildingAtlasRule(".tower.fire:not([data-spec]).is-destroying::before", "watchtower", "destroy", 48, 64),
    buildingAtlasRule(".tower.ice::before", "sawmill", "idle", 96, 112),
    buildingAtlasRule(".tower.ice.is-destroying::before", "sawmill", "destroy", 96, 112),
    buildingAtlasRule(".tower.storm::before", "quarry", "idle", 96, 112),
    buildingAtlasRule(".tower.storm.is-destroying::before", "quarry", "destroy", 96, 112),
    buildingAtlasRule(".castle:not(.is-destroyed)::before", "castle", "idle", 139, 120),
    buildingAtlasRule(".castle.is-destroyed::before", "castle", "destroy", 139, 120),
    buildingAtlasRule(".spawn-cave:not(.is-spawning)::before", "spawn-cave", "idle", 72, 72),
    buildingAtlasRule(".spawn-cave.is-spawning::before", "spawn-cave", "spawn", 72, 72),
    buildingAtlasRule(".tower.thorn::before", "palisade", "idle", 48, 64),
    buildingAtlasRule(".tower.thorn.is-attacking::before", "palisade", "attack", 48, 64),
    buildingAtlasRule(".tower.thorn.is-destroying::before", "palisade", "destroy", 48, 64),
    buildingAtlasRule(".tower.void::before", "obelisk", "idle", 48, 64),
    buildingAtlasRule(".tower.void.is-attacking::before", "obelisk", "attack", 48, 64),
    buildingAtlasRule(".tower.void.is-destroying::before", "obelisk", "destroy", 48, 64),
    buildingAtlasRule(".tower.sun::before", "beacon", "idle", 48, 64),
    buildingAtlasRule(".tower.sun.is-attacking::before", "beacon", "attack", 48, 64),
    buildingAtlasRule(".tower.sun.is-destroying::before", "beacon", "destroy", 48, 64),
  ].filter(Boolean);
  const style = document.createElement("style");
  style.id = "game-atlas-styles";
  style.textContent = rules.join("\n");
  document.head.appendChild(style);
}

injectAtlasStyles();

const state = {
  gold: 175,
  wood: 30,
  stone: 30,
  lives: 20,
  wave: 1,
  selectedTowerId: null,
  buildType: null,
  nextTowerId: 1,
  nextEnemyId: 1,
  nextProjectileId: 1,
  towers: {},
  enemies: [],
  projectiles: [],
  running: false,
  gameOver: false,
  speed: 1,
  lastTime: 0,
  spawnTimer: 0,
  spawned: 0,
  slowUntil: 0,
  baseShield: 0,
  heroId: null,
  heroActive: false,
  heroReturning: false,
  heroChargeKills: 0,
  heroPulse: 0,
  heroX: 50,
  heroY: 58,
  heroAttackCooldown: 0,
  runeShopOpen: false,
  unlockedBuildings: [],
  clearedCells: new Set(["2,21", "9,21", "2,16", "9,16"]),
  resourceCells: new Map(),
  regrowthQueue: [],
  growingCells: new Map(),
  rockBCells: new Set(),
  defaultTowersSeeded: false,
  grid: {
    cols: 12,
    rows: 0,
    cellSize: 0,
  },
};

const towerDefs = {
  fire: { name: "Ветровой дозор", cost: 45, damage: 25, range: 112, rate: 0.78, color: "#ffb23f", attacks: true },
  ice: { name: "Плотницкий круг", cost: 35, color: "#7bc46c", attacks: false, role: "Возвращает Живое древо после каждой волны." },
  storm: { name: "Каменный круг", cost: 35, color: "#aab2bd", attacks: false, role: "Возвращает Камень памяти после каждой волны." },
  thorn: { name: "Плетень Корня", cost: 100, damage: 16, range: 112, rate: 0.62, color: "#79d26b", versus: "земля ×1.5 · воздух ×0.75 · машины ×0.65" },
  void:  { name: "Камень Имени", cost: 125, damage: 34, range: 96, rate: 1.35, color: "#8e86c8", versus: "машины ×1.8 · воздух ×0.6 · земля ×1.0" },
  sun:   { name: "Солнечная мера", cost: 135, damage: 22, range: 138, rate: 0.82, color: "#e4b84f", versus: "воздух ×1.55 · земля ×0.9 · машины ×0.8" },
};
const watchtowerSpecializations = {
  infantry: {
    name: "Стрелец Ветра",
    mark: "I",
    target: "ground",
    damage: 44,
    range: 122,
    rate: 0.58,
    note: "Против пехоты. Быстрый самострел и архивный дальномер.",
    upgrades: {
      3: { name: "Птичья метка", note: "Каждая третья атака наносит пехоте двойной урон." },
      4: { name: "Добивающий болт", note: "По пехоте ниже 35% здоровья: +60% урона." },
      5: { name: "Перевод огня", note: "После убийства немедленно стреляет в следующую цель." },
    },
    subtypes: {
      tracker: {
        name: "Соколиный круг",
        mark: "S",
        note: "Дальний дозор, метка цели и надёжное замедление пехоты.",
        upgrades: {
          7: { name: "Дальний дозор", note: "Увеличивает дальность и приоритет врагов возле базы." },
          8: { name: "Связанная цель", note: "Отмеченные враги замедляются." },
          9: { name: "Соколиная охота", note: "Перевод огня чаще находит новую цель." },
        },
      },
      assassin: {
        name: "Тихий омут",
        mark: "X",
        note: "Скрытый пост для критических выстрелов по сильной пехоте.",
        upgrades: {
          7: { name: "Слабая строка", note: "Птичья метка наносит ещё больше урона." },
          8: { name: "Тихое имя", note: "Добивание срабатывает при более высоком здоровье цели." },
          9: { name: "Выстрел без записи", note: "Каждая пятая атака становится критической." },
        },
      },
    },
  },
  air: {
    name: "Громовой самострел",
    mark: "A",
    target: "air",
    damage: 36,
    range: 156,
    rate: 0.82,
    note: "Против воздуха. Тяжёлые болты, громовая линза и большой радиус.",
    upgrades: {
      3: { name: "Тяжёлый болт", note: "Пробивает две воздушные цели на одной линии." },
      4: { name: "Громовой прицел", note: "Первый выстрел по новой цели наносит +80% урона." },
      5: { name: "Обрыв полёта", note: "Воздушная цель замедляется на 2 секунды." },
    },
    subtypes: {
      scorpion: {
        name: "Змеиный гарпун",
        mark: "N",
        note: "Сильный одиночный удар по прочным воздушным целям.",
        upgrades: {
          7: { name: "Гарпун Прави", note: "Больше урона самой прочной воздушной цели." },
          8: { name: "Слом крыла", note: "Воздушное замедление длится дольше." },
          9: { name: "Приговор неба", note: "Первый выстрел по новой цели становится сокрушительным." },
        },
      },
      hail: {
        name: "Стрибожья метель",
        mark: "G",
        note: "Веер болтов против роёв слабых летающих врагов.",
        upgrades: {
          7: { name: "Двойная тетива", note: "Пробивает больше воздушных целей." },
          8: { name: "Крошащие болты", note: "Часть урона переходит на соседние воздушные цели." },
          9: { name: "Метель Стрибога", note: "Повышает скорострельность против воздушных роёв." },
        },
      },
    },
  },
  siege: {
    name: "Громовой станок",
    mark: "T",
    target: "any",
    damage: 14,
    range: 118,
    rate: 1.15,
    splash: 42,
    note: "Против машин. Громовые заряды с небольшим радиусом взрыва.",
    upgrades: {
      3: { name: "Каменная сечка", note: "Увеличивает радиус взрыва." },
      4: { name: "Ломающий запись заряд", note: "Против машин: +100% урона." },
      5: { name: "Глухой гром", note: "Машины замедляются, пехота ненадолго оглушается." },
    },
    subtypes: {
      mortar: {
        name: "Медвежья ступа",
        mark: "M",
        note: "Медленная навесная стрельба с высоким уроном по машинам.",
        upgrades: {
          7: { name: "Глубинный заряд", note: "Ещё больше урона против машин." },
          8: { name: "Трещина в броне", note: "После попадания машина получает повышенный урон." },
          9: { name: "Протокол «Ступа»", note: "Каждый третий выстрел наносит машине мощный удар." },
        },
      },
      grapeshot: {
        name: "Семистрельный раскат",
        mark: "K",
        note: "Широкая область поражения и подавление группы вокруг взрыва.",
        upgrades: {
          7: { name: "Широкий раскат", note: "Увеличивает радиус взрыва." },
          8: { name: "Тяжёлое эхо", note: "Замедление в области становится сильнее." },
          9: { name: "Семь голосов", note: "Повышает скорострельность батареи." },
        },
      },
    },
  },
};
const baseBuildings = ["fire", "ice", "storm"];
const MAX_TOWER_LEVEL = 12;
const MAX_ECONOMY_LEVEL = 4;
// Index = level you're upgrading TO. [sawmills, quarries] required.
const COMBAT_UPGRADE_ECON_REQ = [
  [0, 0], // 0 unused
  [0, 0], // to L1 unused
  [0, 0], // to L2: free
  [2, 0], // to L3: 2 sawmills
  [2, 1], // to L4: 2 sawmills + 1 quarry
  [3, 1], // to L5: 3 sawmills + 1 quarry
  [3, 2], // to L6: 3 sawmills + 2 quarries
  [4, 2], // to L7: 4 sawmills + 2 quarries
  [4, 3], // to L8: 4 sawmills + 3 quarries
  [5, 3], // to L9: 5 sawmills + 3 quarries
  [5, 4], // to L10+
  [5, 4],
  [5, 4],
];
const SPECIAL_BUILD_CAPS = { void: 6, sun: 4, thorn: 4 };
// Index = already-placed count. [minLevel, neededCount] = need N fire towers at level >= minLevel.
const SPECIAL_BUILD_REQS = {
  void:  [[2,1],[2,2],[3,1],[3,2],[4,1],[4,2]],
  sun:   [[2,1],[3,1],[3,2],[4,1]],
  thorn: [[2,1],[3,1],[3,2],[4,1]],
};
const RESOURCE_MIN_RATIO = 0.4;
const RESOURCE_LAYOUT_SEED = (Math.random() * 9973) | 0;
const RESOURCE_CAP = 350;
const ROAD_BLOCK_DISTANCE = 20;
const ROAD_RAID_CELL_DISTANCE = 390 / 12;
const ROAD_EDGE_RAID_DISTANCE = ROAD_BLOCK_DISTANCE + ROAD_RAID_CELL_DISTANCE * 0.55;
const ECONOMY_BUILDING_HP = 12;
const WATCHTOWER_HP = 10;
const HERO_FIELD_POSITION = { x: 50, y: 58 };
const HERO_BASE_POSITION = { x: 50, y: 70.5 };
const HERO_RETURN_SPEED = 8;
const HERO_ATTACK_RANGE = 42;
const HERO_ATTACK_RATE = 0.72;
const HERO_ATTACK_DAMAGE = 38;
const RAIDER_ATTACK_RANGE = ROAD_BLOCK_DISTANCE + ROAD_RAID_CELL_DISTANCE;
const RAIDER_ATTACK_RATE = 0.8;
const RAIDER_DAMAGE = {
  air: 1,
  ground: 1,
  machine: 1,
};
const enemyNodes = new Map();
const projectileNodes = new Map();
const hudCache = {};
const defaultTowerCells = [
  { col: 2, row: 21, type: "fire" },
  { col: 9, row: 21, type: "fire" },
];
const extraRuneDefs = {
  thorn: { name: "Плетень Корня", cost: 200, mark: "♣", note: "Частый ответ. +50% против наземных; слабее против машин и воздуха." },
  void:  { name: "Камень Имени", cost: 250, mark: "◇", note: "Разрывает Серую директиву. +80% против машин; слабее против воздуха." },
  sun:   { name: "Солнечная мера", cost: 270, mark: "☼", note: "Дальний ответ. +55% против воздуха; увеличенный радиус." },
};
const heroDefs = {
  paladin: {
    name: "Борислав Громовик",
    race: "Хранитель Грома",
    mark: "✚",
    cost: 150,
    skills: [
      "Активное: Громовой ответ — вступает в волну и даёт 3 щита.",
      "Пассивное: Договор защиты — Последний узел выдерживает больше ударов.",
      "Пассивное: Злато службы — волны приносят больше Злата договора.",
    ],
  },
  mage: {
    name: "Аяна Читающая",
    race: "Хранительница Имени",
    mark: "✦",
    cost: 210,
    skills: [
      "Активное: Возврат связи — вступает в волну, даёт щит и замедляет носителей.",
      "Пассивное: Связь слоёв — рабочие круги дают на 15% больше материала.",
      "Пассивное: Дальний смысл — Ветровые дозоры видят дальше.",
    ],
  },
  hunter: {
    name: "Амба Следопытка",
    race: "Хранительница Троп",
    mark: "◆",
    cost: 180,
    skills: [
      "Активное: Живая тропа — вступает в волну, даёт щит и ранит носителей.",
      "Пассивное: Возврат следа — наземные враги дают на 20% больше Злата.",
      "Пассивное: Разведка — первый ответ башен становится сильнее.",
    ],
  },
};

// ── Enemy sprite animation metadata (generated from assets/runtime/sprites/enemies/*.png) ──
const ENEMY_SPRITES = {
  warrior: { fw:128, fh:128, ds:44, dirs:true, assetDir:'../assets/runtime/sprites/enemies', frames: {
    spawn:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    walk:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    attack:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    death:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    breach:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
  }},
  fast: { fw:448, fh:448, gutter:224, ds:52, dirs:true, assetDir:'../assets/runtime/sprites/enemies', frames: {
    spawn:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    walk:  {front:5, back:5, '3qr':5, '3ql':5, sider:5, sidel:5},
    attack:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    death:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    breach:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
  }},
  brute: { fw:144, fh:144, ds:52, dirs:true, frames: {
    spawn:  {front:4, back:4, '3qr':4, '3ql':4, sider:4, sidel:4},
    walk:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    attack:  {front:4, back:4, '3qr':4, '3ql':4, sider:4, sidel:4},
    death:  {front:4, back:4, '3qr':4, '3ql':4, sider:4, sidel:4},
    breach:  {front:4, back:4, '3qr':4, '3ql':4, sider:4, sidel:4},
  }},
  raider: { fw:80, fh:80, ds:40, dirs:true, frames: {
    spawn:  {front:4, back:4, '3qr':4, '3ql':4, sider:4, sidel:4},
    walk:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    attack:  {front:6, back:5, '3qr':6, '3ql':5, sider:7, sidel:6},
    death:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    breach:  {front:4, back:4, '3qr':4, '3ql':4, sider:4, sidel:4},
  }},
  witch_doc: { fw:72, fh:72, ds:36, dirs:true, frames: {
    spawn:  {front:5, back:5, '3qr':5, '3ql':5, sider:5, sidel:5},
    walk:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    attack:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    death:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    breach:  {front:5, back:5, '3qr':5, '3ql':5, sider:5, sidel:5},
  }},
  slime: { fw:88, fh:88, ds:44, dirs:true, frames: {
    spawn:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    walk:  {front:5, back:5, '3qr':5, '3ql':5, sider:5, sidel:5},
    attack:  {front:5, back:5, '3qr':6, '3ql':6, sider:5, sidel:5},
    death:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    breach:  {front:5, back:5, '3qr':5, '3ql':5, sider:5, sidel:5},
  }},
  air: { fw:80, fh:80, ds:40, dirs:true, frames: {
    spawn:  {front:5, back:5, '3qr':5, '3ql':5, sider:5, sidel:5},
    walk:  {front:5, back:5, '3qr':5, '3ql':5, sider:5, sidel:5},
    attack:  {front:6, back:5, '3qr':6, '3ql':6, sider:5, sidel:5},
    death:  {front:7, back:7, '3qr':7, '3ql':7, sider:7, sidel:7},
    breach:  {front:5, back:5, '3qr':5, '3ql':5, sider:5, sidel:5},
  }},
  wraith: { fw:88, fh:88, ds:44, dirs:true, frames: {
    spawn:  {front:5, back:5, '3qr':5, '3ql':5, sider:5, sidel:5},
    walk:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    attack:  {front:5, back:5, '3qr':5, '3ql':5, sider:4, sidel:5},
    death:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    breach:  {front:4, back:4, '3qr':4, '3ql':4, sider:4, sidel:4},
  }},
  berserker: { fw:88, fh:88, ds:44, dirs:true, frames: {
    spawn:  {front:5, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    walk:  {front:5, back:5, '3qr':5, '3ql':5, sider:5, sidel:5},
    attack:  {front:6, back:6, '3qr':6, '3ql':6, sider:5, sidel:5},
    death:  {front:6, back:6, '3qr':6, '3ql':5, sider:4, sidel:4},
    breach:  {front:5, back:5, '3qr':5, '3ql':5, sider:5, sidel:5},
  }},
  shield: { fw:96, fh:96, ds:48, dirs:true, frames: {
    spawn:  {front:5, back:5, '3qr':5, '3ql':5, sider:5, sidel:5},
    walk:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    attack:  {front:5, back:5, '3qr':5, '3ql':5, sider:5, sidel:5},
    death:  {front:6, back:6, '3qr':6, '3ql':7, sider:7, sidel:7},
    breach:  {front:5, back:5, '3qr':5, '3ql':5, sider:5, sidel:5},
  }},
  tunneler: { fw:92, fh:92, ds:46, dirs:true, frames: {
    spawn:  {front:5, back:5, '3qr':5, '3ql':5, sider:5, sidel:5},
    walk:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    attack:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    death:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    breach:  {front:5, back:5, '3qr':5, '3ql':5, sider:5, sidel:5},
  }},
  necro: { fw:80, fh:80, ds:40, dirs:true, frames: {
    spawn:  {front:5, back:5, '3qr':5, '3ql':5, sider:5, sidel:5},
    walk:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    attack:  {front:6, back:6, '3qr':6, '3ql':6, sider:5, sidel:5},
    death:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    breach:  {front:5, back:5, '3qr':5, '3ql':5, sider:5, sidel:5},
  }},
  bomber: { fw:88, fh:88, ds:44, dirs:true, frames: {
    spawn:  {front:5, back:5, '3qr':5, '3ql':5, sider:5, sidel:5},
    walk:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    attack:  {front:6, back:7, '3qr':7, '3ql':7, sider:7, sidel:7},
    death:  {front:7, back:7, '3qr':7, '3ql':6, sider:7, sidel:7},
    breach:  {front:5, back:5, '3qr':5, '3ql':5, sider:5, sidel:5},
  }},
  spellbreak: { fw:88, fh:88, ds:44, dirs:true, frames: {
    spawn:  {front:5, back:5, '3qr':5, '3ql':5, sider:5, sidel:5},
    walk:  {front:5, back:5, '3qr':5, '3ql':5, sider:5, sidel:5},
    attack:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    death:  {front:6, back:6, '3qr':6, '3ql':6, sider:7, sidel:6},
    breach:  {front:5, back:5, '3qr':5, '3ql':5, sider:5, sidel:5},
  }},
  spider: { fw:104, fh:104, ds:52, dirs:true, frames: {
    spawn:  {front:5, back:5, '3qr':5, '3ql':5, sider:5, sidel:5},
    walk:  {front:5, back:5, '3qr':5, '3ql':5, sider:5, sidel:5},
    attack:  {front:5, back:5, '3qr':5, '3ql':5, sider:5, sidel:5},
    death:  {front:6, back:6, '3qr':6, '3ql':5, sider:6, sidel:6},
    breach:  {front:5, back:5, '3qr':5, '3ql':5, sider:5, sidel:5},
  }},
  summoner: { fw:120, fh:120, ds:60, dirs:true, frames: {
    spawn:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    walk:  {front:5, back:5, '3qr':5, '3ql':5, sider:5, sidel:5},
    attack:  {front:7, back:7, '3qr':7, '3ql':7, sider:7, sidel:7},
    death:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    breach:  {front:5, back:5, '3qr':4, '3ql':5, sider:5, sidel:5},
  }},
  machine: { fw:104, fh:104, ds:52, dirs:true, frames: {
    spawn:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    walk:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    attack:  {front:6, back:6, '3qr':4, '3ql':5, sider:6, sidel:6},
    death:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    breach:  {front:5, back:5, '3qr':5, '3ql':5, sider:5, sidel:5},
  }},
  iron_jug: { fw:120, fh:120, ds:60, dirs:true, frames: {
    spawn:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    walk:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    attack:  {front:5, back:6, '3qr':5, '3ql':5, sider:6, sidel:6},
    death:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    breach:  {front:3, back:3, '3qr':3, '3ql':4, sider:3, sidel:3},
  }},
  golem: { fw:144, fh:144, ds:72, dirs:true, frames: {
    spawn:  {front:5, back:5, '3qr':5, '3ql':5, sider:5, sidel:5},
    walk:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    attack:  {front:6, back:6, '3qr':6, '3ql':6, sider:5, sidel:6},
    death:  {front:7, back:7, '3qr':7, '3ql':7, sider:7, sidel:7},
    breach:  {front:4, back:4, '3qr':3, '3ql':4, sider:4, sidel:4},
  }},
  miniBossGround: { fw:120, fh:120, ds:60, dirs:true, frames: {
    spawn:  {front:5, back:6, '3qr':5, '3ql':5, sider:6, sidel:6},
    walk:  {front:5, back:5, '3qr':5, '3ql':5, sider:5, sidel:5},
    attack:  {front:5, back:6, '3qr':5, '3ql':7, sider:7, sidel:6},
    death:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    breach:  {front:5, back:5, '3qr':5, '3ql':5, sider:4, sidel:4},
  }},
  bossGround: { fw:144, fh:144, ds:72, dirs:true, frames: {
    spawn:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    walk:  {front:6, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    attack:  {front:6, back:5, '3qr':5, '3ql':6, sider:5, sidel:4},
    death:  {front:6, back:4, '3qr':5, '3ql':5, sider:3, sidel:6},
    breach:  {front:1, back:1, '3qr':1, '3ql':1, sider:1, sidel:1},
  }},
  bossAir: { fw:144, fh:144, ds:72, dirs:true, frames: {
    spawn:  {front:4, back:5, '3qr':5, '3ql':3, sider:4, sidel:5},
    walk:  {front:5, back:5, '3qr':5, '3ql':5, sider:4, sidel:4},
    attack:  {front:3, back:3, '3qr':2, '3ql':2, sider:3, sidel:1},
    death:  {front:5, back:5, '3qr':5, '3ql':7, sider:5, sidel:7},
    breach:  {front:7, back:4, '3qr':2, '3ql':4, sider:2, sidel:1},
  }},
  bossMachine: { fw:144, fh:144, ds:72, dirs:true, frames: {
    spawn:  {front:4, back:4, '3qr':5, '3ql':4, sider:4, sidel:1},
    walk:  {front:1, back:4, '3qr':2, '3ql':4, sider:3, sidel:2},
    attack:  {front:3, back:4, '3qr':3, '3ql':3, sider:2, sidel:3},
    death:  {front:6, back:5, '3qr':7, '3ql':6, sider:3, sidel:5},
    breach:  {front:5, back:5, '3qr':5, '3ql':5, sider:5, sidel:5},
  }},
  dread_lord: { fw:144, fh:144, ds:72, dirs:true, frames: {
    spawn:  {front:6, back:7, '3qr':4, '3ql':5, sider:2, sidel:3},
    walk:  {front:7, back:6, '3qr':7, '3ql':6, sider:1, sidel:2},
    attack:  {front:4, back:5, '3qr':4, '3ql':6, sider:5, sidel:5},
    death:  {front:7, back:7, '3qr':7, '3ql':8, sider:7, sidel:8},
    breach:  {front:5, back:5, '3qr':5, '3ql':5, sider:4, sidel:6},
  }},
  elder_dragon: { fw:192, fh:192, ds:96, dirs:true, frames: {
    flyin:  3,
    spawn:  {front:4, back:4, '3qr':3, '3ql':5, sider:4, sidel:4},
    walk:  {front:6, back:6, '3qr':4, '3ql':5, sider:1, sidel:3},
    attack:  {front:4, back:3, '3qr':3, '3ql':2, sider:3, sidel:1},
    death:  {front:4, back:6, '3qr':6, '3ql':6, sider:6, sidel:6},
    breach:  {front:4, back:3, '3qr':3, '3ql':4, sider:2, sidel:3},
  }},
};

const ANIM_FPS = { spawn:8, walk:5, walkSide:10, attack:10, death:8, breach:9 };

const enemyDefs = {
  fast:           { name: "Бегуны Глубин", hp: 55, speed: 64, reward: 12, category: "ground" },
  warrior:        { name: "Ратники Чешуи", hp: 90, speed: 42, reward: 14, category: "ground" },
  brute:          { name: "Глиняные тяжеловесы", hp: 120, speed: 38, reward: 17, category: "ground" },
  raider:         { name: "Крюки Имён", hp: 78, speed: 48, reward: 15, category: "ground", canRaid: true },
  witch_doc:      { name: "Серые наставники", hp: 70, speed: 44, reward: 18, category: "ground" },
  slime:          { name: "Навья роса", hp: 100, speed: 36, reward: 16, category: "ground" },
  berserker:      { name: "Красногребневые", hp: 95, speed: 50, reward: 17, category: "ground" },
  shield:         { name: "Хранители Панциря", hp: 140, speed: 34, reward: 19, category: "ground" },
  tunneler:       { name: "Подкопники Давления", hp: 85, speed: 40, reward: 16, category: "ground", canRaid: true },
  necro:          { name: "Зовущие безымянных", hp: 65, speed: 42, reward: 20, category: "ground" },
  bomber:         { name: "Серые носители", hp: 72, speed: 52, reward: 18, category: "air", canRaid: true },
  spellbreak:     { name: "Гасители Ответа", hp: 80, speed: 44, reward: 19, category: "ground" },
  spider:         { name: "Тенётники", hp: 110, speed: 46, reward: 20, category: "ground", canRaid: true },
  summoner:       { name: "Открывающие Промежуток", hp: 88, speed: 38, reward: 24, category: "ground" },
  golem:          { name: "Курганные формы", hp: 200, speed: 28, reward: 30, category: "ground" },
  air:            { name: "Крылатые чешуйники", hp: 62, speed: 58, reward: 17, category: "air", canRaid: true },
  wraith:         { name: "Непомянутые", hp: 88, speed: 54, reward: 19, category: "air", canRaid: true },
  machine:        { name: "Обращённые станки", hp: 135, speed: 34, reward: 21, category: "machine", canRaid: true },
  iron_jug:       { name: "Оболочки Директивы", hp: 180, speed: 26, reward: 28, category: "machine" },
  miniBossGround: { name: "Воевода Красной Чешуи", hp: 220, speed: 28, reward: 36, category: "ground", boss: true },
  bossGround:     { name: "Князь Глубин", hp: 440, speed: 25, reward: 65, category: "ground", boss: true },
  bossAir:        { name: "Трёхглавый Страж Неба", hp: 360, speed: 34, reward: 72, category: "air", boss: true },
  bossMachine:    { name: "Станок Пустого Имени", hp: 560, speed: 22, reward: 88, category: "machine", boss: true },
  dread_lord:     { name: "Серый Проводник", hp: 700, speed: 20, reward: 100, category: "ground", boss: true },
  elder_dragon:   { name: "Пробуждённый Мировой Змей", hp: 1200, speed: 18, reward: 150, category: "air", boss: true },
};
const paths = [
  [[79, 64], [79, 235], [195, 235], [195, 337], [51, 337], [51, 523], [195, 523], [195, 454]],
  [[311, 64], [311, 235], [195, 235], [195, 337], [339, 337], [339, 523], [195, 523], [195, 454]],
];
const structureBlockers = [
  { x: 42, y: 58, w: 74, h: 62 },
  { x: 274, y: 58, w: 74, h: 62 },
  { x: 150, y: 382, w: 90, h: 92 },
];
// Buildable cells that should stay empty (no resource trees/stones placed)
const noResourceCells = new Set(["2,16","9,16"]);

const manualBlockedCells = new Set([
  // road-edge row 22: remove resource cells right on road boundary
  "2,22","3,22","4,22","7,22","8,22","9,22",
  // top rows near spawn gates — no resources
  "1,2",
]);
const manualAllowedCells = new Set([
  // left map edge column — allow resources rows 5–24 (skip rows 2–4 near spawn gate)
  "0,5","0,6","0,7","0,8","0,9","0,10","0,11","0,12",
  "0,13","0,14","0,15","0,16","0,17","0,18","0,19","0,20","0,21","0,22","0,23","0,24",
  // right map edge column — allow resources rows 5–24 (skip rows 2–4 near spawn gate)
  "11,4","11,5","11,6","11,7","11,8","11,9","11,10","11,11","11,12",
  "11,13","11,14","11,15","11,16","11,17","11,18","11,19","11,20","11,21","11,22","11,23","11,24",
  // castle-adjacent cells unblocked
  "5,17","6,17",
]);

const battlefield = document.querySelector(".battlefield");
const gridLayer = document.getElementById("gridLayer");
const towerLayer = document.getElementById("towerLayer");
const dyingLayer = document.getElementById("dyingLayer");
const enemyLayer = document.getElementById("enemyLayer");
const goldEl = document.getElementById("gold");
const woodEl = document.getElementById("wood");
const stoneEl = document.getElementById("stone");
const waveEl = document.getElementById("wave");
const waveAnnounceEl = document.getElementById("waveAnnounce");
const panelTitle = document.getElementById("panelTitle");
const panelText = document.getElementById("panelText");
const towerChoices = document.getElementById("towerChoices");
const towerActions = document.getElementById("towerActions");
const upgradeButton = document.getElementById("upgradeButton");
const sellButton = document.getElementById("sellButton");
const heroChargeEl = document.getElementById("heroCharge");
const heroDrawer = document.getElementById("heroDrawer");
const heroFloat = document.getElementById("heroFloat");
const buildInfoEl = document.getElementById("buildInfo");
const sheet = document.getElementById("sheet");
const sheetTitle = document.getElementById("sheetTitle");
const sheetSubtitle = document.getElementById("sheetSubtitle");
const sheetBody = document.getElementById("sheetBody");
const castleSprite = document.getElementById("castleSprite");
const spawnCaves = [
  document.getElementById("spawnCave0"),
  document.getElementById("spawnCave1"),
];

towerChoices.addEventListener("click", (event) => {
  const button = event.target.closest("[data-type]");
  if (button) setBuildType(button.dataset.type);
});

document.getElementById("startWave").addEventListener("click", startWave);
document.getElementById("speedButton").addEventListener("click", toggleSpeed);
document.getElementById("speedResetButton").addEventListener("click", resetSpeed);
document.getElementById("heroSkill").addEventListener("click", heroShield);
document.getElementById("baseHotspot").addEventListener("click", showHeroSheet);
document.getElementById("closeSheet").addEventListener("click", closeSheet);
upgradeButton.addEventListener("click", upgradeTower);
sellButton.addEventListener("click", sellTower);
window.addEventListener("resize", renderGrid);

function closeHeroDrawer() {
  if (!heroDrawer.classList.contains("open")) return;
  heroDrawer.classList.remove("open");
  heroFloat.classList.add("hidden");
  delete heroDrawer.dataset.activeInfo;
  heroDrawer.querySelectorAll(".hero-drawer-tab").forEach(t => t.classList.remove("active"));
  towerChoices.classList.remove("hidden");
}

function showTowerChoices() {
  if (heroDrawer.classList.contains("open")) {
    closeHeroDrawer();
    return;
  }
  towerChoices.classList.remove("hidden");
}

document.addEventListener("click", (e) => {
  // Close hero float when clicking outside tab buttons
  if (!heroFloat.classList.contains("hidden") && !e.target.closest(".hero-drawer-tab")) {
    heroFloat.classList.add("hidden");
    delete heroDrawer.dataset.activeInfo;
    heroDrawer.querySelectorAll(".hero-drawer-tab").forEach(t => t.classList.remove("active"));
  }

  // Close hero drawer when clicking outside it
  if (heroDrawer.classList.contains("open")) {
    if (!heroDrawer.contains(e.target) && !document.getElementById("heroSkill").contains(e.target)) {
      closeHeroDrawer();
    }
  }

  // Close sheet when clicking on backdrop (outside .sheet-card)
  if (!sheet.classList.contains("hidden")) {
    if (!e.target.closest(".sheet-card")) {
      closeSheet();
    }
  }

  // Deselect tower when clicking anywhere outside towerActions, buildInfo, or heroSkill
  if (!towerActions.classList.contains("hidden")) {
    if (!e.target.closest("#towerActions") && !e.target.closest("#buildInfo") && !e.target.closest("#heroSkill")) {
      returnToBuildChoices();
    }
  }
});

function setBuildType(type) {
  returnToBuildChoices();
  state.buildType = type;
  setBuildModeClass();
  document.querySelectorAll("[data-type]").forEach((button) => {
    button.classList.toggle("active", button.dataset.type === state.buildType);
  });
  towerActions.classList.add("hidden");
  showTowerChoices();

  if (!state.buildType) {
    showPanelNotice("Build Mode", "Choose a building and a cell.");
    hideBuildInfo();
    renderGrid();
    return;
  }

  const def = towerDefs[state.buildType];
  showPanelNotice(def.name, getBuildHint(state.buildType));
  showBuildInfo(def.name, def.cost);
  renderGrid();
}

function selectTower(id) {
  const tower = state.towers[id];
  if (!tower) return;
  hideBuildInfo();
  // Close hero drawer immediately (no animation delay needed here)
  if (heroDrawer.classList.contains("open")) {
    heroDrawer.classList.remove("open");
  }
  state.selectedTowerId = id;
  state.buildType = null;
  setBuildModeClass();
  document.querySelectorAll("[data-type]").forEach((button) => button.classList.remove("active"));
  renderGrid();

  const def = towerDefs[tower.type];
  const combat = getTowerCombatStats(tower);
  const branch = tower.specialization ? watchtowerSpecializations[tower.specialization] : null;
  const subtype = branch && tower.subtype ? branch.subtypes[tower.subtype] : null;
  panelTitle.textContent = branch
    ? `${subtype ? subtype.name : branch.name} lv.${tower.level}`
    : `${def.name} lv.${tower.level}`;
  panelText.textContent = def.attacks
    ? getTowerPanelText(tower, combat)
    : getEconomyBuildingText(tower);
  towerChoices.classList.add("hidden");
  towerActions.classList.remove("hidden");

  if (tower.type === "fire" && !tower.specialization) {
    towerActions.className = "tower-actions";
    const icons = { infantry: "🗡️", air: "🏹", siege: "💣" };
    towerActions.innerHTML = `<div class="tower-spec-row">${Object.entries(watchtowerSpecializations).map(([specId, spec]) =>
      `<button class="tower-action-spec" type="button" data-spec-id="${specId}" title="${spec.name}"><span style="font-size:18px">${icons[specId]}</span><span style="font-size:8px;display:block;color:var(--muted)">${spec.name.split(" ")[0]}</span></button>`
    ).join("")}</div><button class="tower-action-sell-wide" type="button" id="sellButtonDyn">Развязать</button>`;
    towerActions.querySelector("#sellButtonDyn").addEventListener("click", sellTower);
    towerActions.querySelectorAll("[data-spec-id]").forEach(btn => {
      btn.addEventListener("click", () => applyWatchtowerSpecialization(id, btn.dataset.specId));
    });
  } else {
    towerActions.className = "tower-actions";
    towerActions.innerHTML = `<button id="upgradeButtonDyn" type="button" class="upgrade-dyn">${getUpgradeButtonText(tower)}</button><button id="sellButtonDyn" type="button" class="sell-dyn">Развязать</button>`;
    towerActions.querySelector("#upgradeButtonDyn").addEventListener("click", upgradeTower);
    towerActions.querySelector("#sellButtonDyn").addEventListener("click", sellTower);
  }
}

let buildInfoTimer = null;
function showBuildInfo(name, gold, rc = {}, onExpire = null) {
  buildInfoEl.innerHTML =
    (name ? `<span class="build-info-name">${name}</span>` : "")
    + `<span class="build-info-icon atlas-res-gold" aria-hidden="true"></span><span class="build-info-cost">${gold}</span>`
    + (rc.wood  ? `<span class="build-info-icon atlas-res-wood" aria-hidden="true"></span><span class="build-info-cost">${rc.wood}</span>`  : "")
    + (rc.stone ? `<span class="build-info-icon atlas-res-stone" aria-hidden="true"></span><span class="build-info-cost">${rc.stone}</span>` : "");
  buildInfoEl.classList.remove("hidden");
  clearTimeout(buildInfoTimer);
  buildInfoTimer = setTimeout(() => {
    hideBuildInfo();
    if (onExpire) onExpire();
  }, 2500);
}

function hideBuildInfo() {
  clearTimeout(buildInfoTimer);
  buildInfoEl.classList.add("hidden");
}

function returnToBuildChoices() {
  state.selectedTowerId = null;
  towerActions.classList.add("hidden");
  hideBuildInfo();
  showTowerChoices();
}

function resetBuildPanel() {
  state.selectedTowerId = null;
  state.buildType = null;
  setBuildModeClass();
  document.querySelectorAll("[data-type]").forEach((button) => button.classList.remove("active"));
  towerActions.classList.add("hidden");
  showTowerChoices();
  showPanelNotice("Build Mode", "Choose a building and a cell.");
  renderGrid();
}

function buildTowerAt(type, col, row) {
  const def = towerDefs[type];
  const resourceCost = getBuildResourceCost(type);
  if (state.gold < def.cost || !canAffordResources(resourceCost)) {
    showBuildInfo("", def.cost, resourceCost);
    return;
  }
  const position = gridToPercent(col, row);
  const reason = getBuildBlockReason(col, row, type);
  if (reason) {
    showPanelNotice("Cannot build here", reason);
    return;
  }

  const id = state.nextTowerId++;
  const tower = {
    id,
    type,
    level: 1,
    cooldown: 0,
    col,
    row,
    x: position.x,
    y: position.y,
  };
  if (isEconomyBuilding(type)) {
    tower.hp = ECONOMY_BUILDING_HP;
    tower.maxHp = ECONOMY_BUILDING_HP;
  } else if (type === "fire") {
    tower.hp = WATCHTOWER_HP;
    tower.maxHp = WATCHTOWER_HP;
  }
  if (["thorn", "void", "sun"].includes(type)) {
    const existing = getTowerAtCell(col, row);
    if (existing) delete state.towers[existing.id];
  }
  state.towers[id] = tower;
  state.gold -= def.cost;
  spendResources(resourceCost);
  claimCellForBuilding(col, row);
  if (type === "fire") { const k = cellKey(col, row); state.resourceCells.delete(k); state.growingCells.delete(k); }
  if (isEconomyBuilding(type) || ["thorn", "void", "sun"].includes(type)) revealCellsAround(col, row);
  renderGrid();
  renderTowers();
  state.selectedTowerId = null;
  towerActions.classList.add("hidden");
  showTowerChoices();
  showPanelNotice(`${def.name} placed`, "Choose the next cell.");
  updateHud();
}

function upgradeTower() {
  const tower = state.towers[state.selectedTowerId];
  if (!tower) return;
  if (isEconomyBuilding(tower.type) && tower.level >= MAX_ECONOMY_LEVEL) {
    showPanelNotice("Предел рабочего круга", "Свяжите ещё один Плотницкий или Каменный круг.");
    return;
  }
  if (tower.level >= MAX_TOWER_LEVEL) {
    showPanelNotice("Предел формы", "Все доступные слои уже связаны.");
    return;
  }
  if (tower.type === "fire" && tower.level === 1 && !tower.specialization) {
    showWatchtowerUpgradeSheet(tower.id);
    return;
  }
  if (tower.type === "fire" && tower.specialization && tower.level === 5 && !tower.subtype) {
    showWatchtowerSubtypeSheet(tower.id);
    return;
  }
  const econBlock = checkEconReq(tower);
  if (econBlock) {
    showPanelNotice("Buildings required", econBlock);
    return;
  }
  const cost = upgradeCost(tower);
  const resourceCost = getUpgradeResourceCost(tower);
  if (state.gold < cost || !canAffordResources(resourceCost)) {
    showBuildInfo("", cost, resourceCost);
    return;
  }
  state.gold -= cost;
  spendResources(resourceCost);
  tower.level += 1;
  renderTowers();
  selectTower(tower.id);
  updateHud();
}

function showWatchtowerUpgradeSheet(towerId) {
  const tower = state.towers[towerId];
  if (!tower || tower.type !== "fire") return;

  sheetTitle.textContent = "Royal Watch Blueprints";
  sheetSubtitle.textContent = "Choose an engineering specialization for the tower.";
  const specGoldLabel = upgradeCost(tower);
  const specResLabel = formatResourceCost(getUpgradeResourceCost(tower));
  sheetBody.innerHTML = `<div class="upgrade-grid">${Object.entries(watchtowerSpecializations).map(([id, spec]) => `
    <article class="upgrade-card">
      <div class="upgrade-mark">${spec.mark}</div>
      <strong>${spec.name}</strong>
      <button class="info-btn" type="button" data-info-card>?</button>
      <button type="button" data-specialization="${id}">Buy</button>
      <div class="card-detail hidden">
        <span class="price-tag">⚙ ${specGoldLabel} gld${specResLabel ? ' · '+specResLabel : ''}</span>
        <br/>${spec.note}
      </div>
    </article>
  `).join("")}</div>`;

  sheetBody.querySelectorAll("[data-specialization]").forEach((button) => {
    button.addEventListener("click", () => applyWatchtowerSpecialization(towerId, button.dataset.specialization));
  });
  sheetBody.querySelectorAll("[data-info-card]").forEach(btn => {
    btn.addEventListener("click", () => {
      const detail = btn.closest("article").querySelector(".card-detail");
      const open = detail.classList.toggle("hidden");
      btn.classList.toggle("open", !open);
    });
  });
  openSheet();
}

function applyWatchtowerSpecialization(towerId, specialization) {
  const tower = state.towers[towerId];
  if (!tower || tower.type !== "fire" || tower.specialization || !watchtowerSpecializations[specialization]) return;
  const cost = upgradeCost(tower);
  const resourceCost = getUpgradeResourceCost(tower);
  if (state.gold < cost || !canAffordResources(resourceCost)) { showBuildInfo("", cost, resourceCost); return; }

  state.gold -= cost;
  spendResources(resourceCost);
  tower.specialization = specialization;
  tower.level = 2;
  tower.shots = 0;
  tower.hitTargets = new Set();
  closeSheet();
  renderTowers();
  selectTower(tower.id);
  updateHud();
}

function showWatchtowerSubtypeSheet(towerId) {
  const tower = state.towers[towerId];
  const branch = tower && watchtowerSpecializations[tower.specialization];
  if (!tower || !branch) return;

  sheetTitle.textContent = "Workshop Fork";
  sheetSubtitle.textContent = `${branch.name}: choose a subtype after level 5.`;
  const subtypeGoldLabel = upgradeCost(tower);
  const subtypeResLabel = formatResourceCost(getUpgradeResourceCost(tower));
  sheetBody.innerHTML = `<div class="upgrade-grid">${Object.entries(branch.subtypes).map(([id, subtype]) => `
    <article class="upgrade-card">
      <div class="upgrade-mark">${subtype.mark}</div>
      <strong>${subtype.name}</strong>
      <button class="info-btn" type="button" data-info-card>?</button>
      <button type="button" data-subtype="${id}">Buy</button>
      <div class="card-detail hidden">
        <span class="price-tag">⚙ ${subtypeGoldLabel} gld${subtypeResLabel ? ' · '+subtypeResLabel : ''}</span>
        <br/>${subtype.note}
      </div>
    </article>
  `).join("")}</div>`;

  sheetBody.querySelectorAll("[data-subtype]").forEach((button) => {
    button.addEventListener("click", () => applyWatchtowerSubtype(towerId, button.dataset.subtype));
  });
  sheetBody.querySelectorAll("[data-info-card]").forEach(btn => {
    btn.addEventListener("click", () => {
      const detail = btn.closest("article").querySelector(".card-detail");
      const open = detail.classList.toggle("hidden");
      btn.classList.toggle("open", !open);
    });
  });
  openSheet();
}

function applyWatchtowerSubtype(towerId, subtype) {
  const tower = state.towers[towerId];
  const branch = tower && watchtowerSpecializations[tower.specialization];
  if (!tower || !branch || tower.subtype || !branch.subtypes[subtype]) return;
  const cost = upgradeCost(tower);
  const resourceCost = getUpgradeResourceCost(tower);
  if (state.gold < cost || !canAffordResources(resourceCost)) { showBuildInfo("", cost, resourceCost); return; }

  state.gold -= cost;
  spendResources(resourceCost);
  tower.subtype = subtype;
  tower.level = 6;
  closeSheet();
  renderTowers();
  selectTower(tower.id);
  updateHud();
}

function getTowerSellValue(tower) {
  const upgCosts = isEconomyBuilding(tower.type)
    ? [0, 0, 150, 240, 360]
    : [0, 0, 200, 310, 450, 640, 860, 1120, 1420, 1760, 2140, 2560, 3040];
  let invested = towerDefs[tower.type].cost;
  for (let lvl = 2; lvl <= tower.level; lvl++) invested += upgCosts[lvl] || 0;
  return Math.floor(invested * 0.5);
}

function playTowerDestroyAnim(tower) {
  const node = towerLayer.querySelector(`[data-tower-id="${tower.id}"]`);
  if (!node) return;
  const ghost = node.cloneNode(true);
  ghost.classList.add("is-destroying");
  ghost.style.pointerEvents = "none";
  dyingLayer.appendChild(ghost);
  setTimeout(() => ghost.remove(), 1300);
}

function sellTower() {
  const tower = state.towers[state.selectedTowerId];
  if (!tower) return;
  playTowerDestroyAnim(tower);
  scheduleRegrowth(tower);
  state.gold += getTowerSellValue(tower);
  delete state.towers[state.selectedTowerId];
  renderGrid();
  renderTowers();
  resetBuildPanel();
  updateHud();
}

function seedDefaultTowers() {
  if (state.defaultTowersSeeded) return;

  for (const cell of defaultTowerCells) {
    if (getTowerAtCell(cell.col, cell.row) || getTerrainBlockReason(cell.col, cell.row)) continue;
    const position = gridToPercent(cell.col, cell.row);
    const id = state.nextTowerId++;
    claimCellForBuilding(cell.col, cell.row);
    const tower = {
      id,
      type: cell.type,
      level: 1,
      cooldown: 0,
      col: cell.col,
      row: cell.row,
      x: position.x,
      y: position.y,
    };
    if (isEconomyBuilding(cell.type)) {
      tower.hp = ECONOMY_BUILDING_HP;
      tower.maxHp = ECONOMY_BUILDING_HP;
    } else if (cell.type === "fire") {
      tower.hp = WATCHTOWER_HP;
      tower.maxHp = WATCHTOWER_HP;
    }
    state.towers[id] = tower;
  }

  state.defaultTowersSeeded = true;
}

function clearTreeAt(col, row) {
  showPanelNotice("Материальная клетка", "Плотницкий круг ставится на лес, Каменный круг — на камень. Рабочий круг открывает соседние клетки.");
}

function startWave() {
  if (state.running || state.gameOver) return;
  state.running = true;
  state.spawnTimer = 0;
  state.spawned = 0;
  battlefield.classList.add("wave-on");
  showPanelNotice("Дорога открыта", "Сверьте класс носителей с ответом ваших форм.");
  // trigger spawn cave animation
  spawnCaves.forEach(cave => {
    cave.classList.remove("is-spawning");
    void cave.offsetWidth; // force reflow to restart animation
    cave.classList.add("is-spawning");
    setTimeout(() => cave.classList.remove("is-spawning"), 900);
  });
}

function toggleSpeed() {
  state.speed = state.speed >= 3 ? 1 : state.speed + 1;
  updateSpeedButtons();
}

function resetSpeed() {
  state.speed = 1;
  updateSpeedButtons();
}

function updateSpeedButtons() {
  document.getElementById("speedButton").textContent = `x${state.speed}`;
}

function toggleHeroDrawer() {
  // If tower actions panel is open, close it cleanly before toggling drawer
  if (!towerActions.classList.contains("hidden")) {
    towerActions.classList.add("hidden");
    hideBuildInfo();
    state.selectedTowerId = null;
    setBuildModeClass();
  }
  const isOpen = heroDrawer.classList.toggle("open");
  if (!isOpen) {
    setTimeout(() => {
      if (!heroDrawer.classList.contains("open")) towerChoices.classList.remove("hidden");
    }, 220);
    return;
  }
  towerChoices.classList.add("hidden");
  const locked = !canBuyHero();
  heroDrawer.innerHTML = Object.entries(heroDefs).map(([id, hero]) => {
    const selected = state.heroId === id;
    const disabled = locked || (state.heroId && !selected) || state.gold < hero.cost;
    const costLabel = selected ? "✓" : locked ? "🔒" : `${hero.cost} gld`;
    return `<div class="hero-drawer-wrap">
      <button class="hero-drawer-tab" type="button" data-info="${id}">▲</button>
      <button class="hero-drawer-card${selected ? " selected" : ""}${locked ? " locked" : ""}" type="button" data-hero="${id}" ${disabled ? "disabled" : ""}>
        <span class="hero-drawer-mark">${hero.mark}</span>
        <span class="hero-drawer-name">${hero.name}</span>
        <span class="hero-drawer-cost">${costLabel}</span>
      </button>
    </div>`;
  }).join("");
  heroDrawer.querySelectorAll("[data-hero]").forEach(btn => {
    btn.addEventListener("click", () => { buyHero(btn.dataset.hero); closeHeroDrawer(); });
  });
  heroDrawer.querySelectorAll("[data-info]").forEach(btn => {
    btn.addEventListener("click", (e) => {
      e.stopPropagation();
      const id = btn.dataset.info;
      const hero = heroDefs[id];
      const willOpen = heroFloat.classList.contains("hidden") || heroDrawer.dataset.activeInfo !== id;
      heroDrawer.querySelectorAll(".hero-drawer-tab").forEach(t => t.classList.remove("active"));
      if (willOpen) {
        heroFloat.innerHTML = `<strong>${hero.name}</strong><span class="hero-tip-race">${hero.race} · ${hero.cost} gld</span><ul>${hero.skills.map(s => `<li>${s}</li>`).join("")}</ul>`;
        heroFloat.classList.remove("hidden");
        heroDrawer.dataset.activeInfo = id;
        btn.classList.add("active");
      } else {
        heroFloat.classList.add("hidden");
        delete heroDrawer.dataset.activeInfo;
      }
    });
  });
}

function heroShield() {
  if (!state.heroId) {
    toggleHeroDrawer();
    return;
  }
  if (!state.running) {
    showPanelNotice("Хранитель ждёт", "Откройте волну, затем призовите хранителя.");
    return;
  }
  if (state.heroReturning) {
    showPanelNotice(heroDefs[state.heroId].name, "Хранитель возвращается к Последнему узлу.");
    return;
  }
  if (state.heroActive) {
    showPanelNotice(heroDefs[state.heroId].name, "Хранитель уже проявлен до конца волны.");
    return;
  }
  const needed = getHeroSummonKills();
  if (state.heroChargeKills < needed) {
    showPanelNotice("Not enough glory", `Tower kills needed: ${state.heroChargeKills}/${needed}.`);
    return;
  }

  summonHero();
}

function summonHero() {
  const hero = heroDefs[state.heroId];
  state.heroActive = true;
  state.heroReturning = false;
  state.heroChargeKills = 0;
  state.heroPulse = 0;
  setHeroPosition(HERO_FIELD_POSITION.x, HERO_FIELD_POSITION.y);
  battlefield.classList.add("hero-active", `hero-${state.heroId}`);
  if (state.heroId === "paladin") {
    state.baseShield = Math.min(5, state.baseShield + 3);
    addEffect("shield-field", 50, 58);
    showPanelNotice(hero.name, "Summoned until end of wave. Base shield gained 3 charges.");
  } else if (state.heroId === "mage") {
    state.baseShield = Math.min(5, state.baseShield + 1);
    state.slowUntil = performance.now() + 2800;
    addEffect("slow-field", 50, 58);
    showPanelNotice(hero.name, "Summoned until end of wave. Dome slows enemies and grants 1 shield charge.");
  } else if (state.heroId === "hunter") {
    state.baseShield = Math.min(5, state.baseShield + 1);
    strikeEnemiesNearBase(55);
    addEffect("thorn-field", 50, 58);
    showPanelNotice(hero.name, "Summoned until end of wave. Thorns wound enemies near the base.");
  }
  updateHud();
}

function beginHeroReturn() {
  if (!state.heroActive) return;
  state.heroActive = false;
  state.heroReturning = true;
  state.heroPulse = 0;
  showPanelNotice(heroDefs[state.heroId].name, "Волна закрыта. Хранитель возвращается к узлу.");
}

function dismissHero() {
  state.heroActive = false;
  state.heroReturning = false;
  state.heroPulse = 0;
  setHeroPosition(HERO_BASE_POSITION.x, HERO_BASE_POSITION.y);
  battlefield.classList.remove("hero-active", "hero-returning", "hero-paladin", "hero-mage", "hero-hunter");
}

function setHeroPosition(x, y) {
  state.heroX = x;
  state.heroY = y;
  battlefield.style.setProperty("--hero-x", `${x}%`);
  battlefield.style.setProperty("--hero-y", `${y}%`);
}

function updateActiveHero(dt, time) {
  if (!state.heroActive && !state.heroReturning) return;
  updateHeroCombat(dt);
  if (state.heroReturning) {
    updateHeroReturn(dt);
    return;
  }
  state.heroPulse -= dt;
  if (state.heroId === "mage") {
    state.slowUntil = Math.max(state.slowUntil, time + 350);
  }
  if (state.heroPulse > 0) return;
  if (state.heroId === "paladin") {
    state.baseShield = Math.min(5, state.baseShield + 1);
    state.heroPulse = 5;
  } else if (state.heroId === "hunter") {
    strikeEnemiesNearBase(18);
    state.heroPulse = 1.1;
  } else {
    state.heroPulse = 1;
  }
}

function updateHeroReturn(dt) {
  battlefield.classList.add("hero-active", "hero-returning", `hero-${state.heroId}`);
  const rect = cachedRect;
  const hx = rect.width * state.heroX / 100;
  const hy = rect.height * state.heroY / 100;
  const target = state.enemies.find((enemy) =>
    isEnemyActive(enemy) && Math.hypot(enemy.x - hx, enemy.y - hy) <= HERO_ATTACK_RANGE
  );
  if (target) return;

  const dx = HERO_BASE_POSITION.x - state.heroX;
  const dy = HERO_BASE_POSITION.y - state.heroY;
  const dist = Math.hypot(dx, dy);
  if (dist < 0.18) {
    dismissHero();
    return;
  }
  const step = Math.min(dist, HERO_RETURN_SPEED * dt);
  setHeroPosition(state.heroX + dx / dist * step, state.heroY + dy / dist * step);
}

function updateHeroCombat(dt) {
  state.heroAttackCooldown = Math.max(0, state.heroAttackCooldown - dt);
  if (state.heroAttackCooldown > 0) return;
  const rect = cachedRect;
  const hx = rect.width * state.heroX / 100;
  const hy = rect.height * state.heroY / 100;
  const heroRangeSq = HERO_ATTACK_RANGE * HERO_ATTACK_RANGE;
  let target = null;
  let targetDistSq = Infinity;
  for (const enemy of state.enemies) {
    if (!isEnemyActive(enemy)) continue;
    const dx = enemy.x - hx, dy = enemy.y - hy;
    const dSq = dx * dx + dy * dy;
    if (dSq <= heroRangeSq && dSq < targetDistSq) { target = enemy; targetDistSq = dSq; }
  }
  if (!target) return;
  target.hit = 0.12;
  damageEnemy(target, HERO_ATTACK_DAMAGE, false);
  state.heroAttackCooldown = HERO_ATTACK_RATE;
  state.projectiles.push(makeProjectile(hx, hy, target.x, target.y, 0.16, "#b8ff8d"));
}

function strikeEnemiesNearBase(damage) {
  const rect = cachedRect;
  const cx = rect.width * 0.5;
  const cy = rect.height * 0.58;
  [...state.enemies].forEach((enemy) => {
    if (isEnemyActive(enemy) && Math.hypot(enemy.x - cx, enemy.y - cy) < 105) {
      enemy.hit = 0.12;
      damageEnemy(enemy, damage, false);
    }
  });
}

function getHeroSummonKills() {
  return 18 + Math.floor(state.wave * 0.6);
}

function getSpawnInterval(wave, isBoss) {
  if (isBoss) return 1.8;
  if (wave <= 2) return 1.4;
  if (wave <= 4) return 1.2;
  if (wave <= 6) return 1.0;
  if (wave <= 10) return 0.95;
  if (wave <= 15) return 0.9;
  if (wave <= 20) return 0.85;
  return Math.max(0.7, 0.85 - (wave - 20) * 0.004);
}

function update(time) {
  const dt = Math.min((time - state.lastTime) / 1000 || 0, 0.04) * state.speed;
  state.lastTime = time;
  cachedRect = battlefield.getBoundingClientRect();

  if (!state.gameOver) {
    if (state.running) spawnWave(dt);
    updateActiveHero(dt, time);
    updateEnemies(dt, time);
    updateTowers(dt);
    updateProjectiles(dt);
  }
  renderEnemies();
  renderProjectiles();
  updateHud();

  requestAnimationFrame(update);
}

function spawnWave(dt) {
  state.spawnTimer -= dt;
  const plan = getWavePlan(state.wave);
  const total = plan.total;
  if (state.spawned < total && state.spawnTimer <= 0) {
    const simultaneous = state.wave >= 18 && getActivePathCount() === 2;
    const kind0 = plan.kinds[state.spawned % plan.kinds.length];
    const isBoss0 = Boolean(enemyDefs[kind0] && enemyDefs[kind0].boss);

    if (simultaneous && !isBoss0 && state.spawned + 1 < total) {
      const kind1 = plan.kinds[(state.spawned + 1) % plan.kinds.length];
      const isBoss1 = Boolean(enemyDefs[kind1] && enemyDefs[kind1].boss);
      if (!isBoss1) {
        state.enemies.push(makeEnemyOnPath(kind0, 0));
        state.enemies.push(makeEnemyOnPath(kind1, 1));
        state.spawned += 2;
        state.spawnTimer = getSpawnInterval(state.wave, false);
      } else {
        state.enemies.push(makeEnemyOnPath(kind0, state.spawned % 2));
        state.spawned += 1;
        state.spawnTimer = getSpawnInterval(state.wave, false);
      }
    } else {
      const pathIndex = getActivePathCount() > 1 ? state.spawned % 2 : 0;
      state.enemies.push(makeEnemyOnPath(kind0, pathIndex));
      state.spawned += 1;
      state.spawnTimer = getSpawnInterval(state.wave, isBoss0);
    }
  }
  if (state.spawned >= total && state.enemies.length === 0) {
    state.running = false;
    battlefield.classList.remove("wave-on");
    beginHeroReturn();
    const income = collectWaveResources();
    state.wave += 1;
    showWaveAnnounce(state.wave);
    processRegrowth();
    state.gold += getWaveGoldReward();

    const resourceLine = [
      income.wood > 0 || income.stone > 0 ? `Возвращено: ${income.wood} Древа · ${income.stone} Камня.` : "",
      income.overflow > 0 ? `Излишек → +${income.overflow} Злата.` : "",
    ].filter(Boolean).join(" · ");

    if (canBuyHero() && !state.heroId) {
      showPanelNotice("Хранители доступны", `Нажмите на Последний узел и выберите одного хранителя. ${resourceLine}`);
    } else if (state.wave === 9) {
      showPanelNotice("Князь Глубин приближается", `Следующая волна откроет вторую Дорогу. Укрепите оба ответа. ${resourceLine}`);
    } else if (state.wave === 10) {
      showPanelNotice("Волна закрыта", `Теперь носители приходят по двум Дорогам. ${resourceLine}`);
    } else if (state.wave === 17) {
      showPanelNotice("Двойной прилив близко", `С 18-й волны обе Дороги открываются одновременно. ${resourceLine}`);
    } else if (state.wave === 18) {
      showPanelNotice("Двойной прилив", `Обе Дороги открыты одновременно. ${resourceLine}`);
    } else {
      showPanelNotice("Волна закрыта", resourceLine || "Подготовьте следующий ответ.");
    }
  }
}

function getWaveGoldReward() {
  const bonus = state.heroId === "paladin" ? 1.12 : 1;
  const prep = (state.wave === 10 || state.wave === 18) ? 30 : 0;
  return Math.round((22 + state.wave * 3 + prep) * bonus);
}

function getWavePlan(wave) {
  const scripted = {
    1:  { label: "Первое раскрытие", total: 8, kinds: ["fast", "fast", "warrior", "fast"] },
    2:  { label: "Тяжёлый след", total: 10, kinds: ["fast", "fast", "brute", "fast"] },
    3:  { label: "Крюки Имён", total: 10, kinds: ["raider", "fast", "fast", "raider", "fast"] },
    4:  { label: "Цена ответа", total: 14, kinds: ["fast", "brute", "fast", "fast", "brute"] },
    5:  { label: "Воевода Нижней Чешуи", total: 5, kinds: ["fast", "raider", "miniBossGround", "brute", "fast"] },
    6:  { label: "Ложный небесный путь", total: 13, kinds: ["fast", "air", "fast", "brute", "air", "raider"] },
    7:  { label: "Несогласные формы", total: 16, kinds: ["fast", "brute", "raider", "air", "brute"] },
    8:  { label: "Непомянутые в небе", total: 18, kinds: ["fast", "air", "wraith", "raider", "brute", "air"] },
    9:  { label: "Испытание первой Дороги", total: 20, kinds: ["fast", "brute", "raider", "fast", "air", "wraith"] },
    10: { label: "Князь Глубин", total: 8, kinds: ["fast", "brute", "bossGround", "raider", "fast", "brute", "raider", "fast"] },
    11: { label: "Обращённые станки", total: 22, kinds: ["fast", "machine", "brute", "raider", "air", "machine"] },
    12: { label: "Чужая сборка", total: 24, kinds: ["machine", "fast", "brute", "raider", "machine", "air"] },
    13: { label: "Серая директива", total: 26, kinds: ["fast", "machine", "wraith", "brute", "raider", "air"] },
    14: { label: "Одна версия для всех", total: 28, kinds: ["machine", "brute", "air", "raider", "fast", "wraith", "machine"] },
    15: { label: "Трёхглавый Страж Неба", total: 7, kinds: ["wraith", "air", "bossAir", "wraith", "machine", "air", "wraith"] },
    16: { label: "Рейд исправителей", total: 26, kinds: ["fast", "brute", "machine", "raider", "air", "wraith"] },
    17: { label: "Перед двойным приливом", total: 28, kinds: ["machine", "fast", "brute", "air", "raider", "wraith", "machine"] },
    18: { label: "Две Дороги", total: 22, kinds: ["machine", "air", "brute", "wraith", "raider", "fast", "machine"] },
    19: { label: "Последний разный ответ", total: 24, kinds: ["machine", "brute", "raider", "air", "wraith", "fast", "machine"] },
    20: { label: "Станок Пустого Имени", total: 9, kinds: ["machine", "brute", "bossMachine", "raider", "machine", "air", "brute", "raider", "machine"] },
    50: { label: "Пробуждение Великого Ящера", total: 5, kinds: ["dread_lord", "bossAir", "elder_dragon", "bossMachine", "dread_lord"] },
  };
  if (scripted[wave]) return scripted[wave];

  if (wave % 12 === 0) return { label: "Станок Пустого Имени", total: 9, kinds: ["machine", "bossMachine", "air", "brute", "raider", "machine", "wraith", "fast", "raider"] };
  if (wave % 8 === 0) return { label: "Страж ложного неба", total: 9, kinds: ["air", "bossAir", "wraith", "fast", "raider", "air", "wraith", "machine", "brute"] };
  if (wave % 5 === 0) return { label: "Князь Глубин", total: 9, kinds: ["fast", "bossGround", "brute", "raider", "machine", "fast", "brute", "raider", "fast"] };

  const tier = Math.min(4, Math.floor((wave - 21) / 4));
  const mixes = [
    ["fast", "brute", "raider", "air", "wraith", "machine"],
    ["brute", "raider", "air", "machine", "fast", "wraith"],
    ["machine", "air", "wraith", "brute", "raider", "fast"],
    ["raider", "machine", "wraith", "air", "brute", "fast"],
    ["machine", "wraith", "raider", "brute", "air", "fast"],
  ];
  return {
    label: "Смешанный прилив",
    total: 14 + Math.floor((wave - 20) * 1.2),
    kinds: mixes[tier],
  };
}

function makeEnemyOnPath(kind, pathIndex) {
  const base = enemyDefs[kind] || enemyDefs.fast;
  const hp = getEnemyHp(base);
  return {
    id: state.nextEnemyId++,
    kind,
    category: base.category,
    pathIndex,
    hp,
    maxHp: hp,
    speed: base.speed,
    reward: base.reward,
    boss: Boolean(base.boss),
    segment: 0,
    progress: 0,
    attackCooldown: 0,
    raidTargetId: null,
    raidSearchTimer: 0,
    x: 0,
    y: 0,
    hit: 0,
    animState: 'spawn',
    animFrame: 0,
    animTimer: 0,
    dying: false,
    deathProcessed: false,
    deathTimer: 0,
    breaching: false,
    breachTimer: 0,
    flyIn: kind === 'elder_dragon',
    flyInTimer: 0,
  };
}

function makeEnemy(kind, index) {
  return makeEnemyOnPath(kind, index % getActivePathCount());
}

function getEnemyHp(base) {
  if (base.boss) return Math.round(base.hp * (1 + getEnemyTier() * 0.30));
  return Math.round(base.hp * getEnemyHpMultiplier(base));
}

function getEnemyTier() {
  return Math.max(0, Math.floor((state.wave - 14) / 4));
}

function killEnemy(enemy, awardKill = true) {
  if (!enemy || enemy.deathProcessed) return false;
  enemy.deathProcessed = true;
  enemy.hp = 0;
  state.gold += getEnemyReward(enemy);
  if (awardKill) addHeroChargeKill();
  const meta = ENEMY_SPRITES[enemy.kind];
  const deathEntry  = meta?.frames?.death;
  const deathFrames = meta?.dirs
    ? (deathEntry?.[getEnemyDir(enemy)] ?? 0)
    : (deathEntry ?? 0);
  if (deathFrames > 1) {
    enemy.dying = true;
    enemy.hit = 0;
    enemy.deathTimer = 0;
    enemy.animState = 'death';
    enemy.animFrame = 0;
    enemy.animTimer = 0;
  } else {
    state.enemies.splice(state.enemies.indexOf(enemy), 1);
  }
  return true;
}

function isEnemyActive(enemy) {
  return Boolean(enemy && enemy.hp > 0 && !enemy.dying && !enemy.deathProcessed);
}

function damageEnemy(enemy, damage, awardKill = true) {
  if (!isEnemyActive(enemy)) return false;
  enemy.hp -= damage;
  return enemy.hp <= 0 ? killEnemy(enemy, awardKill) : false;
}

function getEnemyHpMultiplier(base) {
  const tier = getEnemyTier();
  if (tier <= 0) return 1;
  const classGrowth = {
    ground: 0.15,
    air: 0.12,
    machine: 0.20,
  };
  return 1 + tier * (classGrowth[base.category] || 0.18);
}

function updateEnemies(dt, time) {
  const rect = cachedRect;
  const scaleX = rect.width / 390;
  const scaleY = rect.height / 610;
  const globalSlow = time < state.slowUntil ? 0.45 : 1;

  for (const enemy of [...state.enemies]) {
    const path = paths[enemy.pathIndex];
    enemy.hit = Math.max(0, enemy.hit - dt);

    // death animation plays out, then remove
    if (enemy.dying) {
      const meta       = ENEMY_SPRITES[enemy.kind];
      const deathEntry = meta?.frames?.death;
      const deathF     = meta?.dirs
        ? (deathEntry?.[getEnemyDir(enemy)] ?? 1)
        : (deathEntry ?? 1);
      const dur = deathF / (ANIM_FPS.death || 8);
      enemy.deathTimer += dt;
      updateEnemyAnim(enemy, dt);
      if (enemy.deathTimer >= dur) {
        state.enemies.splice(state.enemies.indexOf(enemy), 1);
      }
      continue;
    }

    enemy.attackCooldown = Math.max(0, enemy.attackCooldown - dt);
    updateEnemyAnim(enemy, dt);

    // elder_dragon fly-in: animate from top-center to path start during spawn
    if (enemy.flyIn) {
      enemy.flyInTimer = (enemy.flyInTimer || 0) + dt;
      const meta = ENEMY_SPRITES[enemy.kind];
      const spawnFrames = meta?.frames?.spawn || 6;
      const spawnDur = spawnFrames / (ANIM_FPS.spawn || 8);
      const t = Math.min(1, enemy.flyInTimer / spawnDur);
      const pathStart = path?.[0];
      if (pathStart) {
        const tx = pathStart[0] * scaleX;
        const ty = pathStart[1] * scaleY;
        const sx = (rect.width / 2);
        const sy = -180 * scaleY;
        enemy.x = sx + (tx - sx) * t;
        enemy.y = sy + (ty - sy) * t;
      }
      continue;
    }

    if (enemy.animState === 'spawn') {
      updateEnemyPosition(enemy, path, scaleX, scaleY);
      continue;
    }

    updateEnemyPosition(enemy, path, scaleX, scaleY);
    if (updateEnemyRaid(enemy, dt, scaleX, scaleY)) continue;
    const localSlow = enemy.slowUntil && time < enemy.slowUntil ? 0.55 : 1;
    let remaining = enemy.speed * globalSlow * localSlow * dt;
    while (remaining > 0 && enemy.segment < path.length - 1) {
      const a = path[enemy.segment];
      const b = path[enemy.segment + 1];
      const dist = Math.hypot(b[0] - a[0], b[1] - a[1]);
      const need = (1 - enemy.progress) * dist;
      if (remaining >= need) {
        remaining -= need;
        enemy.segment += 1;
        enemy.progress = 0;
      } else {
        enemy.progress += remaining / dist;
        remaining = 0;
      }
    }

    if (enemy.segment >= path.length - 1) {
      state.enemies.splice(state.enemies.indexOf(enemy), 1);
      if (state.baseShield > 0) {
        state.baseShield -= 1;
      } else {
        state.lives = Math.max(0, state.lives - 1);
      }
      if (state.lives === 0) {
        endGame();
      }
      continue;
    }

    updateEnemyPosition(enemy, path, scaleX, scaleY);
  }
}

function getEnemyDir(enemy) {
  const path = paths[enemy.pathIndex];
  const seg  = path?.[enemy.segment];
  const next = path?.[enemy.segment + 1] ?? seg;
  if (!seg || !next) return 'front';
  const dx = next[0] - seg[0];
  const dy = next[1] - seg[1];
  if (Math.abs(dx) > Math.abs(dy)) return dx > 0 ? 'sider' : 'sidel';
  return dy >= 0 ? 'front' : 'back';
}

function updateEnemyAnim(enemy, dt) {
  const meta = ENEMY_SPRITES[enemy.kind];
  if (!meta) return;

  const dir     = meta.dirs ? getEnemyDir(enemy) : null;
  const isSide  = dir === 'sider' || dir === 'sidel';
  const fps     = (enemy.animState === 'walk' && isSide)
    ? (ANIM_FPS.walkSide || 10)
    : (ANIM_FPS[enemy.animState] || 8);
  const frEntry = meta.frames[enemy.animState];
  const nFrames = meta.dirs
    ? (frEntry?.[getEnemyDir(enemy)] || 1)
    : (frEntry || 1);

  // decide state
  let targetState;
  if (enemy.dying)      targetState = 'death';
  else if (enemy.breaching) targetState = 'breach';
  else if (enemy.hit > 0)   targetState = 'attack';
  else if (enemy.animState === 'spawn') targetState = 'spawn';
  else targetState = 'walk';

  if (targetState !== enemy.animState) {
    enemy.animState = targetState;
    enemy.animFrame = 0;
    enemy.animTimer = 0;
  }

  enemy.animTimer += dt;
  if (enemy.animTimer >= 1 / fps) {
    enemy.animTimer -= 1 / fps;
    enemy.animFrame++;
    if (enemy.animFrame >= nFrames) {
      if (enemy.animState === 'spawn') {
        enemy.animState = 'walk';
        enemy.animFrame = 0;
        if (enemy.flyIn) enemy.flyIn = false;
      } else if (enemy.animState === 'death' || enemy.animState === 'breach') {
        enemy.animFrame = nFrames - 1; // hold last frame
      } else {
        enemy.animFrame = 0; // loop
      }
    }
  }
}

function updateEnemyPosition(enemy, path, scaleX, scaleY) {
  if (enemy.segment >= path.length - 1) return;
  const a = path[enemy.segment];
  const b = path[enemy.segment + 1];
  enemy.x = (a[0] + (b[0] - a[0]) * enemy.progress) * scaleX;
  enemy.y = (a[1] + (b[1] - a[1]) * enemy.progress) * scaleY;
}

function getSpriteScale(meta) {
  return meta.ds / (meta.fw || meta.ds);
}

function getSpriteDisplayWidth(meta, nFrames) {
  const gutter = meta.gutter || 0;
  const sourceWidth = (meta.fw || meta.ds) * nFrames + gutter * (nFrames - 1);
  return sourceWidth * getSpriteScale(meta);
}

function getSpriteFrameStep(meta) {
  return ((meta.fw || meta.ds) + (meta.gutter || 0)) * getSpriteScale(meta);
}

function getAtlasAnimation(animKey) {
  return GAME_ATLAS?.animations?.[animKey] || null;
}

function applyAtlasFrame(node, frameName, displaySize) {
  const entry = GAME_ATLAS?.frames?.[frameName];
  const atlasSize = GAME_ATLAS?.meta?.size;
  if (!entry || !atlasSize) return false;

  const source = entry.sourceSize;
  const offset = entry.spriteSourceSize;
  const frame = entry.frame;
  const scale = displaySize / source.w;

  node.style.backgroundImage = `url('${GAME_ATLAS_IMAGE}')`;
  node.style.width = `${source.w * scale}px`;
  node.style.height = `${source.h * scale}px`;
  node.style.backgroundSize = `${atlasSize.w * scale}px ${atlasSize.h * scale}px`;
  node.style.backgroundPosition = `${-(frame.x - offset.x) * scale}px ${-(frame.y - offset.y) * scale}px`;
  return true;
}

function updateEnemyRaid(enemy, dt, scaleX, scaleY) {
  if (!canRaidEconomyBuildings(enemy)) return false;

  enemy.raidSearchTimer -= dt;
  let target;
  if (enemy.raidSearchTimer <= 0) {
    target = getRaidTarget(enemy, scaleX, scaleY);
    enemy.raidTargetId = target ? target.id : null;
    enemy.raidSearchTimer = 0.3;
  } else {
    target = state.towers[enemy.raidTargetId];
    if (target && target.hp <= 0) { target = null; enemy.raidTargetId = null; }
  }

  if (!target) return false;

  enemy.raidTargetId = target.id;
  if (enemy.attackCooldown <= 0) {
    target.hp -= getRaiderDamage(enemy);
    enemy.attackCooldown = RAIDER_ATTACK_RATE;
    enemy.hit = 0.08;
    if (target.hp <= 0) {
      destroyRaidTarget(target);
      enemy.raidTargetId = null;
    } else {
      renderTowers();
    }
  }

  return true;
}

function canRaidEconomyBuildings(enemy) {
  return Boolean(enemyDefs[enemy.kind] && enemyDefs[enemy.kind].canRaid);
}

function getRaidTarget(enemy, scaleX, scaleY) {
  const lockedTarget = state.towers[enemy.raidTargetId];
  if (lockedTarget && lockedTarget.hp > 0 && canEnemyAttackTower(enemy, lockedTarget) &&
      getTowerDistanceToEnemy(lockedTarget, enemy, scaleX, scaleY) <= RAIDER_ATTACK_RANGE) {
    return lockedTarget;
  }

  let best = null;
  let bestDist = Infinity;
  for (const tower of Object.values(state.towers)) {
    if (!tower || tower.hp <= 0 || !canEnemyAttackTower(enemy, tower)) continue;
    const d = getTowerDistanceToEnemy(tower, enemy, scaleX, scaleY);
    if (d <= RAIDER_ATTACK_RANGE && d < bestDist) { bestDist = d; best = tower; }
  }
  return best;
}

function isValidRaidTarget(enemy, tower, scaleX, scaleY) {
  if (!tower || tower.hp <= 0 || !canEnemyAttackTower(enemy, tower)) return false;
  return getTowerDistanceToEnemy(tower, enemy, scaleX, scaleY) <= RAIDER_ATTACK_RANGE;
}

function canEnemyAttackTower(enemy, tower) {
  if (enemy.category === "air") {
    return isEconomyBuilding(tower.type) && isTowerWithinOneCellOfRoad(tower);
  }
  if (enemy.category === "machine") {
    return tower.type === "fire" && isTowerWithinOneCellOfRoad(tower);
  }
  if (enemy.category === "ground") {
    return isEconomyBuilding(tower.type) && isTowerAtRoadEdge(tower);
  }
  return false;
}

function isTowerWithinOneCellOfRoad(tower) {
  if (tower._withinRoad === undefined) {
    const mapX = tower.x * 3.9;
    const mapY = tower.y * 6.1;
    tower._withinRoad = distanceToAnyPath(mapX, mapY) <= ROAD_BLOCK_DISTANCE + ROAD_RAID_CELL_DISTANCE;
  }
  return tower._withinRoad;
}

function isTowerAtRoadEdge(tower) {
  if (tower._atRoadEdge === undefined) {
    const mapX = tower.x * 3.9;
    const mapY = tower.y * 6.1;
    tower._atRoadEdge = distanceToAnyPath(mapX, mapY) <= ROAD_EDGE_RAID_DISTANCE;
  }
  return tower._atRoadEdge;
}

function getTowerDistanceToEnemy(tower, enemy, scaleX, scaleY) {
  const tx = tower.x * 3.9;
  const ty = tower.y * 6.1;
  const ex = enemy.x / scaleX;
  const ey = enemy.y / scaleY;
  return Math.hypot(ex - tx, ey - ty);
}

function getRaiderDamage(enemy) {
  return RAIDER_DAMAGE[enemy.category] || 1;
}

function destroyRaidTarget(tower) {
  playTowerDestroyAnim(tower);
  scheduleRegrowth(tower);
  if (state.selectedTowerId === tower.id) resetBuildPanel();
  delete state.towers[tower.id];
  renderGrid();
  renderTowers();
    showPanelNotice(`${towerDefs[tower.type].name} развязан`, "Рейдеры сорвали имя постройки у Дороги.");
}

function updateTowers(dt) {
  const rect = cachedRect;
  for (const tower of Object.values(state.towers)) {
    tower.cooldown -= dt;
    if (tower.cooldown > 0) continue;

    const def = towerDefs[tower.type];
    if (!def.attacks) continue;
    const combat = getTowerCombatStats(tower);

    const tx = rect.width * tower.x / 100;
    const ty = rect.height * tower.y / 100;
    const rangeSq = combat.range * combat.range;
    let target = null;
    for (const enemy of state.enemies) {
      if (!canTargetEnemy(combat, enemy)) continue;
      const dx = enemy.x - tx, dy = enemy.y - ty;
      if (dx * dx + dy * dy < rangeSq) { target = enemy; break; }
    }
    if (!target) continue;

    tower.shots = (tower.shots || 0) + 1;
    const damage = getTowerDamageAgainst(tower, combat, target);
    target.hit = 0.08;
    const targetKilled = damageEnemy(target, damage);
    if (combat.slowOnHit) {
      target.slowUntil = performance.now() + combat.slowOnHit * 1000;
    }
    if (combat.splash) {
      const splashSq = combat.splash * combat.splash;
      for (const enemy of [...state.enemies]) {
        if (enemy === target || !isEnemyActive(enemy)) continue;
        const sdx = enemy.x - target.x, sdy = enemy.y - target.y;
        if (sdx * sdx + sdy * sdy < splashSq) {
          enemy.hit = 0.08;
          damageEnemy(enemy, damage * 0.45);
          if (combat.concussion && (enemy.category === "ground" || enemy.category === "machine")) {
            enemy.slowUntil = performance.now() + 900;
          }
        }
      }
    }
    if (combat.pierce) {
      let pierceCount = 0;
      for (const enemy of [...state.enemies]) {
        if (pierceCount >= combat.pierce) break;
        if (enemy === target || !canTargetEnemy(combat, enemy)) continue;
        const pdx = enemy.x - tx, pdy = enemy.y - ty;
        if (pdx * pdx + pdy * pdy < rangeSq) {
          enemy.hit = 0.08;
          damageEnemy(enemy, damage * 0.62);
          pierceCount++;
        }
      }
    }
    const projSprite = getTowerProjectileSprite(tower);
    state.projectiles.push(makeProjectile(tx, ty, target.x, target.y, 0.28, def.color, projSprite));
    tower.cooldown = combat.rate / tower.level;

    if (targetKilled) {
      if (combat.chainOnKill) {
        let next = null;
        for (const enemy of state.enemies) {
          if (!canTargetEnemy(combat, enemy)) continue;
          const cdx = enemy.x - tx, cdy = enemy.y - ty;
          if (cdx * cdx + cdy * cdy < rangeSq) { next = enemy; break; }
        }
        if (next) {
          next.hit = 0.08;
          damageEnemy(next, damage * 0.8);
          state.projectiles.push(makeProjectile(tx, ty, next.x, next.y, 0.18, def.color, projSprite));
        }
      }
    }
  }
}

function getEnemyReward(enemy) {
  if (state.heroId === "hunter" && enemy.category === "ground") {
    return Math.round(enemy.reward * 1.2);
  }
  return enemy.reward;
}

function addHeroChargeKill() {
  if (state.heroActive || state.heroReturning) return;
  state.heroChargeKills += 1;
}

function updateProjectiles(dt) {
  state.projectiles = state.projectiles.filter((projectile) => {
    projectile.life -= dt;
    if (projectile.life <= 0 && projectile.sprite) {
      spawnImpact(projectile.sprite, projectile.tx, projectile.ty);
    }
    return projectile.life > 0;
  });
}

function spawnImpact(sprite, x, y) {
  const node = document.createElement('div');
  node.className = `impact ${sprite}-impact`;
  node.style.left = `${x}px`;
  node.style.top = `${y}px`;
  enemyLayer.appendChild(node);
  const duration = sprite === 'ballista' ? 280 : 360;
  setTimeout(() => node.remove(), duration);
}

function getTowerProjectileSprite(tower) {
  if (tower.type === 'thorn') return 'palisade';
  if (tower.type === 'void')  return 'obelisk';
  if (tower.type === 'sun')   return 'beacon';
  if (tower.type === 'fire') {
    if (tower.specialization === 'air')      return 'ballista';
    if (tower.specialization === 'siege') {
      if (tower.subtype === 'mortar') return 'mortar';
      if (tower.subtype === 'grapeshot') return 'grapeshot';
      return 'cannon';
    }
    if (tower.specialization === 'infantry') return 'ranger';
    return 'watchtower'; // base watchtower
  }
  return null;
}

// Frame widths for animated projectile sprites (multi-frame types)
const PROJ_SPRITE_FW = {
  cannon: 20,
  obelisk: 32,
  beacon: 22,
  watchtower: 20,
  ranger: 36,
  mortar: 24,
  palisade: 28,
  grapeshot: 36,
};
const PROJ_SPRITE_FRAMES = {
  watchtower: 5,
  ranger: 5,
  cannon: 5,
  mortar: 5,
  obelisk: 5,
  beacon: 5,
  palisade: 5,
  grapeshot: 5,
};

function makeProjectile(x, y, tx, ty, life, color, sprite) {
  return {
    id: state.nextProjectileId++,
    x,
    y,
    tx,
    ty,
    life,
    maxLife: life,
    color,
    sprite: sprite || null,
  };
}

function collectWaveResources() {
  const income = { wood: 0, stone: 0, overflow: 0 };
  for (const tower of Object.values(state.towers)) {
    if (tower.type === "ice") income.wood += getWaveResourceIncome(tower);
    if (tower.type === "storm") income.stone += getWaveResourceIncome(tower);
  }
  if (state.heroId === "mage") {
    income.wood = Math.round(income.wood * 1.15);
    income.stone = Math.round(income.stone * 1.15);
  }
  state.wood += income.wood;
  state.stone += income.stone;

  const woodOver = Math.max(0, state.wood - RESOURCE_CAP);
  const stoneOver = Math.max(0, state.stone - RESOURCE_CAP);
  state.wood = Math.min(state.wood, RESOURCE_CAP);
  state.stone = Math.min(state.stone, RESOURCE_CAP);
  income.overflow = Math.floor((woodOver + stoneOver) * 0.65);
  state.gold += income.overflow;

  return income;
}

function getWaveResourceIncome(tower) {
  if (tower.type === "ice") {
    const vals = [0, 22, 42, 68, 100];
    return vals[Math.min(tower.level, MAX_ECONOMY_LEVEL)] || 100;
  }
  if (tower.type === "storm") {
    const vals = [0, 20, 38, 62, 92];
    return vals[Math.min(tower.level, MAX_ECONOMY_LEVEL)] || 92;
  }
  return 0;
}

function getEconomyBuildingText(tower) {
  const amount = getWaveResourceIncome(tower);
  const maxNote = tower.level >= MAX_ECONOMY_LEVEL ? " Max level — build more." : "";
  if (tower.type === "ice") return `Возвращает ${amount} Живого древа за волну. Открывает соседние клетки.${maxNote}`;
  if (tower.type === "storm") return `Возвращает ${amount} Камня памяти за волну. Открывает соседние клетки.${maxNote}`;
  return towerDefs[tower.type].role || "";
}

function renderTowers() {
  towerLayer.innerHTML = "";
  Object.values(state.towers).sort((a, b) => a.y - b.y).forEach((tower) => {
    const node = document.createElement("div");
    node.className = `tower ${tower.type} level-${tower.level}`;
    node.style.left = `${tower.x}%`;
    node.style.top = `${tower.y}%`;
    node.title = towerDefs[tower.type].name;
    node.dataset.towerId = tower.id;
    if (tower.specialization) node.dataset.spec = tower.specialization;
    if (tower.subtype) node.dataset.subtype = tower.subtype;
    const body = document.createElement("span");
    body.className = "tower-body";
    node.appendChild(body);
    if (hasRaidHealth(tower) && tower.maxHp) {
      const hp = Math.max(0.35, tower.hp / tower.maxHp);
      node.classList.toggle("damaged", hp < 0.55);
    }
    node.addEventListener("click", (event) => {
      event.stopPropagation();
      // Hero-special build: clicking a fire tower converts it instead of selecting
      if (["thorn", "void", "sun"].includes(state.buildType) && tower.type === "fire") {
        buildTowerAt(state.buildType, tower.col, tower.row);
        return;
      }
      selectTower(tower.id);
    });
    towerLayer.appendChild(node);
  });
}

function renderGrid() {
  const rect = battlefield.getBoundingClientRect();
  if (!rect.width || !rect.height) return;

  const cellSize = rect.width / state.grid.cols;
  const rows = Math.floor(rect.height / cellSize);
  state.grid.cellSize = cellSize;
  state.grid.rows = rows;
  ensureResourceMap();
  gridLayer.innerHTML = "";

  for (let row = 0; row < rows; row += 1) {
    for (let col = 0; col < state.grid.cols; col += 1) {
      const resource = getResourceAtCell(col, row);
      const reason = getBuildBlockReason(col, row, state.buildType);
      const button = document.createElement("button");
      button.type = "button";
      const key = cellKey(col, row);
      const growInfo = (resource === "tree" || resource === "stone") ? state.growingCells.get(key) : undefined;
      const isGrowing = !!growInfo;
      const isHeroSpecialBuild = state.buildType && ["thorn", "void", "sun"].includes(state.buildType);
      const cellTower = getTowerAtCell(col, row);
      const isPlaceable = state.buildType && !reason && (isHeroSpecialBuild ? (cellTower && cellTower.type === "fire") : !cellTower);
      button.className = `grid-cell ${resource || (reason ? reason === "Cell already occupied." ? "occupied" : "blocked" : "")}${isGrowing ? " growing" : ""}${isPlaceable ? " placeable" : ""}`;
      button.style.left = `${col * cellSize}px`;
      button.style.top = `${row * cellSize}px`;
      button.style.width = `${cellSize}px`;
      button.style.height = `${cellSize}px`;
      if (isGrowing) button.dataset.growFrame = growInfo.frame;
      if (resource === "stone") {
        // rock_c near castle (lower rows); slight mixing at border; upper quarry zone = all a
        const cProb = Math.max(0, Math.min(0.9, (row - 14) / 4));
        const rockType = state.rockBCells.has(key) ? "b"
          : spriteHash(key) < cProb ? "c" : "a";
        button.dataset.rock = rockType;
      }
      if (resource === "tree") {
        // oak fades out rows 6→17; pine dominates below; blend uses noise for organic edges
        const oakProb = Math.max(0, Math.min(1, 1 - (row - 6) / 8));
        button.dataset.tree = spriteHash(key) < oakProb ? "oak" : "pine";
      }
      button.setAttribute("aria-hidden", "true");
      button.addEventListener("click", (event) => {
        event.stopPropagation();
        const tower = getTowerAtCell(col, row);
        // Re-read buildType at click time (not capture time) — user may select build type after grid renders
        const heroSpecialNow = state.buildType && ["thorn", "void", "sun"].includes(state.buildType);
        // Hero-special builds replace fire towers — treat as a build action, not tower selection
        if (heroSpecialNow) {
          buildTowerAt(state.buildType, col, row);
          return;
        }
        if (tower) {
          selectTower(tower.id);
          return;
        }
        if (!state.buildType) {
          resetBuildPanel();
          return;
        }
        buildTowerAt(state.buildType, col, row);
      });
      gridLayer.appendChild(button);
    }
  }
}

function renderEnemies() {
  const alive = new Set(state.enemies.map((enemy) => enemy.id));
  for (const [id, node] of enemyNodes) {
    if (!alive.has(id)) {
      node.remove();
      enemyNodes.delete(id);
    }
  }
  state.enemies.forEach((enemy) => {
    let node = enemyNodes.get(enemy.id);
    if (!node) {
      node = document.createElement("div");
      node.className = `enemy ${enemy.kind}`;
      enemyLayer.appendChild(node);
      enemyNodes.set(enemy.id, node);
    }
    node.classList.toggle("hit", enemy.hit > 0);
    node.style.left = `${enemy.x}px`;
    node.style.top  = `${enemy.y}px`;
    const hp   = Math.max(0.25, enemy.hp / enemy.maxHp);
    const meta = ENEMY_SPRITES[enemy.kind];
    const sv   = 0.78 + hp * 0.22;

    // directional enemies handle flip via sprite; others: flip via scaleX
    if (meta?.dirs) {
      node.style.transform = `translate(-50%, -50%) scale(${sv}, ${sv})`;
    } else {
      const ePath = paths[enemy.pathIndex];
      const eSeg  = ePath?.[enemy.segment];
      const eNext = ePath?.[enemy.segment + 1] ?? eSeg;
      const movingLeft = eNext && eSeg && (eNext[0] - eSeg[0]) < 0;
      node.style.transform = `translate(-50%, -50%) scale(${movingLeft ? -sv : sv}, ${sv})`;
    }

    // Sprite animation
    if (meta) {
      // elder_dragon fly-in uses dedicated top-down sprite
      if (enemy.flyIn) {
        const flyInKey = `${enemy.kind}_flyin`;
        if (node.dataset.animKey !== flyInKey) {
          node.dataset.animKey = flyInKey;
          node.style.backgroundImage = `url('../assets/runtime/sprites/enemies/elder_dragon_flyin.png')`;
          node.style.width  = `${meta.ds}px`;
          node.style.height = `${meta.ds}px`;
          const nFrames = meta.frames?.flyin || 6;
          node.style.backgroundSize = `${getSpriteDisplayWidth(meta, nFrames)}px ${meta.ds}px`;
          node.style.backgroundPosition = "0 0";
        }
        node.style.backgroundPositionX = `-${(enemy.animFrame || 0) * getSpriteFrameStep(meta)}px`;
      } else {
        const state_name = enemy.animState || 'walk';
        const dir      = meta.dirs ? getEnemyDir(enemy) : null;
        const animKey  = dir ? `${enemy.kind}_${state_name}_${dir}` : `${enemy.kind}_${state_name}`;
        const atlasAnim = getAtlasAnimation(animKey);

        if (atlasAnim) {
          const frameName = atlasAnim.frames[(enemy.animFrame || 0) % atlasAnim.frames.length];
          if (applyAtlasFrame(node, frameName, meta.ds)) {
            node.dataset.animKey = animKey;
            node.dataset.atlasFrame = frameName;
            return;
          }
        }

        if (node.dataset.animKey !== animKey) {
          node.dataset.animKey = animKey;
          node.dataset.atlasFrame = "";
          const assetDir = meta.assetDir || '../assets/runtime/sprites/enemies';
          const path = dir
            ? `${assetDir}/${enemy.kind}_${state_name}_${dir}.png?v=${SPRITE_VER}`
            : `${assetDir}/${enemy.kind}_${state_name}.png?v=${SPRITE_VER}`;
          node.style.backgroundImage = `url('${path}')`;
          node.style.width  = `${meta.ds}px`;
          node.style.height = `${meta.ds}px`;
          const frEntry = meta.frames[state_name];
          const nFrames = dir ? (frEntry?.[dir] || 1) : (frEntry || 1);
          node.style.backgroundSize = `${getSpriteDisplayWidth(meta, nFrames)}px ${meta.ds}px`;
          node.style.backgroundPosition = "0 0";
        }
        node.style.backgroundPositionX = `-${(enemy.animFrame || 0) * getSpriteFrameStep(meta)}px`;
      }
    }
  });
}

function renderProjectiles() {
  const alive = new Set(state.projectiles.map((projectile) => projectile.id));
  for (const [id, node] of projectileNodes) {
    if (!alive.has(id)) {
      node.remove();
      projectileNodes.delete(id);
    }
  }
  state.projectiles.forEach((projectile) => {
    let node = projectileNodes.get(projectile.id);
    if (!node) {
      node = document.createElement("div");
      if (projectile.sprite) {
        node.className = `projectile has-sprite ${projectile.sprite}-proj`;
      } else {
        node.className = "projectile";
      }
      enemyLayer.appendChild(node);
      projectileNodes.set(projectile.id, node);
    }
    const t = 1 - projectile.life / projectile.maxLife; // 0 = at tower, 1 = at target
    const cx = projectile.x + (projectile.tx - projectile.x) * t;
    const cy = projectile.y + (projectile.ty - projectile.y) * t;
    node.style.left = `${cx}px`;
    node.style.top = `${cy}px`;
    if (projectile.sprite) {
      const angle = Math.atan2(
        projectile.ty - projectile.y,
        projectile.tx - projectile.x
      ) * 180 / Math.PI;
      // Animate multi-frame sprites; single-frame ones just rotate
      const fw = PROJ_SPRITE_FW[projectile.sprite];
      if (fw) {
        const frames = PROJ_SPRITE_FRAMES[projectile.sprite] || 3;
        const frame = Math.floor(t * frames * 2) % frames; // cycle 2x during flight
        node.style.backgroundPositionX = `-${frame * fw}px`;
      }
      node.style.transform = `translate(-50%,-50%) rotate(${angle}deg)`;
    } else {
      node.style.color = projectile.color;
    }
  });
}

function addEffect(className, x, y) {
  const node = document.createElement("div");
  node.className = className;
  node.style.left = `${x}%`;
  node.style.top = `${y}%`;
  battlefield.appendChild(node);
  setTimeout(() => node.remove(), 1300);
}

function updateHud() {
  setCachedText(goldEl, "gold", Number.isFinite(state.gold) ? state.gold : "∞");
  setCachedText(woodEl, "wood", Math.floor(state.wood));
  setCachedText(stoneEl, "stone", Math.floor(state.stone));
  setCachedText(waveEl, "wave", state.wave);
  updateHeroChargeButton();
  updateBaseEther();
}

function setCachedText(node, key, value) {
  const text = String(value);
  if (hudCache[key] === text) return;
  hudCache[key] = text;
  node.textContent = text;
}

function getWaveLabel(wave) {
  const plan = getWavePlan(wave);
  const tier = Math.max(0, Math.floor((wave - 21) / 5));
  if (tier <= 0) return plan.label;
  return `${plan.label} lv.${tier + 1}`;
}

let waveAnnounceTimer = null;
function showWaveAnnounce(wave) {
  if (!waveAnnounceEl) return;
  if (waveAnnounceTimer) clearTimeout(waveAnnounceTimer);
  const label = getWaveLabel(wave);
  waveAnnounceEl.innerHTML = `<span class="wave-announce-label">Волна ${wave}</span><span class="wave-announce-name">${label}</span>`;
  waveAnnounceEl.classList.remove("visible");
  requestAnimationFrame(() => {
    waveAnnounceEl.classList.add("visible");
    waveAnnounceTimer = setTimeout(() => {
      waveAnnounceEl.classList.remove("visible");
    }, 3000);
  });
}

function updateHeroChargeButton() {
  if (!heroChargeEl) return;
  const needed = getHeroSummonKills();
  const current = Math.min(state.heroChargeKills, needed);
  setCachedText(heroChargeEl, "heroCharge", state.heroActive ? "field" : state.heroReturning ? "return" : `${current}/${needed}`);
  const heroBtn = document.getElementById("heroSkill");
  if (heroBtn) {
    heroBtn.classList.toggle("ready", Boolean(state.heroId) && state.heroChargeKills >= needed && !state.heroActive && !state.heroReturning);
    heroBtn.classList.toggle("active", state.heroActive || state.heroReturning);
  }
}

function updateBaseEther() {
  const safeLives = Math.max(0, Math.min(20, state.lives));
  const firstPhase = safeLives > 10;
  const progress = firstPhase ? (20 - safeLives) / 10 : (10 - safeLives) / 10;
  const from = firstPhase ? [47, 116, 255] : [88, 214, 112];
  const to = firstPhase ? [88, 214, 112] : [224, 58, 58];
  const color = mixColor(from, to, progress);
  const coreColor = mixColor(
    firstPhase ? [157, 225, 255] : [179, 255, 156],
    firstPhase ? [179, 255, 156] : [255, 147, 104],
    progress
  );

  battlefield.style.setProperty("--base-ether", color);
  battlefield.style.setProperty("--base-ether-core", coreColor);
}

function mixColor(from, to, progress) {
  const t = Math.max(0, Math.min(1, progress));
  const channels = from.map((value, index) => Math.round(value + (to[index] - value) * t));
  return `rgb(${channels.join(", ")})`;
}

function endGame() {
  state.gameOver = true;
  state.running = false;
  state.enemies = [];
  state.projectiles = [];
  battlefield.classList.add("destroyed");
  castleSprite.classList.add("is-destroyed");
  showPanelNotice("Castle destroyed", "Ether exhausted. Game over.");

  const survived = state.wave - 1;
  sheetTitle.textContent = "Castle Fallen";
  sheetSubtitle.textContent = survived > 0 ? `You survived ${survived} ${waveWord(survived)}.` : "Enemies broke through on the first wave.";
  sheetBody.innerHTML = `
    <div class="game-over-panel">
      <p class="game-over-result">${survived >= 20 ? "Worthy result — you reached the end of the first act." : survived >= 10 ? "Good attempt — now you know the weak points." : "Every defeat is a lesson. Try again."}</p>
      <button type="button" class="game-over-restart" onclick="location.reload()">Restart</button>
    </div>
  `;
  sheet.classList.remove("hidden");
}

function waveWord(n) {
  return n === 1 ? "wave" : "waves";
}

function renderTowerChoices() {
  const btn = (type) => {
    const def = towerDefs[type];
    return `<button type="button" data-type="${type}" aria-label="${def.name}"><i class="building-icon ${type}"></i></button>`;
  };

  let extraSlots;
  if (state.heroId) {
    // Show all 3 special buildings — locked until purchased
    extraSlots = Object.entries(extraRuneDefs).map(([id, rune]) => {
      const owned = state.unlockedBuildings.includes(id);
      if (owned) return btn(id);
      const canAfford = state.gold >= rune.cost;
      return `<button type="button" class="tower-slot-locked${canAfford ? " can-afford" : ""}" data-buy-building="${id}" title="${rune.name} · ${rune.cost} gold">
        <i class="building-icon ${id}"></i>
        <span class="slot-lock-badge"></span>
        <span class="slot-lock-cost">${rune.cost}</span>
      </button>`;
    }).join("");
  } else {
    extraSlots = Array.from({ length: 3 }, (_, i) => {
      const type = state.unlockedBuildings[i];
      return type ? btn(type) : `<div class="tower-slot-empty"></div>`;
    }).join("");
  }

  towerChoices.innerHTML = `<div class="tower-row extra">${extraSlots}</div><div class="tower-row base">${baseBuildings.map(btn).join("")}</div>`;
  towerChoices.querySelectorAll("[data-buy-building]").forEach(b => {
    b.addEventListener("click", () => buyBuildingFromPanel(b.dataset.buyBuilding));
  });
  document.querySelectorAll("[data-type]").forEach((button) => {
    button.classList.toggle("active", button.dataset.type === state.buildType);
  });
}

function buyBuildingFromPanel(id) {
  if (!state.heroId || state.unlockedBuildings.includes(id)) return;
  const rune = extraRuneDefs[id];
  if (state.gold < rune.cost) { showBuildInfo("", rune.cost); return; }
  state.gold -= rune.cost;
  state.unlockedBuildings.push(id);
  updateHud();
  renderTowerChoices();
  showPanelNotice(`${rune.name} unlocked`, "Tap a cell to build.");
}

function canBuyHero() {
  return state.wave > 5;
}

function showHeroSheet() {
  sheetTitle.textContent = "Хранители Последнего узла";
  sheetSubtitle.textContent = canBuyHero()
    ? `Выберите одного хранителя. Общий ответ накапливается убийствами башен.`
    : "Открывается после пяти закрытых волн.";

  sheetBody.innerHTML = `<div class="hero-grid">${Object.entries(heroDefs).map(([id, hero]) => {
    const selected = state.heroId === id;
    const locked = !canBuyHero();
    const disabled = locked || (state.heroId && !selected) || state.gold < hero.cost;
    return `
      <article class="hero-card ${selected ? "selected" : ""}">
        <div class="hero-mark">${hero.mark}</div>
        <strong>${hero.name} <span style="font-weight:400;font-size:10px;color:var(--muted)">${hero.race}</span></strong>
        <button class="info-btn" type="button" data-info-card>?</button>
        <button type="button" data-hero="${id}" ${disabled ? "disabled" : ""}>${selected ? "✓" : locked ? "🔒" : hero.cost+" gld"}</button>
        <ul class="skill-list hidden">
          ${hero.skills.map((skill) => `<li>${skill}</li>`).join("")}
        </ul>
      </article>
    `;
  }).join("")}</div>`;

  sheetBody.querySelectorAll("[data-hero]").forEach((button) => {
    button.addEventListener("click", () => buyHero(button.dataset.hero));
  });
  sheetBody.querySelectorAll("[data-info-card]").forEach(btn => {
    btn.addEventListener("click", () => {
      const skillList = btn.closest("article").querySelector(".skill-list");
      const open = skillList.classList.toggle("hidden");
      btn.classList.toggle("open", !open);
    });
  });
  openSheet();
}

function buyHero(id) {
  if (!canBuyHero() || state.heroId) return;
  const hero = heroDefs[id];
  if (state.gold < hero.cost) { showBuildInfo("", hero.cost); return; }
  state.gold -= hero.cost;
  state.heroId = id;
  updateHud();
  renderTowerChoices();
  const needed = getHeroSummonKills();
  showPanelNotice(hero.name, `Хранитель выбран. Общий ответ: ${Math.min(state.heroChargeKills, needed)}/${needed}.`);
  showRuneShop();
}

function showRuneShop() {
  sheetTitle.textContent = "Rune Shop";
  sheetSubtitle.textContent = state.heroId
    ? "Открывайте формы · обменивайте Злато на материал."
    : "Выберите хранителя, чтобы открыть чертежи.";

  const locked = !state.heroId;
  const runesHtml = Object.entries(extraRuneDefs).map(([id, rune]) => {
    const owned = state.unlockedBuildings.includes(id);
    const disabled = locked || owned || state.gold < rune.cost;
    const btnText = owned ? "Связано" : locked ? "Хранитель" : "Открыть";
    return `
      <article class="rune-card">
        <div class="rune-mark">${rune.mark}</div>
        <strong>${rune.name}</strong>
        <button class="info-btn" type="button" data-info-card>?</button>
        <button type="button" data-rune="${id}" ${disabled ? "disabled" : ""}>${btnText}</button>
        <div class="card-detail hidden">
          <span class="price-tag">⚙ ${rune.cost} gld</span>
          <br/>${rune.note}
        </div>
      </article>
    `;
  }).join("");

  const canBuyWood = state.gold >= 10;
  const canBuyStone = state.gold >= 10;
  const woodFull = state.wood >= RESOURCE_CAP;
  const stoneFull = state.stone >= RESOURCE_CAP;
  const marketHtml = `
    <article class="rune-card market-card">
      <div class="rune-mark">🪵</div>
      <div>
        <strong>10 Живого древа</strong>
        <span>Обменять за 10 Злата.</span>
      </div>
      <button type="button" data-market="wood" ${!canBuyWood || woodFull ? "disabled" : ""}>${woodFull ? "Предел" : "10 Злата"}</button>
    </article>
    <article class="rune-card market-card">
      <div class="rune-mark">🪨</div>
      <div>
        <strong>10 Камня памяти</strong>
        <span>Обменять за 10 Злата.</span>
      </div>
      <button type="button" data-market="stone" ${!canBuyStone || stoneFull ? "disabled" : ""}>${stoneFull ? "Предел" : "10 Злата"}</button>
    </article>
  `;

  sheetBody.innerHTML = `<div class="rune-shop">${runesHtml}${marketHtml}</div>`;

  sheetBody.querySelectorAll("[data-rune]").forEach((button) => {
    button.addEventListener("click", () => buyRune(button.dataset.rune));
  });
  sheetBody.querySelectorAll("[data-market]").forEach((button) => {
    button.addEventListener("click", () => buyMarketResource(button.dataset.market));
  });
  sheetBody.querySelectorAll("[data-info-card]").forEach(btn => {
    btn.addEventListener("click", () => {
      const detail = btn.closest("article").querySelector(".card-detail");
      const open = detail.classList.toggle("hidden");
      btn.classList.toggle("open", !open);
    });
  });
  openSheet();
}

function buyMarketResource(resource) {
  if (state.gold < 10) return;
  if (resource === "wood" && state.wood >= RESOURCE_CAP) return;
  if (resource === "stone" && state.stone >= RESOURCE_CAP) return;
  state.gold -= 10;
  if (resource === "wood") state.wood = Math.min(RESOURCE_CAP, state.wood + 10);
  if (resource === "stone") state.stone = Math.min(RESOURCE_CAP, state.stone + 10);
  updateHud();
  showRuneShop();
}

function buyRune(id) {
  if (!state.heroId || state.unlockedBuildings.includes(id)) return;
  const rune = extraRuneDefs[id];
  if (state.gold < rune.cost) { showBuildInfo("", rune.cost); return; }
  state.gold -= rune.cost;
  state.unlockedBuildings.push(id);
  renderTowerChoices();
  updateHud();
  showPanelNotice(`${rune.name} unlocked`, "New building in the bottom dock.");
  showRuneShop();
}

function openSheet() {
  sheet.classList.remove("hidden");
}

function closeSheet() {
  sheet.classList.add("hidden");
}

function showPanelNotice(title, text) {
  panelTitle.textContent = title;
  panelText.textContent = text;
  buildInfoEl.innerHTML = text
    ? `<span class="build-info-name">${title}</span><span class="build-info-detail">${text}</span>`
    : `<span class="build-info-name">${title}</span>`;
  buildInfoEl.classList.remove("hidden");
  clearTimeout(buildInfoTimer);
  buildInfoTimer = setTimeout(hideBuildInfo, 3500);
}

function setBuildModeClass() {
  battlefield.classList.remove("building", "building-fire", "building-ice", "building-storm");
  if (state.buildType) {
    battlefield.classList.add("building", `building-${state.buildType}`);
  }
}

function getActivePathCount() {
  return state.wave >= 10 ? 2 : 1;
}

function upgradeCost(tower) {
  if (isEconomyBuilding(tower.type)) {
    const costs = [0, 0, 150, 240, 360];
    return costs[tower.level + 1] || 260;
  }

  const costs = [0, 0, 200, 310, 450, 640, 860, 1120, 1420, 1760, 2140, 2560, 3040];
  return costs[tower.level + 1] || 2600;
}

function getTowerCombatStats(tower) {
  if (tower.type === "fire" && tower.specialization) {
    const branch = watchtowerSpecializations[tower.specialization];
    const stats = { ...branch };
    if (tower.level >= 3) {
      if (tower.specialization === "infantry") stats.rate *= 0.9;
      if (tower.specialization === "air") stats.pierce = 2;
      if (tower.specialization === "siege") stats.splash += 18;
    }
    if (tower.level >= 5) {
      if (tower.specialization === "infantry") stats.chainOnKill = true;
      if (tower.specialization === "air") stats.slowOnHit = 2;
      if (tower.specialization === "siege") stats.concussion = true;
    }
    if (tower.subtype) applyWatchtowerSubtypeStats(tower, stats);
    applyMasteryStats(tower, stats);
    return stats;
  }
  return towerDefs[tower.type];
}

function applyWatchtowerSubtypeStats(tower, stats) {
  if (tower.subtype === "tracker") {
    stats.range *= 1.18;
    stats.slowOnHit = Math.max(stats.slowOnHit || 0, 0.8);
    if (tower.level >= 7) stats.range *= 1.12;
    if (tower.level >= 9) stats.chainOnKill = true;
  } else if (tower.subtype === "assassin") {
    stats.damage *= 1.28;
    stats.markMultiplier = 2.6;
    if (tower.level >= 7) stats.markMultiplier = 3.1;
    if (tower.level >= 9) stats.critEvery = 5;
  } else if (tower.subtype === "scorpion") {
    stats.damage *= 1.45;
    stats.slowOnHit = Math.max(stats.slowOnHit || 0, 3);
    if (tower.level >= 7) stats.damage *= 1.18;
    if (tower.level >= 8) stats.slowOnHit = 4;
  } else if (tower.subtype === "hail") {
    stats.pierce = Math.max(stats.pierce || 0, 4);
    stats.damage *= 0.86;
    if (tower.level >= 7) stats.pierce = Math.max(stats.pierce || 0, 6);
    if (tower.level >= 9) stats.rate *= 0.82;
  } else if (tower.subtype === "mortar") {
    stats.damage *= 1.65;
    stats.rate *= 1.2;
    if (tower.level >= 7) stats.damage *= 1.24;
    if (tower.level >= 9) stats.siegeEvery = 3;
  } else if (tower.subtype === "grapeshot") {
    stats.splash *= 1.45;
    stats.damage *= 1.08;
    if (tower.level >= 7) stats.splash *= 1.22;
    if (tower.level >= 9) stats.rate *= 0.85;
  }
}

function applyMasteryStats(tower, stats) {
  const mastery = Math.max(0, tower.level - 9);
  for (let i = 0; i < mastery; i += 1) {
    const type = i % 3;
    if (type === 0) stats.damage *= 1.1;
    if (type === 1) stats.range *= 1.05;
    if (type === 2) stats.rate *= 0.93;
  }
}

function canTargetEnemy(combat, enemy) {
  if (!isEnemyActive(enemy)) return false;
  if (!combat.target || combat.target === "any") return true;
  return enemy.category === combat.target;
}

const TOWER_CATEGORY_BONUS = {
  thorn: { ground: 1.50, air: 0.75, machine: 0.65 },
  void:  { ground: 1.00, air: 0.60, machine: 1.80 },
  sun:   { ground: 0.90, air: 1.55, machine: 0.80 },
};

function getTowerDamageAgainst(tower, combat, enemy) {
  let damage = combat.damage * tower.level;
  const bonus = TOWER_CATEGORY_BONUS[tower.type];
  if (bonus && enemy.category) damage *= bonus[enemy.category] ?? 1;
  if (tower.specialization === "infantry" && tower.level >= 3 && tower.shots % 3 === 0) {
    damage *= combat.markMultiplier || 2;
  }
  if (tower.specialization === "infantry" && tower.level >= 4 && enemy.hp / enemy.maxHp < (tower.subtype === "assassin" && tower.level >= 8 ? 0.48 : 0.35)) {
    damage *= 1.6;
  }
  if (combat.critEvery && tower.shots % combat.critEvery === 0) damage *= 1.85;
  if (tower.specialization === "air" && tower.level >= 4 && !tower.hitTargets.has(enemy)) {
    damage *= 1.8;
    tower.hitTargets.add(enemy);
  }
  if (tower.specialization === "siege") {
    if (enemy.category === "machine" && tower.level >= 4) damage *= 2;
    if (combat.siegeEvery && tower.shots % combat.siegeEvery === 0 && enemy.category === "machine") damage *= 1.75;
    if (enemy.category !== "machine") damage *= 0.55;
  }
  return damage;
}

function getTowerPanelText(tower, combat) {
  const next = getNextUpgradeInfo(tower);
  const def = towerDefs[tower.type];
  const base = `Damage ${Math.round(combat.damage * tower.level)} · range ${Math.round(combat.range)}`;
  const vs = def.versus ? `Versus: ${def.versus}` : null;
  const hint = getUpcomingEconHint(tower);
  const parts = [base, vs, next ? `Next: ${next.name}` : null, hint ? `⚑ ${hint}` : null].filter(Boolean);
  return parts.join(". ");
}

function getUpgradeButtonText(tower) {
  if (isEconomyBuilding(tower.type) && tower.level >= MAX_ECONOMY_LEVEL) {
    return "Предел формы";
  }
  if (tower.level >= MAX_TOWER_LEVEL) {
    return "Предел формы";
  }
  if (tower.type === "fire" && tower.level === 1 && !tower.specialization) {
    return "Choose blueprint";
  }
  if (tower.type === "fire" && tower.specialization && tower.level === 5 && !tower.subtype) {
    return "Choose subtype";
  }
  const econBlock = checkEconReq(tower);
  if (econBlock) return `${econBlock}`;
  const next = getNextUpgradeInfo(tower);
  const rc = getUpgradeResourceCost(tower);
  const resLabel = (rc.wood > 0 || rc.stone > 0) ? formatResourceCost(rc) : "Без материала";
  return next ? `${next.name} · ${upgradeCost(tower)} gld. · ${resLabel}` : `Upgrade · ${upgradeCost(tower)} gld. · ${resLabel}`;
}

function getNextUpgradeInfo(tower) {
  if (tower.type !== "fire" || !tower.specialization) return null;
  const branch = watchtowerSpecializations[tower.specialization];
  if (tower.level < 5) return branch.upgrades[tower.level + 1];
  if (tower.level === 5 && !tower.subtype) return { name: "Развилка пути" };
  if (tower.subtype && tower.level < 9) return branch.subtypes[tower.subtype].upgrades[tower.level + 1];
  if (tower.level >= MAX_TOWER_LEVEL) return null;
  const mastery = ["Mastery: +damage", "Mastery: +range", "Mastery: +speed"];
  return { name: mastery[Math.max(0, tower.level - 9) % mastery.length] };
}

function countFireAtLevel(minLevel) {
  return Object.values(state.towers).filter(t => t.type === "fire" && t.level >= minLevel).length;
}

function getSpecialBuildBlockReason(type) {
  const cap = SPECIAL_BUILD_CAPS[type];
  if (!cap) return "";
  const current = Object.values(state.towers).filter(t => t.type === type).length;
  if (current >= cap) return `Limit: no more than ${cap} ${towerDefs[type].name}.`;
  return "";
}

function getBuildBlockReason(col, row, type = state.buildType) {
  const tower = getTowerAtCell(col, row);

  const isHeroSpecial = ["thorn", "void", "sun"].includes(type);
  if (isHeroSpecial) {
    if (!tower || tower.type !== "fire") return "Requires a watchtower.";
    const specialReason = getSpecialBuildBlockReason(type);
    if (specialReason) return specialReason;
    return "";
  }

  if (tower) {
    return "Cell already occupied.";
  }

  const terrainReason = getTerrainBlockReason(col, row);
  if (terrainReason) {
    return terrainReason;
  }

  const resource = getResourceAtCell(col, row);
  const opened = state.clearedCells.has(cellKey(col, row));

  if (type === "fire") {
    const isGrowing = !!resource && state.growingCells.has(cellKey(col, row));
    return (opened && !resource) || isGrowing ? "" : "Дозорной веси нужна свободная клетка.";
  }

  if (type === "ice") {
    return resource === "tree" ? "" : "Плотницкую артель можно поставить только на лес.";
  }

  if (type === "storm") {
    return resource === "stone" ? "" : "Каменную артель можно поставить только на камень.";
  }

  if (resource) {
    return "Resource cell.";
  }

  const specialReason = getSpecialBuildBlockReason(type);
  if (specialReason) return specialReason;

  return "";
}

function getTerrainBlockReason(col, row) {
  const position = gridToPercent(col, row);
  const xPercent = position.x;
  const yPercent = position.y;
  const key = cellKey(col, row);

  if (manualBlockedCells.has(key)) {
    return "Закрытая область.";
  }

  if (manualAllowedCells.has(key)) {
    const mapX = xPercent * 3.9;
    const mapY = yPercent * 6.1;
    if (distanceToAnyPath(mapX, mapY) < ROAD_BLOCK_DISTANCE) return "Дорога.";
    return "";
  }

  if (xPercent < 7 || xPercent > 93 || yPercent < 7 || yPercent > 92) {
    return "Край поля.";
  }

  const mapX = xPercent * 3.9;
  const mapY = yPercent * 6.1;

  if (isInsideBlockedStructure(mapX, mapY)) {
    return "Последний узел.";
  }

  const roadDistance = distanceToAnyPath(mapX, mapY);
  if (roadDistance < ROAD_BLOCK_DISTANCE) {
    return "Дорога.";
  }

  return "";
}

function generateResourceMap() {
  const resourceKeys = [];
  for (let row = 0; row < state.grid.rows; row += 1) {
    for (let col = 0; col < state.grid.cols; col += 1) {
      const ck = cellKey(col, row);
      if (!getTerrainBlockReason(col, row) && !getTowerAtCell(col, row) && !noResourceCells.has(ck)) {
        resourceKeys.push(ck);
      }
    }
  }

  const stoneTarget = resourceKeys.length - Math.floor(resourceKeys.length * 0.70);
  const weighted = resourceKeys
    .map((key) => {
      const [, row] = key.split(",").map(Number);
      // upper quarry zone: slight stone bias; lower rows: growing tree bias
      const bias = isUpperQuarryZoneKey(key)
        ? 0.28
        : -Math.min(0.85, Math.max(0, (row - 15) * 0.13));
      return { key, score: seededCellScore(key) + bias };
    })
    .sort((a, b) => b.score - a.score);
  state.resourceCells.clear();
  weighted.forEach(({ key }, index) => {
    state.resourceCells.set(key, index < stoneTarget ? "stone" : "tree");
  });

  state.clearedCells.forEach((key) => state.resourceCells.delete(key));
  state.resourceCells.set("5,23", "tree");
  state.resourceCells.set("10,23", "stone");
}

function seededCellScore(key) {
  const [col, row] = key.split(",").map(Number);
  const n = Math.sin((col + 1) * 12.9898 + (row + 1) * 78.233 + RESOURCE_LAYOUT_SEED) * 43758.5453;
  return n - Math.floor(n);
}

// Independent hash for visual sprite assignment (rock type, tree type)
// Uses different constants so it doesn't correlate with resource placement
function spriteHash(key) {
  const [col, row] = key.split(",").map(Number);
  const n = Math.sin((col + 7) * 31.7753 + (row + 3) * 89.4561) * 43758.5453;
  return n - Math.floor(n);
}

function isUpperQuarryZoneKey(key) {
  const [col, row] = key.split(",").map(Number);
  return col >= 3 && col <= 8 && row >= 6 && row <= 16;
}

function ensureResourceMap() {
  if (!state.grid.rows || state.resourceCells.size > 0) return;
  generateResourceMap();
}

function getResourceAtCell(col, row) {
  ensureResourceMap();
  const key = cellKey(col, row);
  if (state.clearedCells.has(key) || getTowerAtCell(col, row) || getTerrainBlockReason(col, row)) {
    return "";
  }
  return state.resourceCells.get(key) || "";
}

function getCellLabel(col, row, resource, reason) {
  if (resource === "tree") return "Лес. Здесь можно связать Плотницкий круг.";
  if (resource === "stone") return "Камень. Здесь можно связать Каменный круг.";
  return reason || "Открытая клетка";
}

function claimCellForBuilding(col, row) {
  state.clearedCells.add(cellKey(col, row));
}

function scheduleRegrowth(tower) {
  if (!isEconomyBuilding(tower.type)) return;
  const resourceType = tower.type === "ice" ? "tree" : "stone";
  // pine 4-5 waves, oak 7-8, stone 9-10; last 4 waves are animation frames
  let totalWaves;
  let treeVariant = null;
  if (resourceType === "stone") {
    totalWaves = 9 + Math.floor(Math.random() * 2);
  } else {
    // Use same spriteHash logic as renderGrid so growth speed matches visual appearance
    const oakProb = Math.max(0, Math.min(1, 1 - (tower.row - 6) / 11));
    treeVariant = spriteHash(cellKey(tower.col, tower.row)) < oakProb ? "oak" : "pine";
    totalWaves = treeVariant === "oak"
      ? 7 + Math.floor(Math.random() * 2)
      : 4 + Math.floor(Math.random() * 2);
  }
  const targetWave = state.wave + totalWaves;
  const cells = [[tower.col, tower.row]];
  for (let dy = -1; dy <= 1; dy++) {
    for (let dx = -1; dx <= 1; dx++) {
      if (dx === 0 && dy === 0) continue;
      const nc = tower.col + dx, nr = tower.row + dy;
      if (nc < 0 || nc >= state.grid.cols || nr < 0 || nr >= state.grid.rows) continue;
      if (!getTowerAtCell(nc, nr) && !getTerrainBlockReason(nc, nr) && state.clearedCells.has(cellKey(nc, nr))) {
        cells.push([nc, nr]);
      }
    }
  }
  state.regrowthQueue.push({ targetWave, cells, resourceType, treeVariant });
}

function processRegrowth() {
  const newGrowing = new Map();
  state.regrowthQueue = state.regrowthQueue.filter((entry) => {
    const wavesLeft = entry.targetWave - state.wave;
    if (wavesLeft <= 0) {
      // Fully grown — make permanent
      for (const [col, row] of entry.cells) {
        const key = cellKey(col, row);
        if (getTowerAtCell(col, row) || getTerrainBlockReason(col, row)) continue;
        state.clearedCells.delete(key);
        state.resourceCells.set(key, entry.resourceType);
        if (entry.resourceType === "stone") state.rockBCells.add(key);
      }
      return false;
    }
    if (wavesLeft <= 5) {
      // Animation phase: frame 0 = first appearance, 4 = last before full
      const frame = 5 - wavesLeft;
      for (const [col, row] of entry.cells) {
        const key = cellKey(col, row);
        if (getTowerAtCell(col, row) || getTerrainBlockReason(col, row)) continue;
        state.clearedCells.delete(key);
        state.resourceCells.set(key, entry.resourceType);
        if (entry.resourceType === "stone" && frame === 0) state.rockBCells.add(key);
        newGrowing.set(key, { frame, variant: entry.treeVariant });
      }
    }
    // wavesLeft > 5: still hidden, cells stay in clearedCells
    return true;
  });
  state.growingCells = newGrowing;
  renderGrid();
}

function revealCellsAround(col, row) {
  for (let dy = -1; dy <= 1; dy += 1) {
    for (let dx = -1; dx <= 1; dx += 1) {
      if (dx === 0 && dy === 0) continue;
      const nextCol = col + dx;
      const nextRow = row + dy;
      if (nextCol < 0 || nextCol >= state.grid.cols || nextRow < 0 || nextRow >= state.grid.rows) continue;
      if (!getTowerAtCell(nextCol, nextRow) && !getTerrainBlockReason(nextCol, nextRow)) {
        state.clearedCells.add(cellKey(nextCol, nextRow));
      }
    }
  }
}

function isEconomyBuilding(type) {
  return type === "ice" || type === "storm";
}

function playerHasEconomyBuilding() {
  return Object.values(state.towers).some((t) => isEconomyBuilding(t.type));
}

function needsEconomyToUpgrade(tower) {
  return !isEconomyBuilding(tower.type) && tower.level >= 4 && !playerHasEconomyBuilding();
}

function countEconBuildings() {
  let sawmills = 0, quarries = 0;
  for (const t of Object.values(state.towers)) {
    if (t.type === "ice") sawmills++;
    else if (t.type === "storm") quarries++;
  }
  return { sawmills, quarries };
}

function getEconReqForUpgrade(toLevel) {
  const req = COMBAT_UPGRADE_ECON_REQ[Math.min(toLevel, COMBAT_UPGRADE_ECON_REQ.length - 1)];
  return { sawmills: req[0], quarries: req[1] };
}

function getUpcomingEconHint(tower) {
  if (isEconomyBuilding(tower.type)) return null;
  const have = countEconBuildings();
  for (let lvl = tower.level + 1; lvl <= tower.level + 2; lvl++) {
    const req = getEconReqForUpgrade(lvl);
    if (req.sawmills === 0 && req.quarries === 0) continue;
    if (have.sawmills >= req.sawmills && have.quarries >= req.quarries) continue;
    const parts = [];
    if (req.sawmills > have.sawmills) parts.push(`${req.sawmills - have.sawmills} more sawmill(s)`);
    if (req.quarries > have.quarries) parts.push(`${req.quarries - have.quarries} more quarry(ies)`);
    return `L${lvl}: ${parts.join(' + ')}`;
  }
  return null;
}

function checkEconReq(tower) {
  if (isEconomyBuilding(tower.type)) return null;
  const req = getEconReqForUpgrade(tower.level + 1);
  if (req.sawmills === 0 && req.quarries === 0) return null;
  const have = countEconBuildings();
  if (have.sawmills >= req.sawmills && have.quarries >= req.quarries) return null;
  const parts = [];
  if (req.sawmills > 0) parts.push(`${req.sawmills} sawmill(s)`);
  if (req.quarries > 0) parts.push(`${req.quarries} quarry(ies)`);
  return `Required: ${parts.join(" + ")}`;
}

function hasRaidHealth(tower) {
  return isEconomyBuilding(tower.type) || tower.type === "fire";
}

function getBuildResourceCost(type) {
  return { wood: 0, stone: 0 };
}

function getUpgradeResourceCost(tower) {
  const nextLevel = tower.level + 1;
  if (tower.type === "ice") {
    const w = [0, 0, 70, 135, 230];
    const s = [0, 0, 50, 100, 170];
    return { wood: w[nextLevel] || 0, stone: s[nextLevel] || 0 };
  }
  if (tower.type === "storm") {
    const w = [0, 0, 50, 100, 170];
    const s = [0, 0, 70, 135, 230];
    return { wood: w[nextLevel] || 0, stone: s[nextLevel] || 0 };
  }
  const w = [0, 0, 20, 50, 25, 90, 160, 245, 345, 465, 605, 765, 950];
  const s = [0, 0, 15, 35, 20, 75, 130, 205, 290, 390, 505, 640, 795];
  return { wood: w[nextLevel] || 950, stone: s[nextLevel] || 795 };
}

function canAffordResources(cost) {
  return state.wood >= cost.wood && state.stone >= cost.stone;
}

function spendResources(cost) {
  state.wood -= cost.wood;
  state.stone -= cost.stone;
}

function formatResourceCost(cost) {
  return `${cost.wood} Древа · ${cost.stone} Камня`;
}

function getBuildHint(type) {
  const def = towerDefs[type];
  const place = type === "ice"
    ? "Только на лесной клетке."
    : type === "storm"
      ? "Только на каменной клетке."
      : "Только на открытой клетке.";
  const roleHints = {
    thorn: "Частый ответ против наземных носителей.",
    void:  "Разрыв директивы против машин.",
    sun:   "Дальний ответ против воздуха.",
    fire:  "Гибкая форма с ветвящимися чертежами.",
  };
  const role = roleHints[type] ? `${roleHints[type]} ` : "";
  const rc = getBuildResourceCost(type);
  const resStr = (rc.wood > 0 || rc.stone > 0) ? `, ${formatResourceCost(rc)}` : "";
  return `${role}Цена ${def.cost}${resStr}. ${place}`;
}

function cellKey(col, row) {
  return `${col},${row}`;
}

function gridToPercent(col, row) {
  const rect = battlefield.getBoundingClientRect();
  const cellSize = state.grid.cellSize || rect.width / state.grid.cols;
  const x = ((col + 0.5) * cellSize / rect.width) * 100;
  const y = ((row + 0.5) * cellSize / rect.height) * 100;
  return { x, y };
}

function getTowerAtCell(col, row) {
  return Object.values(state.towers).find((tower) => tower.col === col && tower.row === row);
}

function isInsideBlockedStructure(x, y) {
  return structureBlockers.some((area) => (
    x >= area.x &&
    x <= area.x + area.w &&
    y >= area.y &&
    y <= area.y + area.h
  ));
}

function distanceToAnyPath(x, y) {
  let best = Infinity;
  for (const path of paths) {
    for (let i = 0; i < path.length - 1; i += 1) {
      best = Math.min(best, distanceToSegment(x, y, path[i], path[i + 1]));
    }
  }
  return best;
}

function distanceToSegment(x, y, a, b) {
  const vx = b[0] - a[0];
  const vy = b[1] - a[1];
  const wx = x - a[0];
  const wy = y - a[1];
  const lenSq = vx * vx + vy * vy;
  const t = Math.max(0, Math.min(1, (wx * vx + wy * vy) / lenSq));
  const px = a[0] + vx * t;
  const py = a[1] + vy * t;
  return Math.hypot(x - px, y - py);
}

renderTowerChoices();
renderGrid();
seedDefaultTowers();
renderGrid();
renderTowers();
updateHud();
requestAnimationFrame(update);
