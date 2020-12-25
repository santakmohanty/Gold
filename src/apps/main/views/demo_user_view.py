from django.contrib import messages
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render, redirect

from apps.main.models.demo_user_model import DemoUser
from apps.main.views.base_view import BaseView


class DemoUserView(BaseView):

    @staticmethod
    def index(request: HttpRequest):
        return render(request, 'pages/index.html', {})