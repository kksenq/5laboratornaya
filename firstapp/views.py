from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from .models import Client, Collective_contract, Employee_category, Collective_contract, Company, Agent, Users
from .forms import DataClient, Collective_contract, DataEmployee_category, DataCollective_contract, DataCompany, DataAgent, DataUsers

# Create your views here.

def logout(request):
    return render(request, "registration/login.html")

def index(request):
    return render(request, "index.html")

def index_client(request):
    index_form = DataClient()
    index_data = Client.objects.all()
    return render(request, "Firstapp/Client.html", {"form": index_form, "data": index_data})

class view_Client(View):
    def add_Client(request):
        if request.method == "POST":
            add_data = Client()
            add_data.full_name = request.POST.get('full_name')
            add_data.age = request.POST.get('age')
            add_data.risk_category = request.POST.get('risk_category')
            add_data.collective_contract_id = Collective_contract.objects.get(id=request.POST.get("collective_contract_id"))
            add_data.save()
            return HttpResponseRedirect("/home/Client")

    def del_Client(request):
        if request.method == "POST":
            del_int = request.POST.get("del_int", "")
            del_data = Client.objects.get(id=del_int)
            del_data.delete()
            return HttpResponseRedirect("/home/Client")


    def update_Client(request):
        if request.method == "POST":
            update_int = request.POST.get("update_int", "")
            update_data = Client.objects.get(id=update_int)
            update_data.full_name = request.POST.get('full_name')
            update_data.age = request.POST.get('age')
            update_data.risk_category = request.POST.get('risk_category')
            update_data.collective_contract_id = Collective_contract.objects.get(id=request.POST.get("collective_contract_id"))
            update_data.save()
            return HttpResponseRedirect("/home/Employee_category")



def index_employee_category(request):
    index_form = DataEmployee_category()
    index_data = Employee_category.objects.all()
    return render(request, "Firstapp/Employee_category.html", {"form": index_form, "data": index_data})


class view_Employee_category(View):
    def add_Employee_category(request):
        if request.method == "POST":
            add_data = Employee_category()
            add_data.number = request.POST.get('number')
            add_data.employee_full_name = request.POST.get('employee_full_name')
            add_data.employee_risk_category = request.POST.get('employee_risk_category')
            add_data.save()
            return HttpResponseRedirect("/home/Employee_category")

    def del_Employee_category(request):
        if request.method == "POST":
            del_int = request.POST.get("del_int", "")
            del_data = Employee_category.objects.get(id=del_int)
            del_data.delete()
            return HttpResponseRedirect("/home/Employee_category")

    def update_Employee_category(request):
        if request.method == "POST":
            update_int = request.POST.get("update_int", "")
            update_data = Employee_category.objects.get(id=update_int)
            update_data.number = request.POST.get('number')
            update_data.employee_full_name = request.POST.get('employee_full_name')
            update_data.employee_risk_category = request.POST.get('employee_risk_category')
            update_data.save()
            return HttpResponseRedirect("/home/Employee_category")



def index_Collective_contract(request):
    index_form = DataCollective_contract()
    index_data = Collective_contract.objects.all()
    return render(request, "Firstapp/Collective_contract.html", {"form": index_form, "data": index_data})


class view_Collective_contract(View):
    def add_Collective_contract(request):
        if request.method == "POST":
            add_data = Collective_contract()
            add_data.term_of_the_contract = request.POST.get('term_of_the_contract')
            add_data.date_of_conclusion = request.POST.get('date_of_conclusion')
            add_data.payments_for_insured_events = request.POST.get('payments_for_insured_events')
            add_data.employee_category_id = Employee_category.objects.get(id=request.POST.get("employee_category_id"))
            add_data.save()
            return HttpResponseRedirect("/home/Collective_contract")

    def del_Collective_contract(request):
        if request.method == "POST":
            del_int = request.POST.get("del_int", "")
            del_data = Employee_category.objects.get(id=del_int)
            del_data.delete()
            return HttpResponseRedirect("/home/Collective_contract")

    def update_Collective_contract(request):
        if request.method == "POST":
            update_int = request.POST.get("update_int", "")
            update_data = Collective_contract.objects.get(id=update_int)
            update_data.term_of_the_contract  = request.POST.get('term_of_the_contract ')
            update_data.date_of_conclusion = request.POST.get('date_of_conclusion')
            update_data.payments_for_insured_events = request.POST.get('payments_for_insured_events')
            update_data.employee_category_id = request.POST.get('employee_category_id')
            update_data.save()
            return HttpResponseRedirect("/home/Collective_contract")



