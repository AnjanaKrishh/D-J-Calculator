from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class AdditionView(View):
   def post(self, request):
       request_body = request.body #get value from request body
       form_data = loads(request_body) #convert json format to python dictionary
       n1 = form_data.get('num1') #get value of num1 from the dictionary
       n2 = form_data.get('num2')  #get value of num2 from the dictionary
       result = n1 + n2
       print(request_body) #print the request body to the console for debugging
       data = {
              "Sum": result
       }
       return JsonResponse(data)
@method_decorator(csrf_exempt, name='dispatch')
class SubtractionView(View):
   def post(self, request):
       data= request.body 
       form_data = loads(data) 
       n1 = form_data.get('num1') 
       n2 = form_data.get('num2')  
       difference = n1 - n2
       
       result = {
              "Subtraction": difference
       }
       return JsonResponse(result)
   
@method_decorator(csrf_exempt, name='dispatch')
class MultiplicationView(View):
   def post(self, request):
       request_body = request.body #get value from request body
       form_data = loads(request_body) #convert json format to python dictionary
       n1 = form_data.get('num1') #get value of num1 from the dictionary
       n2 = form_data.get('num2')  #get value of num2 from the dictionary
       result = n1 * n2
       print(request_body) #print the request body to the console for debugging
       data = {
              "Multiplication": result
       }
       return JsonResponse(data)
@method_decorator(csrf_exempt, name='dispatch')
class DivisionView(View):
   def post(self, request):
       request_body = request.body #get value from request body
       form_data = loads(request_body) #convert json format to python dictionary
       n1 = form_data.get('num1') #get value of num1 from the dictionary
       n2 = form_data.get('num2')  #get value of num2 from the dictionary
       result = n1 / n2
       print(request_body) #print the request body to the console for debugging
       data = {
              "Division": result
       }
       return JsonResponse(data)
@method_decorator(csrf_exempt, name='dispatch')
class ModulusView(View):
   def post(self, request):
       request_body = request.body #get value from request body
       form_data = loads(request_body) #convert json format to python dictionary
       n1 = form_data.get('num1') #get value of num1 from the dictionary
       n2 = form_data.get('num2')  #get value of num2 from the dictionary
       result = n1 % n2
       print(request_body) #print the request body to the console for debugging
       data = {
              "Modulus": result
       }
       return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class PercentageView(View):
   def post(self, request):
       request_body = request.body
       form_data = loads(request_body) 
       n1 = form_data.get('obtained_marks')
       n2 = form_data.get('total_marks')  
       result = (n1 / n2) * 100
       print(request_body) 
       data = {
              "Percentage": result
       }
       return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class BMIView(View):
   def post(self, request):
       request_body = request.body
       form_data = loads(request_body) 
       weight = form_data.get('weight')
       height = form_data.get('height')  
       height_in_meters = height / 100  
       bmi = weight / (height_in_meters ** 2)
       print(request_body) 
       data = {
              "BMI": bmi
       }
       return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class AgeView(View):
   def post(self, request):
       request_body = request.body
       form_data = loads(request_body) 
       birth_year = form_data.get('birth_year')
       current_year = form_data.get('current_year')  
       age = current_year - birth_year
       print(request_body) 
       data = {
              "Age": age
       }
       return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class SimpleInterestView(View):
   def post(self, request):
       request_body = request.body
       form_data = loads(request_body) 
       principal = form_data.get('principal')
       rate = form_data.get('rate')  
       time = form_data.get('time')  
       simple_interest = (principal * rate * time) / 100
       print(request_body) 
       data = {
              "principal": principal,
              "rate": rate, 
              "time": time,
              "Simple Interest": simple_interest
       }
       return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class ElectricityBillView(View):
   def post(self, request):
       request_body = request.body
       form_data = loads(request_body) 
       units = form_data.get('units')
       rate= form_data.get('rate')  
       electricity_bill = units * rate
       print(request_body) 
       data = {
              "units": units,
              "rate": rate, 
              "Electricity Bill": electricity_bill
       }
       return JsonResponse(data)