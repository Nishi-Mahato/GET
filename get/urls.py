"""get URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path, re_path
# from django.contrib.auth import views
from django.contrib.auth.views import LoginView, LogoutView,PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeDoneView, PasswordChangeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tms.urls',namespace='tms')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('payment/', include('payment.urls', namespace='payment')),
    # url(r'^accounts/login/$', LoginView.as_view(template_name='registration/login.html'), name="login"),
    # url(r'^accounts/logout/$', LogoutView.as_view(), LogoutView.next_page, name="logout"),
    # url(r'^accounts/login/$', views.login, name='login'),
    # url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),

    re_path(r'^accounts/login/$', LoginView.as_view(template_name='registration/login.html'), name="login"),
    re_path(r'^accounts/logout/$', LogoutView.as_view(template_name='registration/logout.html'), LogoutView.next_page, name="logout"),
    re_path(r'^accounts/password/reset/$', PasswordResetView.as_view(template_name='registration/password_reset_page.html'), name='password_reset'),
    re_path(r'^accounts/password/reset/done/$', PasswordResetDoneView.as_view(template_name='registration/passwordreset_pagedone.html'), name='password_reset_done'),
    re_path( r'^accounts/password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirmpage.html'), name='password_reset_confirm'),
    re_path(r'^accounts/password/reset/complete/$', PasswordResetCompleteView.as_view(template_name='registration/password_reset_completepage.html'), name='password_reset_complete'),
    re_path(r'^accounts/password/change/$', PasswordChangeView.as_view(template_name='registration/change-password.html'), name='password_change'),
    re_path(r'^accounts/password/change/done/$', PasswordChangeDoneView.as_view(template_name='registration/change-password-done.html'), name='password_change_done'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)