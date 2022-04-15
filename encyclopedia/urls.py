from django.urls import path

from . import views
app_name='wiki'
urlpatterns = [
    path('wiki/create/',views.create,name='create'),   
    path('entries/<str:title>',views.single_entry,name=('single-entry')),
    path('wiki',views.random,name='random'),
    path('wiki/edit',views.edit,name='edit'),
    path("", views.index, name="index")
]
