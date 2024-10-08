from django.utils.crypto import get_random_string
from django.http import JsonResponse
from operation import Authenticacion
from django.core import serializers
from django.db import models
from setting.models import *
import json, env

class User(models.Model):
    type_worker_id = models.ForeignKey(Type_Worker, on_delete = models.CASCADE, null = True, blank = True)
    sub_type_worker_id = models.ForeignKey(Sub_Type_Worker, on_delete = models.CASCADE, null = True, blank = True)
    payroll_type_document_identification_id = models.ForeignKey(Payroll_Type_Document_Identification, on_delete = models.CASCADE, null = True, blank = True)
    municipality_id = models.ForeignKey(Municipalities, on_delete = models.CASCADE, null = True, blank = True)
    type_contract_id = models.ForeignKey(Type_Contract, on_delete = models.CASCADE, null = True, blank = True)
    high_risk_pension = models.BooleanField(default = False)
    identification_number = models.IntegerField()
    surname = models.CharField(max_length=255)
    second_surname = models.CharField(max_length=255, null = True, blank = True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255)
    integral_salary = models.BooleanField(default = True)
    salary = models.IntegerField(default = 0, null = True, blank = True)
    email = models.EmailField(null = True, blank = True)
    user_name = models.CharField(max_length = 20, null = True, blank = True,unique=True)
    psswd = models.CharField(max_length = 20, default = get_random_string(length=20), unique = True)
    block = models.BooleanField(default = False)
    permission = models.ManyToManyField(Permission, blank = True, null = True)
    active = models.BooleanField(default = False)
    internal_email = models.EmailField(null=True, blank=True, unique= True)
    company = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.surname}"

    @classmethod
    def login(cls, request):
        result = False
        message = None
        user = None
        _data = None
        _user = None

        try:
            user = cls.objects.get(user_name= request.data['user_name'].lower(), psswd= request.data['psswd'])
        except cls.DoesNotExist as e:
            user = None
            message = str(e)
        
        if user is not None:
            _data = json.dumps({'pk_company': user.company})
            _data = Authenticacion(request).Login_Company(_data)
            result = True
            message = "Success"
            _user = cls.get_user_serialized(cls,user)[0]['fields']
            _user['pk_user'] = user.pk
            _user['permission'] = [ i.name for i in user.permission.all()]
        return {'result': result, 'message': message,'data':_data,'user': _user}


    @staticmethod
    def get_user_serialized(cls,user):
        try:
            serialized_employee = serializers.serialize('json', [user])
            return json.loads(serialized_employee)
        except cls.DoesNotExist:
            return JsonResponse({'error': 'Employee not found'}, status=404)



    @classmethod
    def create_user(cls, data):
        result = False
        message = None
        try:
            employee = cls.objects.get(identification_number=data['identification_number'])
            message = "The employee already exists."
        except cls.DoesNotExist as e:
            employee = None

        if employee is None:
	        employee = cls(
	            type_worker_id = Type_Worker.objects.get(id = data['type_worker_id']),
	            sub_type_worker_id = Sub_Type_Worker.objects.get(id = data['sub_type_worker_id']),
	            payroll_type_document_identification_id = Payroll_Type_Document_Identification.objects.get(id = data['payroll_type_document_identification_id']),
	            municipality_id = Municipalities.objects.get(id = data['municipality_id']),
	            type_contract_id = Type_Contract.objects.get(id = data['type_contract_id']),
	            high_risk_pension = data['high_risk_pension'],
	            identification_number = data['identification_number'],
	            surname = data['surname'],
	            second_surname = data['second_surname'],
	            first_name = data['first_name'],
	            middle_name = None,
	            address = data['address'],
	            salary = int(data['salary']),
	            email = data['email'],
	            company = data['pk_company'],
	            user_name = data['user_name'].lower(),
	            psswd = get_random_string(length=20) if data['psswd'] is None else data['psswd'],
	            internal_email = f"{data['user_name'].lower()}@{data['name_company'].lower().replace(' ','')}.com"
	        )
	        employee.save()
	        for i in data['permissions']:
	            employee.permission.add(Permission.objects.get(pk = i))
	        message = "Success"
	        result = True
	        _data = {"System":"Registration was carried out from the system"} if data['pk_user'] is None else json.loads(cls.get_user_serialized(cls,employee).content.decode('utf-8'))[0]['fields']
	        User_History.register_movement("Created",_data,data)
        return {'result':result, 'message':message}


class User_History(models.Model):
    ACTION_CHOICES = (
        ('Created', 'Created'),
        ('Modified', 'Modified'),
        ('Deleted', 'Deleted')
    )
    
    action = models.CharField(max_length=10, choices=ACTION_CHOICES, null=True, blank=True)
    user_who_registers = models.JSONField(null=True, blank=True)
    recorded_user = models.JSONField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    @classmethod
    def register_movement(cls, action, uwr, ru):
        cls(
            action=action,
            user_who_registers=uwr,
            recorded_user=ru
        ).save()

