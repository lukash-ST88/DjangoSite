from django.urls import path, re_path
from .views import *
from django.views.decorators.cache import cache_page # cache_page is a decorator

# adding cache this way: path('', cache_page(60)(WomenHome.as_view()), name='home') cahce for 60 seconds
urlpatterns = [
    path('', WomenHome.as_view(), name='home'), # as_view() calls the class of view
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'),
]
