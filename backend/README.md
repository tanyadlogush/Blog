# SkillUp course project

## Requirements
Application | version
----------- | -------
Python      | 3.8.3  
PostgreSQL  | 13.2-1  

## Installation
```bash
git clone git@github.com:tanyadlogush/skillup_python_course.git

# Go to the Django application folder
cd skillup_course/blog/backend/

# Install dependencies
pipenv install
# Activate virtual envirnonment
pipenv shell
```

## Run django project
```bash
# Make migrations
python manage.py migrate
# Run server
python manage.py runserver
```