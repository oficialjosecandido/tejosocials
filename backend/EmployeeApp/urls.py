from django.conf.urls import url
from EmployeeApp import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^department/$', views.departmentApi),
    url(r'^department/([0-9]+)$', views.departmentApi),
    url(r'^employee/$', views.employeeApi),
    url(r'^profile/([0-9]+)$', views.detailEmployeeApi),
    url(r'^thisProfile/([0-9]+)$', views.getThisEmployeeApi),
    url(r'^SaveFile$', views.SaveFile),
    url(r'^role/([0-9]+)$', views.departmentEmployeeApi),
    url(r'^technologies/$', views.techsApi),
    url(r'^tech/([0-9]+)$', views.techEmployeeApi),
    url(r'^techReport/$', views.getTechReportApi),
    url(r'^softReport/$', views.getSoftReportApi),
    url(r'^chats/$', views.getChatsApi),
    url(r'^chatRead', views.markReadAPI),
    url(r'^reply', views.replyMessageAPI),
    url(r'^sendMessage', views.sendMessageAPI),

    url(r'^sendMessage/$', views.contactApi),
    url(r'^delete/$', views.contactApi),
    url(r'^newsletter/$', views.newsletterApi),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
