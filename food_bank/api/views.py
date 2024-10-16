from django.shortcuts import render, HttpResponse
import json

# Create your views here.
def sample_api(request):
    jsondata = {
        "hello": "world"
    }
    return HttpResponse(json.dumps(jsondata))

def account_login(request):
    return HttpResponse("account login")