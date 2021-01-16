
from django.contrib import admin
from django.urls import path
from firstapp import views
from django.conf.urls import include, url
from django.views.generic import RedirectView

admin.autodiscover()

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='accounts/login/')),
    url(r'^admin/backups/', include('dbbackup_ui.urls')),
    url(r'^admin/', admin.site.urls),
    path('home/', views.index, name='home'),


    # добавление клиента
    path('home/Client/', views.index_client, name='Client'),
    path('home/Client/add/', views.view_Client.add_Client, name ='add_Client'),
    path('home/Client/del/', views.view_Client.del_Client, name ='del_Client'),
    path('home/Client/update/', views.view_Client.update_Client, name ='update_Client'),

    # добавление категории сотрудника
    path('home/Employee_category/', views.index_employee_category, name='Employee_category'),
    path('home/Employee_category/add/', views.view_Employee_category.add_Employee_category, name='add_Employee_category'),
    path('home/Employee_category/del/', views.view_Employee_category.del_Employee_category, name='del_Employee_category'),
    path('home/Employee_category/update/', views.view_Employee_category.update_Employee_category, name='update_Employee_category'),

    # добавление категории сотрудника
    path('home/Collective_contract/', views.index_Collective_contract, name='Collective_contract'),
    path('home/Collective_contract/add/', views.view_Collective_contract.add_Collective_contract, name='add_Collective_contract'),
    path('home/Collective_contract/del/', views.view_Collective_contract.del_Collective_contract, name='del_Collective_contract'),
    path('home/Collective_contract/update/', views.view_Collective_contract.update_Collective_contract, name='update_Collective_contract'),

    # добавление компании
    path('home/Company/', views.index_Company, name='Company'),
    path('home/Company/add/', views.view_Company.add_Company, name='add_Company'),
    path('home/Company/del/', views.view_Company.del_Company, name='del_Company'),
    path('home/Company/update/', views.view_Company.update_Company, name='update_Company'),

    # добавление агента
    path('home/Agent/', views.index_Agent, name='Agent'),
    path('home/Agent/add/', views.view_Agent.add_Agent, name='add_Agent'),
    path('home/Agent/del/', views.view_Agent.del_Agent, name='del_Agent'),
    path('home/Agent/update/', views.view_Agent.update_Agent, name='update_Agent'),

    # добавление пользователя
    path('home/Users/', views.index_Users, name='Users'),
    path('home/Users/add/', views.view_Users.add_Users, name='add_Users'),
    path('home/Users/del/', views.view_Users.del_Users, name='del_Users'),
    path('home/Users/update/', views.view_Users.update_Users, name='update_Users'),

    # добавление пользователя
    path('home/Backup_copy/', views.index_Backup_copy, name='Backup_copy'),
    path('home/Backup_copy/add/', views.view_Backup_copy.add_Backup_copy, name='add_Backup_copy'),
    path('home/Backup_copy/del/', views.view_Backup_copy.del_Backup_copy, name='del_Backup_copy'),
    path('home/Backup_copy/update/', views.view_Backup_copy.update_Backup_copy, name='update_Backup_copy'),

]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]