# django-g

> **Warning**
> AFAIK this project is not in production anywhere, even at Buser. It is a work in progress.

Django global context to get current request from anywhere in your application.

Many scenarios need the current request but Django don't have it accessible.
They expect that your application implement a middleware to use the request,
but it is burdensome and not reusable.

Other packages, like [django-threadlocals](https://pypi.org/project/django-threadlocals/) do the same thing with threadlocals, but it doesn't work on the
async world.

## How to install

```
$ pip install django-g
```

## How to use

Add `django_g.middleware.RequestMiddleware` to your settings `MIDDLEWARE`. It
is a small middleware just to capture the current request and save to global
context, ordering probably doesn't matter because any other middleware
already have access to the request.

```python
MIDDLEWARE = [
    "django_g.middleware.RequestMiddleware",
    ...
]
```


```python
from django_g import get_current_request


def your_func():
    request = get_current_request()
    # Use the request here. Be careful and handle when `request=None`.
```

**protip** It is not a good idea to get the request everywhere, because you're
coupling the framework specifics with your logic, so use this package only to
get the request where you don't have a better way.