def index_Company(request):
    index_form = DataCompany()
    index_data = Company.objects.all()
    return render(request, "Firstapp/Company.html", {"form": index_form, "data": index_data})


class view_Company(View):
    def add_Company(request):
        if request.method == "POST":
            add_data = Company()
            add_data.code = request.POST.get('code')
            add_data.full_name = request.POST.get('full_name')
            add_data.short_title = request.POST.get('short_title')
            add_data.adress = request.POST.get('adress')
            add_data.bank_details = request.POST.get('bank_details')
            add_data.company_specialization = request.POST.get('company_specialization')
            add_data.collective_contract_id = Collective_contract.objects.get(id=request.POST.get("collective_contract_id"))
            add_data.save()
            return HttpResponseRedirect("/home/Company")

    def del_Company(request):
        if request.method == "POST":
            del_int = request.POST.get("del_int", "")
            del_data = Company.objects.get(id=del_int)
            del_data.delete()
            return HttpResponseRedirect("/home/Company")

    def update_Company(request):
        if request.method == "POST":
            update_int = request.POST.get("update_int", "")
            update_data = Company.objects.get(id=update_int)
            update_data.code = request.POST.get('code')
            update_data.full_name = request.POST.get('full_name')
            update_data.short_title = request.POST.get('short_title')
            update_data.adress = request.POST.get('adress')
            update_data.bank_details = request.POST.get('bank_details')
            update_data.company_specialization = request.POST.get('company_specialization')
            update_data.collective_contract_id = request.POST.get('collective_contract_id')
            update_data.save()
            return HttpResponseRedirect("/home/Company")


def index_Agent(request):
    index_form = DataAgent()
    index_data = Agent.objects.all()
    return render(request, "Firstapp/Agent.html", {"form": index_form, "data": index_data})


class view_Agent(View):
    def add_Agent(request):
        if request.method == "POST":
            add_data = Agent()
            add_data.full_name = request.POST.get('full_name')
            add_data.passport_data = request.POST.get('passport_data')
            add_data.collective_contract_id = Collective_contract.objects.get(id=request.POST.get("collective_contract_id"))
            add_data.save()
            return HttpResponseRedirect("/home/Agent")

    def del_Agent(request):
        if request.method == "POST":
            del_int = request.POST.get("del_int", "")
            del_data = Agent.objects.get(id=del_int)
            del_data.delete()
            return HttpResponseRedirect("/home/Agent")

    def update_Agent(request):
        if request.method == "POST":
            update_int = request.POST.get("update_int", "")
            update_data = Agent.objects.get(id=update_int)
            update_data.full_name = request.POST.get('full_name')
            update_data.passport_data = request.POST.get('passport_data')
            update_data.collective_contract_id = request.POST.get('collective_contract_id')
            update_data.save()
            return HttpResponseRedirect("/home/Agent")


def index_Users(request):
    index_form = DataUsers()
    index_data = Users.objects.all()
    return render(request, "Firstapp/Users.html", {"form": index_form, "data": index_data})


class view_Users(View):
    def add_Users(request):
        if request.method == "POST":
            add_data = Users()
            add_data.number = request.POST.get('number')
            add_data.name = request.POST.get('name')
            add_data.save()
            return HttpResponseRedirect("/home/Users")

    def del_Users(request):
        if request.method == "POST":
            del_int = request.POST.get("del_int", "")
            del_data = Users.objects.get(id=del_int)
            del_data.delete()
            return HttpResponseRedirect("/home/Users")

    def update_Users(request):
        if request.method == "POST":
            update_int = request.POST.get("update_int", "")
            update_data = Users.objects.get(id=update_int)
            update_data.number = request.POST.get('number')
            update_data.name = request.POST.get('name')
            update_data.save()
            return HttpResponseRedirect("/home/Users")






