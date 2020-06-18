from django.shortcuts import render
from signup.models import Signup
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from django.http  import JsonResponse,HttpResponse
from westargram.settings import SECRET_KEY
import bcrypt
import jwt

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    def post(self, request):
        data = json.loads(request.body) #data는 request의 데이터를 json형태로 불러온다

        try: #시도해라
            #만약 signup의 데이터 중에 request로 받아온 data['new_id']키값이 존재한다면
            if Signup.objects.filter(new_id = data['new_id']).exists():

                #객체를 가져온다.signup의 데이터 중 new_id =data['new_id']인 데이터를 새로운 객체로 만든다.
                user = Signup.objects.get(new_id = data['new_id'])
                user_password = user.password.encode('utf-8')

                
                if bcrypt.checkpw(data['password'].encode('utf-8'),user_password):
                   
                    #토큰발행
                    token = jwt.encode({'id' : user.id}, SECRET_KEY, algorithm = "HS256")
                    token = token.decode('utf-8')       

                    #리턴해라.제이슨 타입으로 
                    return JsonResponse({"token" : token }, status=200)

                else: # 그게아니면

                    #리턴해라 제이슨타입으로 {'message : 비밀번호가 틀렸습니다 !}
                    return JsonResponse({'message':"비밀번호가 틀렸습니다!"}, status = 401)

            else: #그게아니면

                #리턴해라 400
                return HttpResponse(status=400)


        except KeyError : #예외처리

            #리턴해라 제이슨타입으로 {message:INVALID_KEYS}
            return JsonResponse({'mesaage':"INVALID_KEYS"},status =400)



# Create your views here.
