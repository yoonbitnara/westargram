import json
from django.views import View
from django.http  import JsonResponse,HttpResponse
from .models      import Comment
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from signup.models import Signup
from login.utills import Login_check



'''
class CommentView(View):
    def post(self,request):
        data = json.loads(request.body)
        Comment(
            user_id = data['user_id'],
            comment_data = data['comment_data']
        ).save()

        return JsonResponse({'massge':'SUCCESS'}, status=200)

    def get(self,request):
        user_data = Comment.objects.values()
        return JsonResponse({'Comments':list(user_data)}, status=200)
'''
@method_decorator(csrf_exempt, name='dispatch')
class CommentView(View) :
    @Login_check
    def post(self, request):
        data = json.loads(request.body)
        Comment(
            user_id  = data['user_id'],
            comment_data = data['comment_data'],
            account = Signup.objects.get(id=1)
        ).save()
        return JsonResponse({'message':'SUCCESS'}, status=200)
#예외처리
    def get(self, request):
        user_data = Comment.objects.values()
        return JsonResponse({'Comments':list(user_data)}, status=200)




# Create your views here.
