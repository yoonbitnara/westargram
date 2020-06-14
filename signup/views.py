from django.shortcuts import render
from .models import Signup
import json
from django.views import View
from django.http  import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class SignupView(View) :
    def post(self, request):
        data = json.loads(request.body)
        Signup(
            new_id  = data['new_id'],
            password = data['password'],
            email = data['email'] 
        ).save()
        return JsonResponse({'message':'SUCCESS'}, status=200)
#예외처리
    def get(self, request):
        sign_id = Signup.objects.values()
        return JsonResponse({'Signup':list(sign_id)}, status=200)


# Create your views here.
