# CHAT Application

## Run a redis server first
```
$ docker run -p 6379:6379 -d redis:5
```
    Pre-requiresites :
        Docker should be installed.

## Testing whether the redis server is working or not
```
$ python3 manage.py shell
>>> import channels.layers
>>> channel_layer = channels.layers.get_channel_layer()
>>> from asgiref.sync import async_to_sync
>>> async_to_sync(channel_layer.send)('test_channel', {'type': 'hello'})
>>> async_to_sync(channel_layer.receive)('test_channel')
{'type': 'hello'}
```

## Testing the application
```
$ python manage.py test main.tests
```
    Pre-requisites : 
        Make sure you have chrome driver installed before testing.
        https://sites.google.com/a/chromium.org/chromedriver/home
# References :
- https://channels.readthedocs.io/en/stable/tutorial/part_2.html