from django.contrib import admin
from django.shortcuts import redirect
from django_otp import user_has_device
from django.urls import reverse

class OTPRequiredAdminSite(admin.AdminSite):
    def has_permission(self, request):
        # Must be logged in AND have 2FA verified
        if not super().has_permission(request):
            return False
        # If user has no device registered, redirect to setup
        if not user_has_device(request.user):
            return False
        return request.user.is_verified()  # OTP must be verified this session
    
    def login(self, request, extra_context=None):
        # Redirect to 2FA setup if no device registered
        if request.user.is_authenticated and not user_has_device(request.user):
            return redirect(reverse('two_factor:setup'))
        return super().login(request, extra_context)

admin.site.__class__ = OTPRequiredAdminSite
