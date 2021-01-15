from django.urls import path

from apps.main.views.demo_user_view import DemoUserView

app_name = 'apps'

urlpatterns = [
    path('search', DemoUserView.search, name='search'),
    path('upload', DemoUserView.upload, name='upload'),
    path('', DemoUserView.index, name='index'),

]
