#!/bin/sh

install:
	sudo docker-compose build
	sudo docker-compose up -d
	sleep 4
	sudo docker container exec check_weather_ctn python manage.py migrate
	sudo docker container exec check_weather_ctn python manage.py createsuperuser --noinput
	sudo docker-compose stop

run:
	sudo docker-compose up -d

stop:
	sudo docker-compose stop

show_urls:
	sudo docker container exec check_weather_ctn python manage.py show_urls

tests:
	sudo docker container exec check_weather_ctn pytest core/tests.py

log:
	sudo docker container logs -f check_weather_ctn

clear:
	sudo docker-compose down -v

exec:
	 sudo docker container exec -it check_weather_ctn bash