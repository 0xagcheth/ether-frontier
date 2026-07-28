# Ether Frontier — Prompt/Lore Alignment Audit v1

Status: **PASS — text/runtime aligned; visual approval pending**  
Updated: 2026-07-24

## Scope

Проверены активные источники, влияющие на игровой runtime, concept art и
production layered sprite atlases. Старые v1–v5 документы могут сохраняться как
история итераций, но не являются production-входами.

## Canon lock

- Публичное название: **Ether Frontier: Семь кругов Ирия**.
- Подзаголовок кампании: **Семь дорог последнего узла**.
- Единственный активный вариант лора — вариант C.
- Семь дорог — оригинальный игровой союз культурных ремесленных традиций, а не
  заявление о единой исторической доктрине.
- Явь, Навь и Правь — спорная внутриигровая школа толкования.
- Даария не подаётся как подтверждённый исторический факт.
- Китеж-17, секретная лаборатория, управляющий архив и варианты A/B исключены.
- Вражеские различия выражаются материалом, способом движения и игровой
  функцией, а не этнической или расовой кодировкой.

## Corrections completed

| Область | Исправление |
|---|---|
| Реальная механика | Лор наложен на три ресурса, рабочие места, открытие клеток, восстановление природы, рейды, две дороги, волны, развитие дозора и заряд хранителей |
| Runtime UI | Названия ресурсов, построек, героев, врагов, боссов, волн, действий и сообщений перенесены на канон v6 |
| Tutorial | Отладочная первая волна со всеми существами заменена читаемой стартовой волной |
| Object identity | Каждый runtime ID получил функцию, материал, силуэт и обязательные подвижные/сменные слои |
| Camera | Runtime-объекты закреплены за true top-down orthographic 90° |
| Material | Отдельные вырубные картонные детали, печатная бумага, видимые кромки, зазоры и локальные контактные тени |
| Mechanisms | Универсальный арбалет запрещён; оружие определяется ролью конкретного объекта |
| Prompt chain | Concept-проверка C01–C07 отделена от object-atlas production |
| Source of truth | Runtime atlas содержит только прозрачные tight sprites; JSON владеет rect, pivot, attachment, drawOrder и animations |

## Active production sources

### Lore and mechanics

- `../02_creative/game-lore-bible-v6.md`
- `../01_design/game-system-and-lore-integration-v1.md`
- `../02_creative/entity-mechanics-codex-v5.md`
- `../02_creative/character-bible-v5.md`
- `../02_creative/faction-bible-v5.md`

### Concept art

- `../03_art/world-concept-art-prompt-bible-v2.md`
- `../../assets/staging/prompts/concept_art_call_plan_v2.json`

### Layered objects

- `asset-prompt-bible-v6.md`
- `object-family-and-variation-spec-v5.md`
- `object-lore-material-overlay-v5.md`
- `../../assets/staging/prompts/layered_sprite_atlas_master_prompt_v2.md`
- `../../assets/staging/prompts/restart_all_layered_sprite_atlases_clean_v2.md`

## Concept approval sequence

| Call | Проверяемая гипотеза |
|---|---|
| C01 | Совместимость маршрута, башен и картонного мира с реальным TD-экраном |
| C02 | Читаемость экономики, рабочих мест и восстановления природы |
| C03 | Различимость трёх вражеских материальных грамматик без этнической кодировки |
| C04 | Захват Серых как добавление/снятие отдельных child layers |
| C05 | Хранители как поддержка tower-defense композиции, а не отдельная RPG-сцена |
| C06 | Масштаб боссов без потери маршрута и игровых целей |
| C07 | UI как ясный картонный прибор без декоративного шума |

## Validation result

- JavaScript проходит синтаксическую проверку.
- Игра загружается, стартовая волна запускается и использует новый tutorial
  roster.
- Watchtower ImageGen 2 source plan валиден: 14 упорядоченных вызовов.
- Текущие browser 404 относятся к ещё не созданным утверждённым runtime atlas
  PNG/JS, а не к ошибке переноса лора.

## Remaining production gate

1. Сгенерировать C01–C07 через built-in ImageGen 2.
2. Выбрать и явно утвердить одно совместимое направление мира.
3. Зафиксировать утверждённые concept images в `canon-asset-registry.md`.
4. Запустить Watchtower через
   `layered_sprite_atlas_master_prompt_v2.md`.
5. Пройти visual + technical validation Watchtower.
6. Только после подтверждения переходить к следующему объекту.

До прохождения C01–C07 и утверждения направления production atlas не
генерируется.
