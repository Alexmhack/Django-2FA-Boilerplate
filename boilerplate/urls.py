from django.contrib import admin
from django.urls import path, include

from two_factor.urls import urlpatterns as tf_urls

from two_factor.admin import AdminSiteOTPRequired
from django_otp.admin import OTPAdminSite
from two_factor.gateways.twilio.urls import urlpatterns as tf_twilio_urls

# admin.site.__class__ = AdminSiteOTPRequired
admin.site.__class__ = OTPAdminSite

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(tf_urls)),
    path('', include(tf_twilio_urls)),
]
