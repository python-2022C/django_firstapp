from django.http import JsonResponse
from django.http import HttpResponse
import json


def home(request):
    # this data comes as bytestring
    # that is why we have to decode to string
    byte = request.body
    # this decote bytestring do string
    text = byte.decode()
    # since we need dict object 
    # we have to turn string to dict object
    data = json.loads(text)
    # returns sum of dict object values
    return JsonResponse({'sum': int(data.get('a', 0))+int(data.get('b', 0))})

def subtracts(request):
    # byte = request.body 
    # text = byte.decode()
    # data = json.loads(text)
    req = json.loads(request.body.decode())
    return JsonResponse({"sum":int(req.get(a,0))-int(req.get(b,0))})

def multiple(request):
    byte = request.body 
    text = byte.decode()
    data = json.loads(text)
    return JsonResponse({'sum':int(data.get('a',0))*int(data.get('b',0))})

def division(request):
    byte = request.body 
    text = byte.decode
    data = json.loads(text)
    return JsonResponse({'sum':int(data.get("a",0))/int(data.get("b",0))})