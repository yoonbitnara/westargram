from django.shortcuts import render
from signup.models import Signup
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from django.http  import JsonResponse,HttpResponse

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    def post(self, request):
        data = json.loads(request.body) #data는 request의 데이터를 json형태로 불러온다

        try: #시도해라
            #만약 signup의 데이터 중에 request로 받아온 data['name]키값이 존재한다면
            if Signup.objects.filter(new_id = data['name']).exists():

                #객체를 가져온다.signup의 데이터 중 name =data['name']인 데이터를 새로운 객체로 만든다.
                user = Signup.objects.get(new_id = data['name'])

                #만약 유저안에 패스워드랑 안에 패스워드의 value값이 같다면
                if user.password == data['password']:

                    #리턴해라.제이슨 타입으로 {message}:{user.email}님 로그인 성공
                    return JsonResponse({'message':f'{user.email}님 로그인 성공'}, status = 200)

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
