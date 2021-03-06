# Сети петри

- Сеть Петри выполняется посредством запусков переходов.
- Запуск перехода управляется фишками в его входных
позициях и сопровождается удалением фишек из этих
позиций и добавлением новых фишек в его выходные
позиции.
- Переход может запускаться только в том случае, когда он
разрешен.
- Переход называется разрешенным, если каждая из его
входных позиций содержит число фишек, не меньшее, чем
число дуг, ведущих из этой позиции в переход (или
кратности входной дуги).
- Разрешённые переходы можно запускать в произвольном
порядке

## Переходы

- `#ˆ: T × P → N0`
- `# ˆ(t, p)` – кратность дуги из t в p
- `ˆ# : P × T → N0`
- `ˆ# (p, t)` – кратность дуги из p в t
- `N0` – множество натуральных чисел и 0
- `q(p)` – число фишек в позиции p

- Переход t разрешён если ∀p ∈ I(t) справедливо
q(p) ≥ ˆ# (p, t)
- Запуск перехода
q
0
(p) = q(p) −ˆ# (p, t) + # ˆ(t, p)
- Сеть можно запускать до тех пор, пока в ней есть
разрешённые переходы
- Порядок запуска переходов не определён
