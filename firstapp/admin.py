from django.contrib import admin
from .models import Client, Collective_contract, Employee_category, Collective_contract, Company, Agent, Users, Backup_copy
# Register your models here.

@admin.register(Collective_contract)
class Collective_contractAdmin(admin.ModelAdmin):
    list_display = ('term_of_the_contract','date_of_conclusion','payments_for_insured_events')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name','age','risk_category')

@admin.register(Employee_category)
class Employee_categoryAdmin(admin.ModelAdmin):
    list_display = ('number','employee_full_name','employee_risk_category', 'agent_id')

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('code','full_name','short_title','adress','bank_details', 'company_specialization')

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('full_name','passport_data')


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('name','login', 'password')

@admin.register(Backup_copy)
class Backup_copyAdmin(admin.ModelAdmin):
    list_display = ('name','number')