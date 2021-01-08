Для запуска необходимо выполнить:
0. Установить зависимости из requirements.txt 
1. Создать файл .env и определить в нем следующие переменные: 
   * SECRET_KEY
   * DEBUG
   * PG_USER
   * PG_PASSWORD
   * PG_DB_NAME 
   * PG_HOST 
   * PG_PORT
2. Запустить БД: docker-compose --env-file .\cinemaFriday\cinemaFriday\.env up pg
3. Накатить миграции на бд: python manage.py migrate
4. Заполнить данные для примера: python manage.py upload_data_fb
5. Запустить сервирс: python manage.py runserver

<hr>
