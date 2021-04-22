from django.urls import path
from.import views

urlpatterns=[
    path('',views.index, name='index'),

    path('new',views.addShow, name='addShow'),

    path('create',views.createShow, name='createShow'),

    path('<int:showId>/edit',views.editShow),

    path('<int:showId>',views.displayShow),

    path('<int:showId>/destroy',views.destroyShow),

    path('<int:showId>/update', views.updateShow, name="updateShow"),


    path('<url>',views.catch_all),

]