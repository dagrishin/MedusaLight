# MedusaLight
#### 0) Файл .env.dev положить в корень
#### 1) Создать образ и запустить контейнер

    docker-compose up --build
##### 2) Создать супер юзера

    docker exec -it medusa_light_web bash
    python manage.py createsuperuser
##### 3) Перейти по адресу

    http://localhost/admin/ админка
    http://localhost/swagger/ свагер