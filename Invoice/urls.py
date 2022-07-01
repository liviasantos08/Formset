from django.contrib import admin
from django.urls import path
from nota import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Base.as_view(), name='base'),
    path('form/', views.Forms.as_view(), name='form'),
    path('invoice/', views.TestView.as_view(), name='invoice-list'),
    path('gera/<id>',  views.TestView.view_pdf, name='gerapdf'),

]
