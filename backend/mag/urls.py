from django.conf.urls import url
from mag import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^sendMessage/$', views.contactApi),
    url(r'^getPosts/$', views.getPostsAPI),
    url(r'^getPosts/(<key:key>)$', views.getPostsThisAPI),
    url(r'^post/(<slug:slug>)$', views.getThisPostAPI),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
