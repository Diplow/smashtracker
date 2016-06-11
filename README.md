# Smash Tracker (ST)

## Purpose

ST enables you to easily track Super Smash Bros results among people of your company.

ST focuses on storing and formating games and users data for effecient processing from data visualization tools like Artefact's Inisghts.


## Setup

*require python 2.7 for running*
```
export PYTHONPATH=$PYTHONPATH:**PROJECT_HOME**/tracker
pip install -r tracker/requirements.txt
python tracker/manage.py makemigrations tracker
python tracker/manage.py migrate
python tracker/manage.py createsuperuser
python tracker/manage.py runserver
```

Your server is running on localhost:8000


## API

### /admin

Add your company's people with the django admin interface.

### /newgame

Save a game in your database

### /exportgames

Download the list of your games to json format.

### /exportusers

Download the list of your users to json format.
