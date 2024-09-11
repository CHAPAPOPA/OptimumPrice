# Real Estate Scraper

## Описание

Данный проект представляет собой парсер, разработанный с использованием фреймворка Scrapy, для сбора данных о новостройках с сайта [наш.дом.рф](https://наш.дом.рф). Основной задачей парсера является сбор данных с карточек объектов недвижимости и детализированная информация внутри каждого объявления.

## Текущая реализация

На данный момент парсер может:
- Инициализировать запрос на стартовую страницу каталога новостроек.
- Собрать базовую информацию о недвижимости: название жилого комплекса, адрес, ID объявления, дату ввода в эксплуатацию и застройщика.

## Планируемые улучшения

1. **Обработка динамической подгрузки данных**: На сайте используется кнопка "Показать еще", которая динамически загружает дополнительные результаты. В текущей реализации отсутствует полноценная обработка этой функциональности.
   
2. **Парсинг дополнительных данных**: Планируется добавить сбор детализированных данных внутри каждого объявления, таких как:
   - Группа компаний.
   - Дата публикации проекта.
   - Дата выдачи ключей.
   - Средняя цена за 1 м².
   - Процент распроданных квартир.
   - Класс недвижимости.
   - Количество квартир.
   
3. **Использование внутренних API**: В текущей версии запросы направляются на статические страницы сайта. Для более стабильной и точной работы планируется изучить возможность использования внутренних API сайта.

4. **Обработка ошибок**: Будет добавлена обработка ошибок для предотвращения сбоев при недоступности сайта или неправильной работе кнопки "Показать еще".

5. **Сохранение данных**: Реализовано сохранение данных в формате JSON. В дальнейшем можно добавить возможность выбора формата (CSV, JSON) и расширить список сохраняемых полей.

## Запуск проекта

1. Установите все необходимые зависимости:
    ```bash
    pip install -r requirements.txt
    ```

2. Запустите паука:
    ```bash
    scrapy crawl real_estate_spider
    ```

## Возможные улучшения

- Расширение функционала для работы с динамическими страницами с использованием JavaScript.
- Улучшение производительности и скорости парсинга.
- Добавление автотестов для верификации правильности сбора данных.

## Примечание

Проект находится в стадии разработки. Некоторые функции могут быть не полностью реализованы.
