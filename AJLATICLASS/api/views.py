from django.shortcuts import render

# Create your views here.
import serializer as serializer
from rest_framework import serializers
# from DRF.drf_serailezer.api.models import Employee
import json
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Employee
from .serializers import EmployeeSerializer
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import  View
@method_decorator(csrf_exempt,name='dispatch')
class EmployeeAPI(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        print(f"Json data is {json_data}")
        id = None
        if json_data:
            stream = io.BytesIO(json_data)
            py_data = JSONParser().parse(stream)
            id = py_data.get('id', None)
        if id:
            emp = Employee.objects.get(id=id)
            print(f"Employee is {emp}")
            serializer = EmployeeSerializer(emp)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    def post(self,request,*args,**kwargs):
        json_data = request.body
        print(f"Json data is {json_data}")
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        serializer = EmployeeSerializer(data=py_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'New record created.'}
            json_data = JSONRenderer().render(res)
        else:
            json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    # return HttpResponse(json_data)
    def put(self,request,*args,**kwargs):
        json_data = request.body
        print(f"Json data is {json_data}")
        # deserializing the json data to complex type
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        id = py_data.get('id')
        emp = Employee.objects.get(id=id)
        # emp.delete()
        serializer = EmployeeSerializer(emp, data=py_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'New record Updated.'}
            json_data = JSONRenderer().render(res)
        else:
            json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data)


    def delete(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        id = py_data.get('id')
        emp = Employee.objects.get(id=id)
        emp.delete()
        res = {'msg': 'Data Deleted!!'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')