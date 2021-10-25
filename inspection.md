# **Инспекция кода**
**Инспекция кода** (англ. *code inspection*) или **рецензирование кода, обзор кода, ревизия кода** (англ. *code review*) — систематическая проверка исходного кода программы. 

>**Задача**: улучшение качества ПО путем обнаружения и исправления ошибок, допущенных при его разработке, а также совершенствование навыков разработчика.

В процессе инспекции кода могут быть найдены и устранены такие проблемы, как: 
- ошибки в форматировании строк; 
- состояние гонки;
- утечка памяти;
- переполнение буфера.

К очевидным плюсам этой практики можно отнести:
- улучшение качества кода;
- нахождение «глупых» ошибок (опечаток) в реализации;
- повышение степени совместного владения кодом;
- приведение кода к единому стилю написания;
- получение нового опыта, обмен знаниями и т.д.

## **Что можно инспектировать**

Для ревью подходит любой код. Однако, review **обязательно** должно проводиться для критических мест в приложении, таких как: 
1. механизмы аутентификации
2. механизмы авторизации
3. механизмы передачи и обработки ценной информации (денежных транзакций и пр.)

Также для review подходят и юнит-тесты, поскольку их код также подвержен ошибкам.
**Неправильный тест может стоить очень дорого.**

## **На что смотреть во время инспекции**
### Архитектура/Дизайн
- **Принцип «одной ответственности».** Идея в том, что у каждого класса должно быть только одно назначение, что применимо также и к методам. *Если возникает нужда в союзе «и» при описании того, что делает метод, то стоит разделить его на несколько более простых.*


- **Принцип «Открыт/Закрыт».** Если язык объектно-ориентированный, убедитесь открыты ли ваши объекты для расширения, но закрыты для модификации.


- **Дупликация кода.** При повторении одного и того же куска кода 3 или более раз, необходимо вынести его в отдельный метод.


- **Поиск багов.** Просматривайте код на наличие ошибок-на-единицу, нарушений условий циклов и т.д.


- **Эффективность.** Проверяйте, эффективна ли реализация какого-либо алгоритма.

### Стиль

- **Имена методов.** Давать имена различным вещам — одна из самых сложных задач в программировании. Если метод называется ```get_message_queue_name()```, но делает что-то кроме этого, например, убирает HTML из входных данных, тогда это имя не подходит ему.

- **Имена переменных.** Будьте как можно лаконичнее и выбирайте говорящие имена переменных, которые облегчат чтение кода в будущем.

- **Длина классов**. Классы должны быть меньше 300 строк, а в идеале — меньше 100. Скорее всего, если в вашем коде есть длинные классы, то их можно разбить на несколько, что облегчит понимание их предназначения.

- **Длина файла**. Для Python 1000 строк в одном файле — предел. Возможно, стоит разбить файл на несколько, улучшить читабельность кода.

- **Документация.** Сложные методы лучше задокументировать так, чтобы было понятно, за что отвечает каждый аргумент.

### Тестирование

- **Полнота тестов**. Необходимо продумывать тесты так, чтобы можно было в полной мере оценить возможности и недостатки кода. (Могут ли они заставить ваш код упасть? Легко ли они читаются? Насколько они хрупки?)

- **Тестирование на правильном уровне**. Нужно убедиться, тестируется ли тот уровень приложения, который нужно тестировать для проверки функциональности. Гарри Бернардт рекомендует такое соотношение — 95% юнит-тестов и 5% интеграционных тестов.

- **Количество объектов-имитаций.** Если в тесте более трех имитационных объектов, нужно его переписать.

- **Соответствование требованиям.** Если тест не соответствует каким-то критериям, то лучше провести тестирование заново.

## **Как проводить инспектирование кода**

- **Задавайте вопросы.** Задавайте вопросы, которые подтолкнут разработчиков к обсуждению. Например, как работает этот метод? Если изменится какое-то требование, то что нужно будет поменять в коде? Как сделать код более поддерживаемым?

- **Делайте комплименты и поощрения.** Одна из самых важных вещей в тестировании — награждение разработчиков за рост и приложение усилий. 

- **Обсуждайте детали наедине.** Большие архитектурные изменения лучше обсуждать всей командой, в то время как про мелкие детали лучше говорить наедине с разработчиком, который ответственен за них, дабы не вовлекать лишних людей.

- **Объясняйте причины.** Всегда лучше рассказать или спросить, почему предложенные изменения необходимы. Порой может возникнуть чувство, что они несущественны, до тех пор, пока вы не объясните повод.

- **Дело в коде.** Обсуждайте сам код, а не разработчиков, которые его писали. Это создаcт непринужденную атмосферу, тем более, программисты ни при чем — инспектирование призвано улучшить качество кода.

- **Указывайте на важность изменений.** Если вы считаете, что ваше предложение важно, то стоит сказать об этом, тогда на него обратят внимание и быстрее начнут двигаться в нужном направлении, что создаст видимость результата.

**Источники:**

1. https://habr.com/ru/post/142564/#comments
2. https://ru.wikipedia.org/wiki/Просмотр_кода
3. https://tproger.ru/translations/code-review-best-practices/ 