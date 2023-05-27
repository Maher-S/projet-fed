This is our semester project for the BDBI class of 2023. The project aims to enhance and develop our skills in web scraping. 
To run this project on Windows, make sure you have the following environment set up:

dependencies:
------------------
for scraping app:
Pip version 23.1.2
Python version 3.10.11
Scrapy version 2.9.0
Schedule Version: 1.2.0
mysqlclient Version: 2.1.1

for the web app:
Django version 3.2.19

shared for 2 apps:
MySQL version 8.0.33 for Win64


configurations and excution:
----------------------------
make sure that you created MySQL Database (using wampserver or any other tool)
DB name: Immo_offres
no need for any DB tables creation in this phase 

Run the project
-------------------
open the project's main directory in your IDE:

For the web app:

in the settings.py file make sure to add your database configurations
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'immo_offres',
        'USER': 'your username',
        'PASSWORD': 'your psswd',
        'HOST': 'hostname or IP',
        'PORT': 'Port value',
    }
}

Access the Immo_offres app directory in the terminal (main directory of the project)
Run the following command lines:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver
	Open your web browser and go to http://127.0.0.1:8000/ to access the app.


For the scraping app (Immo-Scraper):

open a new terminal and access the immo-scraper directory
	if you want to make the scraping process go automatically run the foloowing command (you can adjust the time scheduler in the script if you want)
	python tasks.py 
	The scraping process should now run continuously based on the scheduler's time lapse.

	if you want to run each spider seperatly use these commands:
	scrapy runspider Tayara.py
	scrapy runspider TunisieAnnonce.py
