# matboj

## Installation

* [Python 3](https://www.python.org/downloads/) (recommended: add Python to PATH)
* *virtualenv* and *virtualenvwrapper*

        pip install virtualenvwrapper-win
    
    Create a virtual environment
    
        mkvirtualenv matboj
    
    To later activate the environment, use
    
        workon matboj

* Django 1.8

        pip install Django==1.8

* Other required modules

        pip install django-debug-toolbar

## Usage

    python manage.py runserver 0.0.0.0:80
    
### Administration

With your browser, access the administration at `localhost:80/admin`.

The default login credentials are username: `admin` password: `admin`

### Matboje

Access the list at `localhost:80/matboje`
