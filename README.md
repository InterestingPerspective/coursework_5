        РАБОТА С БД КОМПАНИЙ HEADHUNTER'A И ИХ ВАКАНСИЙ

1. Для начала нужно установить библиотеку psycopg2 с помощью команды в терминале: "pip install psycopg2".
2. Создать БД с помощью pgAdmin.
3. Поочерёдно выполнить 2 скрипта из файлов: create_tables.py и fill_db.py, сперва изменив параметры подключения (database, user, password).
4. В файле data_selection.py на 4-й строке изменить параметры подключения к БД (database, user, password). С 7-й по 11-ю строки методы для выбирания данных из БД. Их поочерёдно нужно расскоменчивать (удалять и добавлять "#").
5. В файле funcs_for_db можно менять параметры для парсинга в функциях: get_employers() ("text"), choose_employers() (изменить диапазон количества вакансий на компанию и количество выбранных компаний).
