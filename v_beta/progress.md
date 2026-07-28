Original prompt: Проверить на существующей HTML-игре, совместим ли новый лор и картонный визуальный стиль с реальным игровым экраном.

## 2026-07-24

- Найден основной экран: `game/index.html`.
- Ошибочно добавленный CSS visual-hypothesis режим удалён из HTML по уточнению
  пользователя: требуется нарисованный ImageGen mockup, а не применение стиля к
  странице.
- Сохранены исходный браузерный reference и screenshot первого paint-over.
- Layout, маршрут и HUD не изменены.
- Добавлены временные визуальные формы Седьмого круга, четырёх защитных
  конструкций, Детей Нижнего Змея, Нави и Серых.
- Подготовлен screenshot-композиционный reference для ImageGen.
- Два ImageGen-вызова (edit и independent generation) завершились сетевой
  ошибкой до рендера; генерацию mockup нужно повторить.

## TODO

- После пользовательского выбора усилить или ослабить картонную фактуру.
- Заменить CSS placeholders утверждёнными concept assets.
- Поднять размер и контраст ключевых башен относительно окружения.
- После утверждения направления подготовить atlas master prompt.

## 2026-07-24 — lore/mechanics integration

- Audited the actual `game/game.js` runtime.
- Documented genre, economy, worksites, regrowth, raid risk, two-road waves,
  Watchtower branches, hero charge and endless scaling in
  `docs/01_design/game-system-and-lore-integration-v1.md`.
- Wrote proposed canon `game-lore-bible-v6.md`.
- Wrote runtime/planned coverage in `entity-mechanics-codex-v5.md`.
- Rebuilt prompt language in `asset-prompt-bible-v6.md`,
  `world-concept-art-prompt-bible-v2.md`,
  `concept_art_call_plan_v2.json` and
  `layered_sprite_atlas_master_prompt_v2.md`.
- Found runtime/document drift: wave 1 is an all-entity debug showcase; old UI
  strings remain; the 15-mission campaign is not an implemented multi-map
  campaign; registered hero structures are not currently buildable.

## TODO after this integration

- Public title remains `Семь кругов Ирия`; `Семь дорог последнего узла` is a
  campaign subtitle, not a replacement title.
- Runtime text migration completed; user review of Lore Bible v6, display names
  and object descriptions remains the editorial gate.
- Generate and review C01–C07 concept art.
- Only then start the v2 atlas master prompt with Wind Watch.

## 2026-07-24 — runtime lore migration completed

- Перенесены в `game/index.html` и `game/game.js` канонические названия
  ресурсов, базовых форм, улучшений, героев, врагов, боссов, волн и действий.
- Первая отладочная волна со всеми типами врагов заменена стартовой tutorial
  волной из бегунов и ратников.
- Runtime IDs и баланс не переименовывались, поэтому существующая игровая логика
  и будущие manifest JSON сохраняют совместимость.
- `node --check game/game.js` пройден.
- Browser smoke test пройден: экран загрузился, кнопка `Открыть волну` работает,
  новая волна запускается.
- Наблюдаемые 404 относятся к отсутствующим production runtime atlas, которые
  намеренно не создаются до утверждения C01–C07.
- Watchtower source call plan прошёл технический валидатор: 14 упорядоченных
  ImageGen 2 вызовов.
- Удалена последняя активная ссылка restart pipeline на старый
  `asset-prompt-bible-v4.md`; production цепочка теперь замкнута на v6/v5.

## Current production gate

- Сгенерировать и проверить C01–C07.
- Получить подтверждение единого визуального направления.
- Затем собрать Watchtower по layered atlas master prompt v2 и остановиться на
  его visual + technical approval.

## 2026-07-24 — documentation-only hold

- По указанию пользователя остановлена любая генерация изображений.
- Создан единый текстовый отчёт
  `docs/00_project/complete-lore-gameplay-and-asset-report-v1.md`.
- В отчёт сведены мир, конфликт, сюжет, реальная TD-механика, экономика,
  персонажи, фракции, все runtime-постройки, ветви Watchtower, враги, боссы,
  карта, окружение, planned content, визуальные правила, слои и prompt pipeline.
- C01–C07 зафиксированы только текстом и не запускаются до отдельного решения
  пользователя.

## 2026-07-24 — full text consistency audit

- Перепроверена цепочка world → conflict → campaign → runtime mechanics →
  entities → visual rules → prompts → atlas contract.
- Активный `current-production-state.md` очищен от противоречащей истории
  Китеж/старого Watchtower pipeline.
- Исправлены устаревшие утверждения о debug wave 1 и старых UI-строках.
- Унифицированы display names runtime, naming map, entity codex, object spec и
  сводного отчёта.
- Исправлен roster count: 19 реализованных обычных врагов + 1 planned scout.
- Формально разделены Семь Дорог и Семь функциональных Кругов.
- Старый десятистраничный рассказ переведён в archival status из-за pre-v6
  персонажей и буквального Велеса.
- Добавлен `production-prompt-catalog-v1.md`: индивидуальные prompts для
  врагов, боссов, planned support, окружения, VFX и hero animation sources.
- Создан `lore-and-production-consistency-audit-v1.md` с итоговым PASS.

## 2026-07-24 — new-window concept-art handoff

- Подготовлен самодостаточный
  `assets/staging/prompts/new_window_game_concept_art_master_prompt_v1.md`.
- Prompt требует built-in ImageGen 2 и два gameplay-view concept art:
  C01 gameplay compatibility и C02 factions/capture.
- Встроены active-doc order, реальный layout reference, lore/material locks,
  точные output paths, QA-критерии, network-failure policy и stop condition.
- Prompt запрещает переход к sprite atlas и изменение HTML/CSS до человеческой
  проверки двух изображений.
