from django.test import TestCase
import unittest
from .models import Client, Collective_contract, Employee_category, Collective_contract, Company, Agent, Users, Backup_copy
from django.urls import reverse

class View_Client_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Client.objects.create(full_name='Иванов И.И.', age='20', risk_category='sdtgh', collective_contract_id='1')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/Client/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('Client'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('Client'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Client.html')

class View_Collective_contract_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Collective_contract.objects.create(term_of_the_contract='3', date_of_conclusion='2018-05-22', employee_category_id='1', payments_for_insured_events='2334')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/Collective_contract/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('Collective_contract'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('Collective_contract'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Collective_contract.html')

class View_Employee_categoryt_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Employee_category.objects.create(number='3', employee_full_name='sdfrgh', employee_risk_category='1', agent_id='1')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/Employee_category/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('Employee_category'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('Employee_category'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Employee_category.html')

class View_Company_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Company.objects.create(code='3', full_name='sdfrgh', short_title='sdefgthy', adress='1sdfg', bank_details='1', company_specialization='fghj', collective_contract_id='1')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/Company/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('Company'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('Company'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Company.html')

class View_Agent_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Agent.objects.create(full_name='dfgyu', passport_data='345678', collective_contract_id='1')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/Agent/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('Agent'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('Agent'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Agent.html')

class View_Users_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Users.objects.create(name='dfgyu', login='345678', password='1456')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/Users/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('Users'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('Users'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Users.html')

class View_Backup_copy_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Backup_copy.objects.create(name='dfgyu', number='3')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/Backup_copy/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('Backup_copy'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('Backup_copy'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Backup_copy.html')