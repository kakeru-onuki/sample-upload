
from django.contrib import admin #Djangoの管理者用の画面を呼び出すためのモジュールadminを呼び出す
from django.urls import  path , include
from . import views

urlpatterns = [
path("",views.index), #urlの後ろが何も入力されなかったら、views.pyで定義した関数indexを読み込む
path("hoge/",include("hoge.urls")),#hogeのアプリのルーティングを対応付ける　/hoge/後ろの関数名でhoge.urlsから読み込む。
path("fuga",views.fuga),
path('admin/', admin.site.urls),
path("form",views.render_form),
path("login",views.login),
]
