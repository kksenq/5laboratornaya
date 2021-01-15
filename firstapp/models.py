from django.db import models
import datetime
# Create your models here.

class Client(models.Model):
    full_name = models.CharField(max_length=120)
    age = models.IntegerField()
    risk_category = models.CharField(max_length=120)
    collective_contract_id = models.ForeignKey('Collective_contract', on_delete=models.CASCADE)
    objects = models.Manager()

class Collective_contract(models.Model):
    term_of_the_contract = models.IntegerField()
    date_of_conclusion = models.DateField(default=datetime.date.today)
    employee_category_id = models.ForeignKey('Employee_category', on_delete=models.CASCADE)
    payments_for_insured_events = models.IntegerField()
    objects = models.Manager()

class Employee_category(models.Model):
    number = models.IntegerField()
    employee_full_name = models.CharField(max_length=120)
    employee_risk_category = models.CharField(max_length=120)
    objects = models.Manager()

class Company(models.Model):
    code = models.IntegerField()
    full_name = models.CharField(max_length=120)
    short_title = models.CharField(max_length=120)
    adress = models.CharField(max_length=120)
    bank_details = models.IntegerField()
    company_specialization = models.CharField(max_length=120)
    collective_contract_id = models.ForeignKey('Collective_contract', on_delete=models.CASCADE)
    objects = models.Manager()

class Agent(models.Model):
    full_name = models.CharField(max_length=120)
    passport_data = models.IntegerField()
    collective_contract_id = models.ForeignKey('Collective_contract', on_delete=models.CASCADE)
    objects = models.Manager()

class Users(models.Model):
    name = models.CharField(max_length=120)
    number = models.CharField(max_length=120)
    objects = models.Manager()