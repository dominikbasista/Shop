from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from accounts import views

app_name = 'accounts'

urlpatterns = [

    path('sign-up', views.sign_up, name='sign_up'),
    path('login', views.login, name='login'),
    path('account-settings/<int:id>', views.account_settings, name='account_settings'),
    path('account-settings/<int:id>/history', views.account_history, name='account_history'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)