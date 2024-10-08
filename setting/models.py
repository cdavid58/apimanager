from django.db import models

class Unit_Measures(models.Model):
    _id = models.IntegerField(unique = True)
    name = models.CharField(max_length = 191)

    def __str__(self):
        return f"{self._id} - {self.name}"

    @classmethod
    def create_unit_measures(cls, data):
        value = cls(_id = data['id'], name = data['name'])
        value.save()

    @classmethod
    def get_unit_measures(cls):
        return [
            {
                'id': i._id,
                'name':i.name
            }
            for i in cls.objects.all().order_by('name')
        ]

class Operation(models.Model):
    url_api = models.CharField(max_length = 255)

class BANK_NAME(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class Transaction_Types(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class Book_Account(models.Model):
    name = models.CharField(max_length = 80)

    def __str__(self):
        return self.name

class Book_Account_Type(models.Model):
    name = models.CharField(max_length = 80)
    book_account = models.ForeignKey(Book_Account, on_delete= models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.book_account.name}'


class Municipalities(models.Model):
    _id = models.IntegerField()
    name = models.CharField(max_length = 35)

    def __str__(self):
        return self.name

    @classmethod
    def get_municipalities(cls):
        return [
            {
                'pk':i.pk,
                "name":i.name
            }
            for i in cls.objects.all()
        ]

class Type_Document_I(models.Model):
    _id = models.IntegerField()
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

    @classmethod
    def get_type_document_i(cls):
        return [
            {
                'pk':i.pk,
                "name":i.name
            }
            for i in cls.objects.all()
        ]

class Type_Document(models.Model):
    _id = models.IntegerField()
    name = models.CharField(max_length = 100)

    def __str__(self):
        return f'ID: {self.id} - DOC: {self.name}'

    @classmethod
    def get_type_document(cls):
        return [
            {
                'pk':i.pk,
                "name":i.name
            }
            for i in cls.objects.all()
        ]

class Type_Organization(models.Model):
    _id = models.IntegerField()
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

    @classmethod
    def get_type_organization(cls):
        return [
            {
                'pk':i.pk,
                "name":i.name
            }
            for i in cls.objects.all()
        ]

class Type_Regimen(models.Model):
    _id = models.IntegerField()
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name


    @classmethod
    def get_type_regimen(cls):
        return [
            {
                'pk':i.pk,
                "name":i.name
            }
            for i in cls.objects.all()
        ]

class Type_Contract(models.Model):
    _id = models.IntegerField()
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name


    @classmethod
    def get_type_contract(cls):
        return [
            {
                'pk':i.pk,
                "name":i.name
            }
            for i in cls.objects.all()
        ]

class Payroll_Type_Document_Identification(models.Model):
    _id = models.IntegerField()
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name


    @classmethod
    def get_payroll_type_document_identification(cls):
        return [
            {
                'pk':i.pk,
                "name":i.name
            }
            for i in cls.objects.all()
        ]

class Sub_Type_Worker(models.Model):
    _id = models.IntegerField()
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name


    @classmethod
    def get_sub_type_worker(cls):
        return [
            {
                'pk':i.pk,
                "name":i.name
            }
            for i in cls.objects.all()
        ]

class Type_Worker(models.Model):
    _id = models.IntegerField()
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name


    @classmethod
    def get_type_worker(cls):
        return [
            {
                'pk':i.pk,
                "name":i.name
            }
            for i in cls.objects.all()
        ]

class Payment_Form(models.Model):
    _id = models.IntegerField()
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class Payment_Method(models.Model):
    _id = models.IntegerField()
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class Permission(models.Model):
    _id = models.IntegerField(default = 1)
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

    @classmethod
    def get_list_permission(cls):
        return [
            {
                'pk_permission' : i.pk,
                "name":i.name
            }
            for i in cls.objects.all()
        ]
