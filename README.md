# Django-2FA-Boilerplate
A simple boilerplate django project implementing the 2 Factor Autentication for Django Admin and Users

`pip install django-two-factor-auth pillow`


**settings.py**
```
INSTALLED_APPS = [
	...

    'django_otp',
    'django_otp.plugins.otp_static',
    'django_otp.plugins.otp_totp',
    'two_factor',
]
```

```
MIDDLEWARE = [
    # Include for twilio gateway
    'two_factor.middleware.threadlocals.ThreadLocals',
]
```

```
TWO_FACTOR_QR_FACTORY = 'qrcode.image.pil.PilImage'

PHONENUMBER_DEFAULT_REGION = 'IN'

TWO_FACTOR_PATCH_ADMIN = False

OTP_TOTP_ISSUER = 'Awesome Inc.'
```

**urls.py**

```
...
from two_factor.urls import urlpatterns as tf_urls

from django_otp.admin import OTPAdminSite

admin.site.__class__ = OTPAdminSite

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(tf_urls)),
]
```

Run migrations and server and register a new user.
