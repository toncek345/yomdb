# yomdb

Your own movie database

### Quick start
Before starting make sure you have installed python(3.6), pip, virtualenv, virtualenvwrapper and postgres.

* Clone repo from github:
```
https://github.com/toncek345/yomdb
```

* Make virtual environment:
```
mkvirtualenv -p /usr/bin/python3.6 yomdb
```

* Make yomdb database in postgres

* Switch to new virtual environment:
```
workon yomdb
cd yomdb/
```

* Fetch dependencies:
```
pip install -r requirements
```

* Migrate database:
```
python manage.py migrate
```

In order for app to work you need to have omdb api key.
You can get it for free (1000 daily requests) from: [omdapi](http://www.omdbapi.com/apikey.aspx)
Put the api key in settings file yomdb/settings under empty string.

### Database

Database is accessed only locally (default port) and it is using default username and password (postgres superuser).
