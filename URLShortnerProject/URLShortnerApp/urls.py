from django.urls import path, include
from . import views

urlpatterns = [
    path('shorten/', views.get_form, name='urlform'),
    path('<short_url>/', views.redirect_short_url, name='redirectpath'),
    #path('<slug:my_url>', views.redirect_short_url,name='redirectpath'),
]
