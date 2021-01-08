<h1>GITLAB CI/CD </h1>

[![Coverage Status](https://coveralls.io/repos/gitlab/toropow/otus_dev_ci_gitlab/badge.svg?branch=HEAD)](https://coveralls.io/gitlab/toropow/otus_dev_ci_gitlab?branch=HEAD)
<hr>
Процесс CI/CD <br>
1. Запустить сервис для скачивания и установки контейра докер на локальном host (https://github.com/toropow/otus_webhook). <br> 
2. Запустить ngrok и обновить url в .gitlab-ci.yml <br>
3. Сделать commit в ветку main. Запустится gitlab ci. <br>
4. После установки и прогона тестов (+ покрытие в coveralls) докер-образ запушится (через docker in docker) в docker registry. <br> 
5. После пуша нового образа прозойдет обращение по API, и на локальном хосте запустится образ docker.  <br>


