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

## References
https://www.youtube.com/watch?v=mIlgzn2zuFE