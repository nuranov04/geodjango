
            Добро пожаловать на мой django-project :)
    
    Это тестовое задание. Суть проекта заключается в том, 
    чтобы подлючить geodjango в админ панель. При запуске 
    с помощью докера автоматически в базу отправляется данные 
    о всех странах. 



Для того чтобы запустить проект вам необходимо выполнить следущие команды:

- git clone https://github.com/nuranov04/geodjango.git 
- cd geodjango
- docker compose build 
- docker compose up
- docker compose exec backend bash 
- cd backend/
- ./manage.py createsuperuser ( Вводите свои данные:) )
- ctrl+D

Наслаждайтесь, если возникнут какие-то вопросы можете писать на мой tg: @NuranovArtur или на linkedin: linkedin.com/in/arturnuranov/