# AllAuth Package
**allauth** provides simple way to use multiple authentication providers like like Google, Facebook and Git etc as an authenticator for your app.

## Installation
To install **allauth** on your machine, use below command.
```shell
pip install django-allauth
```

## Modification in your Project
In this section, we will discuss some of the changes that you have to make in your main project folder.

#### Modifications in `project\settings.py`
- allauth: It provides the core framework and utilities needed for the Allauth package to function. It includes common settings, utilities, and the base configuration required for the other Allauth modules to work together.
- allauth.account:  It focuses on user account management. This includes features like user registration, login, logout, password reset, email verification, and account settings. This module handles the core functionality related to user accounts, such as views, forms, and URLs for these actions.
- allauth.socialaccount: Enables social account authentication (e.g., via Facebook, Google)
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
    'django.contrib.auth.backends.ModelBackend',  # Default ModelBackend
    'allauth.account.auth_backends.AuthenticationBackend',  # Allauth authentication backend for social authentication
]
```

#### Changes in `urls.py`

It includes all the URL patterns provided by the Django Allauth package for handling user authentication and account management like:
- http://yourdomain.com/accounts/login/: Login page
- http://yourdomain.com/accounts/logout/: Logout page
- http://yourdomain.com/accounts/signup/: Signup page
- http://yourdomain.com/accounts/password/reset/: Password reset page

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