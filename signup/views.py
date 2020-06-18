from django.shortcuts import render
from .models import Signup
import json
from django.views import View
from django.http  import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import bcrypt

@method_decorator(csrf_exempt, name='dispatch')
class SignupView(View) :
    def post(self, request):
        try:
            data = json.loads(request.body)
            hashd_password = bcrypt.hashpw(data['password'].encode('utf-8'),bcrypt.gensalt())
            Signup(
                new_id  = data['new_id'],
                password = hashd_password.decode('utf-8'),
                email = data['email'] 
            ).save()
            return JsonResponse({'message':'SUCCESS'}, status=200)
        except KeyError : #예외처리
            #리턴해라 제이슨타입으로 {message:INVALID_KEYS}
            return JsonResponse({'mesaage':"INVALID_KEYS"},status =400)
#예외처리
'''
    def get(self, request):
            sign_id = Signup.objects.values()
            return JsonResponse({'Signup':list(sign_id)}, status=200)

        except KeyError : #예외처리

            #리턴해라 제이슨타입으로 {message:INVALID_KEYS}
            return JsonResponse({'mesaage':"INVALID_KEYS"},status =400)
            '''



# Create your views here.
