from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,"index.html",{"title":"Hello world"})
    #HTTPでリクエストに対してテキスト形式でリスポンスを返すためのdjango.http.HttpResponseを使用。

def fuga(request):
    return HttpResponse("fuga")

def render_form(request):
    return  render(request,"login.html")

def login(request):
    if request.POST["username"]and request.POST["email"]:
        return render(request,"check.html",{"email":request.POST["username"],"username":request.POST["email"]})
    else:
        return render(request,"error.html")
