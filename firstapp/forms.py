from django import forms
from .models import Client, Collective_contract, Employee_category, Company, Agent, Users


class DataClient(forms.Form):
    full_name = forms.CharField(label="Имя клиента")
    age = forms.IntegerField(label="Возраст")
    risk_category = forms.CharField(label="Категория риска")
    collective_contract_id = forms.ModelChoiceField(label="Коллективный контракт", queryset=Collective_contract.objects.all().order_by('id'))


class DataCollective_contract(forms.Form):
    term_of_the_contract = forms.IntegerField(label="Срок контракта")
    date_of_conclusion = forms.DateField(label="Дата заключения")
    employee_category_id = forms.ModelChoiceField(label="Категория сотрудника", queryset=Employee_category.objects.all().order_by('id'))
    payments_for_insured_events = forms.IntegerField(label="Выплата по страховым случаям")

class DataEmployee_category(forms.Form):
    number = forms.IntegerField(label="Номер")
    employee_full_name = forms.CharField(label="Имя сотрудника")
    employee_risk_category = forms.CharField(label="Категория риска сотрудника")

class DataCompany(forms.Form):
    code = forms.IntegerField(label="Код")
    full_name = forms.CharField(label="Полное название")
    short_title = forms.CharField(label="Аббревеатура")
    adress = forms.CharField(label="Адрес")
    bank_details = forms.IntegerField(label="Банковские реквизиты")
    company_specialization = forms.CharField(label="Специализация компании")
    collective_contract_id = forms.ModelChoiceField(label="Коллективный контракт", queryset=Collective_contract.objects.all().order_by('id'))

class DataAgent(forms.Form):
    full_name = forms.CharField(label="Имя агента")
    passport_data = forms.IntegerField(label="Данные паспорта")
    collective_contract_id = forms.ModelChoiceField(label="Коллективный контракт", queryset=Collective_contract.objects.all().order_by('id'))

class DataUsers(forms.Form):
    number = forms.CharField(label="Номер")
    name = forms.CharField(label="Имя пользователя")


