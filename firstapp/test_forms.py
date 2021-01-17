from django.test import TestCase
import unittest
from .forms import DataClient, Collective_contract, DataEmployee_category, DataCollective_contract, DataCompany, DataAgent, DataUsers, DataBackup_copy

class DataClientFormTest(TestCase):
    def test_full_name_label(self):
        form = DataClient()
        self.assertTrue(form.fields['full_name'].label == None or form.fields['full_name'].label == 'Имя клиента')

    def test_age_label(self):
        form = DataClient()
        self.assertTrue(form.fields['age'].label == None or form.fields['age'].label == 'Возраст')

    def test_risk_category_label(self):
        form = DataClient()
        self.assertTrue(form.fields['risk_category'].label == None or form.fields['risk_category'].label == 'Категория риска')

    def test_collective_contract_id_label(self):
        form = DataClient()
        self.assertTrue(form.fields['collective_contract_id'].label == None or form.fields['collective_contract_id'].label == 'Коллективный контракт')

    def test_resoult(self):
        form = DataClient(data={'full_name': "Иван Иванович", 'age': "18", 'risk_category': 'sdfghjk', 'collective_contract_id': 1})
        self.assertTrue(form.is_valid())

class DataCollective_contractFormTest(TestCase):
    def test_term_of_the_contract_label(self):
            form = DataCollective_contract()
            self.assertTrue(form.fields['term_of_the_contract'].label == None or form.fields['term_of_the_contract'].label == 'Срок контракта')

    def test_date_of_conclusion_label(self):
        form = DataCollective_contract()
        self.assertTrue(form.fields['date_of_conclusion'].label == None or form.fields['date_of_conclusion'].label == 'Дата заключения')

    def test_employee_category_id_label(self):
        form = DataCollective_contract()
        self.assertTrue(form.fields['employee_category_id'].label == None or form.fields['employee_category_id'].label == 'Категория сотрудника')

    def test_payments_for_insured_events_label(self):
        form = DataCollective_contract()
        self.assertTrue(form.fields['payments_for_insured_events'].label == None or form.fields['payments_for_insured_events'].label == 'Выплата по страховым случаям')

    def test_resoult(self):
        form = DataCollective_contract(data={'term_of_the_contract': "55", 'date_of_conclusion': "2010-03-15", 'employee_category_id': 1, 'payments_for_insured_events': '33'})
        self.assertTrue(form.is_valid())

class DataEmployee_categoryFormTest(TestCase):
    def test_number_label(self):
        form = DataEmployee_category()
        self.assertTrue(form.fields['number'].label == None or form.fields['number'].label == 'Номер')

    def test_employee_full_name_label(self):
        form = DataEmployee_category()
        self.assertTrue(form.fields['employee_full_name'].label == None or form.fields['employee_full_name'].label == 'Имя сотрудника')

    def test_employee_risk_category_label(self):
        form = DataEmployee_category()
        self.assertTrue(form.fields['employee_risk_category'].label == None or form.fields['employee_risk_category'].label == 'Категория риска сотрудника')

    def test_agent_id_label(self):
        form = DataEmployee_category()
        self.assertTrue(form.fields['agent_id'].label == None or form.fields['agent_id'].label == 'Агент')

    def test_resoult(self):
        form = DataEmployee_category(data={'number': "55", 'employee_full_name': "Fdhjk", 'agent_id': 1, 'employee_risk_category': '33'})
        self.assertTrue(form.is_valid())

class DataCompanyFormTest(TestCase):
    def test_code_label(self):
        form = DataCompany()
        self.assertTrue(form.fields['code'].label == None or form.fields['code'].label == 'Код')

    def test_full_name_label(self):
        form = DataCompany()
        self.assertTrue(form.fields['full_name'].label == None or form.fields['full_name'].label == 'Полное название')

    def test_short_title_label(self):
        form = DataCompany()
        self.assertTrue(form.fields['short_title'].label == None or form.fields['short_title'].label == 'Аббревеатура')

    def test_adress_label(self):
        form = DataCompany()
        self.assertTrue(form.fields['adress'].label == None or form.fields['adress'].label == 'Адрес')

    def test_bank_details_label(self):
        form = DataCompany()
        self.assertTrue(form.fields['bank_details'].label == None or form.fields['bank_details'].label == 'Банковские реквизиты')

    def test_company_specialization_label(self):
        form = DataCompany()
        self.assertTrue(form.fields['company_specialization'].label == None or form.fields['company_specialization'].label == 'Специализация компании')

    def test_collective_contract_id_label(self):
        form = DataCompany()
        self.assertTrue(form.fields['collective_contract_id'].label == None or form.fields['collective_contract_id'].label == 'Коллективный контракт')

    def test_resoult(self):
        form = DataCompany(data={'code': "55", 'full_name': "Fdhjk", 'short_title': '3dfghj', 'adress': '3dfghj', 'bank_details': '34567', 'company_specialization': '34567', 'collective_contract_id': 1,})
        self.assertTrue(form.is_valid())

class DataAgentFormTest(TestCase):
    def test_full_name_label(self):
        form = DataAgent()
        self.assertTrue(form.fields['full_name'].label == None or form.fields['full_name'].label == 'Имя агента')

    def test_passport_data_label(self):
        form = DataAgent()
        self.assertTrue(form.fields['passport_data'].label == None or form.fields['passport_data'].label == 'Данные паспорта')

    def test_collective_contract_id_label(self):
        form = DataAgent()
        self.assertTrue(form.fields['collective_contract_id'].label == None or form.fields['collective_contract_id'].label == 'Коллективный контракт')

    def test_resoult(self):
        form = DataAgent(data={'full_name': "dfghjkl", 'passport_data': "2345678", 'collective_contract_id': 1})
        self.assertTrue(form.is_valid())

class DataUsersFormTest(TestCase):
    def test_name_label(self):
        form = DataUsers()
        self.assertTrue(form.fields['name'].label == None or form.fields['name'].label == 'Имя пользователя')

    def test_login_label(self):
        form = DataUsers()
        self.assertTrue(form.fields['login'].label == None or form.fields['login'].label == 'Логин')

    def test_password_label(self):
        form = DataUsers()
        self.assertTrue(form.fields['password'].label == None or form.fields['password'].label == 'Пароль')

    def test_resoult(self):
        form = DataUsers(data={'name': "dfghjkl", 'login': "2345678", 'password': "234567"})
        self.assertTrue(form.is_valid())

class DataBackup_copyFormTest(TestCase):
    def test_number_label(self):
        form = DataBackup_copy()
        self.assertTrue(form.fields['number'].label == None or form.fields['number'].label == 'Номер')

    def test_name_label(self):
        form = DataBackup_copy()
        self.assertTrue(form.fields['name'].label == None or form.fields['name'].label == 'Имя пользователя')

    def test_resoult(self):
        form = DataBackup_copy(data={'number': "34567", 'name': "sdfgfhghj"})
        self.assertTrue(form.is_valid())





