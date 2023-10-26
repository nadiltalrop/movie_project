from django.urls import path

from. import views


app_name ='movie'

urlpatterns = [
    path('',views.index,name='index'),
    path('movie/<int:id>/',views.detail,name="detail"),
    path('add-movie/',views.add_movie,name='add_movie'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]

