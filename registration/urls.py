from django.conf.urls.defaults import *
from django.contrib.auth import views as auth_views
from views import register_common_user, register_company_user, confirmation
from forms import LoginForm

urlpatterns = patterns('',
    url(r'^registrarse/$',
        register_common_user,
        {'template_name': 'registration/register_user.html'},
        name='register_common_user'),
#    url(r'^empresa/$',
#        register_company_user,
#        {'template_name': 'registration/register_company.html'},
#        name='register_company_user'),
    url(r'^confirmacion/(?P<activation_key>[a-f0-9]{32})/$',
        confirmation,
        {'template_name': 'registration/confirmation.html'},
        name='confirmation'),
    url(r'^ingresar/$',
        auth_views.login,
        {'template_name': 'registration/login.html',
         'authentication_form': LoginForm},
        name='login'),
    url(r'^salir/$',
        auth_views.logout,
        {'template_name': 'registration/logout.html'},
        name='logout'),
    url(r'^password/change/$',
        auth_views.password_change,
        name='auth_password_change'),
    url(r'^password/change/done/$',
        auth_views.password_change_done,
        name='auth_password_change_done'),
    url(r'^password/reset/$',
        auth_views.password_reset,
        name='auth_password_reset'),
    url(r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.password_reset_confirm,
        name='auth_password_reset_confirm'),
    url(r'^password/reset/complete/$',
        auth_views.password_reset_complete,
        name='auth_password_reset_complete'),
    url(r'^password/reset/done/$',
        auth_views.password_reset_done,
        name='auth_password_reset_done'),
)
