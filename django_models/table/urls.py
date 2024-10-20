from django.urls import path
from . import views

urlpatterns = [
    path('ofv/<str:FromObject>', views.FormView, name='order_url'),
    path('sv/<str:modelObject>', views.ShowView, name='show_url'),
    path('up/<str:modelObject>/<str:FromObject>/<int:f_oid>', views.ShowView, name= 'update_url'),
    path('del/<str:modelObject>/<int:f_oid>', views.deleteView, name= 'delete_url'),
]