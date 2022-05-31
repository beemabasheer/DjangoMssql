from django.contrib import admin
from django.urls import path
from SalesTeam import views

urlpatterns = [
    path('sales/list/', views.SalesList.as_view()),
    path('sales/create', views.SalesCreate.as_view()),
    path('add',views.SalesTeamFormView.as_view(),
        name='sales.team.add'),
    path('edit/<int:id>/',views.SalesTeamFormView.as_view(),
         name='sales-team.edit'),
    path('', views.sales_team_view,name='sales.team.list'),



  



]
