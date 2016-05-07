# remainderApp
Remainder application developed using django 1.8

# Stack
1. Django 1.8
2. celery
3. redis
4. timezone_field
5. django_forms_bootstrap
6. css date time picker.
7. arrow.

#### Send REST api request to `http://localhost:8000/appointments/jsonnew`

Example POST request:
    
    `{
    "email":"madhusudhan638@gmail.com",
    
    "message":"aweseome it is",
    
    "time":"2016-05-07 23:57:00"
    }`

# Models:
`class Appointement(models.Model):`

    email = models.EmailField()
    message = models.TextField()
    time = models.DateTimeField()
    timezone = TimeZoneField(default='Asia/Kolkata')`
    
# How to run it locally

1. Clone the repo
2. Go to remainderApp branch
3. Create a virtual environment using `mkvirtualenv <virtualenvname>`
4. Activate the virtual environment using `workon <virtualenvname>`
5. Run the following command: `pip install -r requirements.txt`.
6. Open `remainderApp/settings.py` file and fill in the values for `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD`.
7. Run the following command to migrate the DB, `python manage.py migrate`.
8. Start the redis server using `redis-server`.
9. Start the app using `python manage.py runserver`
10. Run the celery workers using `celeryd --app remainderApp.celery -l info`
11. Go to `localhost:8000/`.

    

