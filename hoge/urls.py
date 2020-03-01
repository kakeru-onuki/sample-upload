from django.urls import path
from . import views
# アプリのルーティングの基本設定がしてあるdjangoAppでこのhoge/urls.py全体が/hogeのルーティングに対応付けることに注意
# つまり/アプリ名から後ろのルーティングを対応付けないとアクセスできないということ。

urlpatterns=[
    #/hogeに対応
    path("",views.index),
    #/hogefooに対応
    path("foo",views.foo),
    # /hoge/wooに対応
    path("woo",views.woo),
]
