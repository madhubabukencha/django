# AllAuth Package
**allauth** package provides away to use social apps like Google, Facebook etc as authenticator..,

## Installation
You can installation allauth package using pip
```shell
pip install django-allauth
```

## Modification in your Project
Modification in `project\settings.py`
```python
INSTALLED_APPS = [
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
]

MIDDLEWARE = [
    "allauth.account.middleware.AccountMiddleware",
]

AUTHENTICATION_BACKEND = [
    'django.contrib.auth.backends.ModelBackend'
]

# Setting email console for testing. You can set you 
# your real email details
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
```

Changes in `urls.py`
```python
from django.urls import path, include

urlpatterns = [
    path("accounts/", include("allauth.urls"))
]
```

## References
- https://www.youtube.com/watch?v=mIlgzn2zuFE
- https://studygyaan.com/django/how-to-add-gmail-log-in-in-django
- https://studygyaan.com/django/add-facebook-login-to-django-website-using-django-allauth