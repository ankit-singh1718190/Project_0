from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from django.http import HttpResponse,JsonResponse
from rest_framework.renderers import JSONRenderer
# Create your views here.
def StudentFun(request):
    stu=Student.objects.all()
    serializer=StudentSerializer(stu,many=True)
    return JsonResponse(serializer.data,safe=False)

    # json_data=JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type='application/json')