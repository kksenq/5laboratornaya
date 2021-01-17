from django.test import TestCase
import unittest
from .models import Client, Collective_contract, Employee_category, Collective_contract, Company, Agent, Users, Backup_copy

class ClientModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Client.objects.create(full_name='Иванов И.И.', age='20', risk_category='sdtgh', collective_contract_id='1')

    def test_full_name_label(self):
        ad = Client.objects.get(id=1)
        field_label = ad._meta.get_field('full_name').verbose_name
        self.assertEquals(field_label, 'full_name')

    def test_age_label(self):
        ad = Client.objects.get(id=1)
        field_label = ad._meta.get_field('age').verbose_name
        self.assertEquals(field_label, 'age')

    def test_risk_category_label(self):
        ad = Client.objects.get(id=1)
        field_label = ad._meta.get_field('risk_category').verbose_name
        self.assertEquals(field_label, 'risk_category')

    def test_collective_contract_id_label(self):
        ad = Client.objects.get(id=1)
        field_label = ad._meta.get_field('collective_contract_id').verbose_name
        self.assertEquals(field_label, 'collective_contract_id')

class Collective_contractModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Collective_contract.objects.create(term_of_the_contract='3', date_of_conclusion='2018-05-22', employee_category_id='1', payments_for_insured_events='2334')

    def test_term_of_the_contract_label(self):
        ad = Collective_contract.objects.get(id=1)
        field_label = ad._meta.get_field('term_of_the_contract').verbose_name
        self.assertEquals(field_label, 'term_of_the_contract')

    def test_date_of_conclusion_label(self):
        ad = Collective_contract.objects.get(id=1)
        field_label = ad._meta.get_field('date_of_conclusion').verbose_name
        self.assertEquals(field_label, 'date_of_conclusion')

    def test_employee_category_id_label(self):
        ad = Collective_contract.objects.get(id=1)
        field_label = ad._meta.get_field('employee_category_id').verbose_name
        self.assertEquals(field_label, 'employee_category_id')

    def test_payments_for_insured_events_label(self):
        ad = Collective_contract.objects.get(id=1)
        field_label = ad._meta.get_field('payments_for_insured_events').verbose_name
        self.assertEquals(field_label, 'payments_for_insured_events')

class Employee_categoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Employee_category.objects.create(number='3', employee_full_name='sdfrgh', employee_risk_category='1', agent_id='1')

    def test_number_label(self):
        ad = Employee_category.objects.get(id=1)
        field_label = ad._meta.get_field('number').verbose_name
        self.assertEquals(field_label, 'number')

    def test_employee_full_name_label(self):
        ad = Employee_category.objects.get(id=1)
        field_label = ad._meta.get_field('employee_full_name').verbose_name
        self.assertEquals(field_label, 'employee_full_name')

    def test_employee_risk_category_label(self):
        ad = Employee_category.objects.get(id=1)
        field_label = ad._meta.get_field('employee_risk_category').verbose_name
        self.assertEquals(field_label, 'employee_risk_category')

    def test_agent_id_label(self):
        ad = Employee_category.objects.get(id=1)
        field_label = ad._meta.get_field('agent_id').verbose_name
        self.assertEquals(field_label, 'agent_id')

class CompanyModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Company.objects.create(code='3', full_name='sdfrgh', short_title='sdefgthy', adress='1sdfg', bank_details='1', company_specialization='fghj', collective_contract_id='1')

    def test_number_label(self):
        ad = Company.objects.get(id=1)
        field_label = ad._meta.get_field('code').verbose_name
        self.assertEquals(field_label, 'code')

    def test_full_name_label(self):
        ad = Company.objects.get(id=1)
        field_label = ad._meta.get_field('full_name').verbose_name
        self.assertEquals(field_label, 'full_name')

    def test_short_title_label(self):
        ad = Company.objects.get(id=1)
        field_label = ad._meta.get_field('short_title').verbose_name
        self.assertEquals(field_label, 'short_title')

    def test_adress_label(self):
        ad = Company.objects.get(id=1)
        field_label = ad._meta.get_field('adress').verbose_name
        self.assertEquals(field_label, 'adress')

    def test_bank_details_label(self):
        ad = Company.objects.get(id=1)
        field_label = ad._meta.get_field('bank_details').verbose_name
        self.assertEquals(field_label, 'bank_details')

    def test_company_specialization_label(self):
        ad = Company.objects.get(id=1)
        field_label = ad._meta.get_field('company_specialization').verbose_name
        self.assertEquals(field_label, 'company_specialization')

    def test_collective_contract_id_label(self):
        ad = Company.objects.get(id=1)
        field_label = ad._meta.get_field('collective_contract_id').verbose_name
        self.assertEquals(field_label, 'collective_contract_id')

class AgentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Agent.objects.create(full_name='dfgyu', passport_data='345678', collective_contract_id='1')

    def test_full_name_label(self):
        ad = Agent.objects.get(id=1)
        field_label = ad._meta.get_field('full_name').verbose_name
        self.assertEquals(field_label, 'full_name')

    def test_passport_data_label(self):
        ad = Agent.objects.get(id=1)
        field_label = ad._meta.get_field('passport_data').verbose_name
        self.assertEquals(field_label, 'passport_data')

    def test_collective_contract_id_label(self):
        ad = Agent.objects.get(id=1)
        field_label = ad._meta.get_field('collective_contract_id').verbose_name
        self.assertEquals(field_label, 'collective_contract_id')

class UsersModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Users.objects.create(name='dfgyu', login='345678', password='1456')

    def test_name_label(self):
        ad = Users.objects.get(id=1)
        field_label = ad._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_login_label(self):
        ad = Users.objects.get(id=1)
        field_label = ad._meta.get_field('login').verbose_name
        self.assertEquals(field_label, 'login')

    def test_password_label(self):
        ad = Users.objects.get(id=1)
        field_label = ad._meta.get_field('password').verbose_name
        self.assertEquals(field_label, 'password')

class Backup_copyModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Backup_copy.objects.create(name='dfgyu', number='3')

    def test_name_label(self):
        ad = Backup_copy.objects.get(id=1)
        field_label = ad._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_login_label(self):
        ad = Backup_copy.objects.get(id=1)
        field_label = ad._meta.get_field('number').verbose_name
        self.assertEquals(field_label, 'number')



