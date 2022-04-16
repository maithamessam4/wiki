from django.urls import path

from . import views
app_name='wiki'
urlpatterns = [
    path('wiki/create/',views.create,name='create'),   
    path('entries/<str:title>',views.single_entry,name=('single-entry')),
    path("wiki/edit/<str:entry>/", views.edit, name="edit"),
    path("", views.index, name="index"),
]

#    path("edit", views.edit, name="edit"),
