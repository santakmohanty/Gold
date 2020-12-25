from django.urls import path
from apps.main.views.demo_user_view import DemoUserView

app_name = 'apps'

urlpatterns = [
    path('index/', DemoUserView.index, name = 'index'),
]
