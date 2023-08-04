from django.urls import path
from .views import index, advertisement, advertisement_post, register, profile, login,top_sellers 

urlpatterns = [
    path('', index, name = "home"),
    path('advertisement_post/', advertisement_post, name = "advp"),
    path('advertisement/', advertisement, name = "adv"),
    path('login/', login, name = "log"),
    path('profile/', profile, name = "prof"),
    path('register/', register, name = "reg"),
    path('top_sellers/', top_sellers, name = "sel")      

]