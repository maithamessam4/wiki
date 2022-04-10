from django.urls import path

from . import views
app_name='wiki'
urlpatterns = [
    path('wiki/create/',views.create,name="create"),   
    path('entries/<str:title>',views.single_entery,name=('single-entery')),
    path('wiki/edit/<str:title>/',views.edit,name="edit"),
    path("", views.index, name="index")
]
