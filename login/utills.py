import jwt
import json
from django.http     import JsonResponse
from signup.models   import Signup
from westargram.settings import SECRET_KEY

def Login_check(func):
    def wrapper(self, request, *args, **kwargs):
        if "Authorization" not in request.headers: #header에 토큰값이 담겨있는지 확인한다.
            return JsonResponse({"error_code" : "INVALID_LOGIN"}, status=401)
        encode_token = request.headers["Authorization"] #헤더의 토큰 값을 입력해준다.
        try:
            data = jwt.decode(encode_token, SECRET_KEY, algorithms='HS256') #데이터를 decode하여준다. encode할 때 썻던 id값을 추출하기 위해서 이다.
            user = Signup.objects.get(id = data["id"]) #id를 통해 user의 정보를 user에 담아준다.
            request.user = user #가장 중요한 부분이다. get을 통해 가져온 user의 정보를 request.user에 담아준다. 이는 후에 데코레이터를 붙혀줄 views에 사용된다.
        except jwt.DecodeError:
            return JsonResponse({"error_code":"INVALID_TOKEN"}, status=401)
        # except Signup.DoesNotExist:
           # return JsonResponse({"error_code":"UNKNOWN_USER"}, status=401)
        return func(self, request, *args, **kwargs) #리턴되는 requset의 값은 user을 정보를 담은 requset가 된다.
    return wrapper