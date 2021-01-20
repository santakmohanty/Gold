from django.http import HttpRequest
from django.shortcuts import render

from apps.main.views.base_view import BaseView
import pandas as pd
output_list = [
    {
        "sku": "Lorem",
        "description": "ipsum",
        "asin_no": "dolor",
        "misc": "sit",
        "warehouse_b": "sit",
    },
    {

        "sku": "amet",
        "description": "consectetur",
        "asin_no": "adipiscing",
        "misc": "elit",
        "warehouse_b": "elit",
    },
    {

        "sku": "Integer",
        "description": "nec",
        "asin_no": "odio",
        "misc": "Praesent",
        "warehouse_b": "Praesent",
    },
    {

        "sku": "libero",
        "description": "Sed",
        "asin_no": "cursus",
        "misc": "ante",
        "warehouse_b": "ante",
    },
    {

        "sku": "dapibus",
        "description": "diam",
        "asin_no": "Sed",
        "misc": "nisi",
        "warehouse_b": "nisi",
    },
    {

        "sku": "Nulla",
        "description": "quis",
        "asin_no": "sem",
        "misc": "at",
        "warehouse_b": "at",
    },
    {

        "sku": "nibh",
        "description": "elementum",
        "asin_no": "imperdiet",
        "misc": "Duis",
        "warehouse_b": "Duis",
    },
    {

        "sku": "sagittis",
        "description": "ipsum",
        "asin_no": "Praesent",
        "misc": "mauris",
        "warehouse_b": "mauris",
    },
    {

        "sku": "Fusce",
        "description": "nec",
        "asin_no": "tellus",
        "misc": "sed",
        "warehouse_b": "sed",
    },
    {

        "sku": "augue",
        "description": "semper",
        "asin_no": "porta",
        "misc": "Mauris",
        "warehouse_b": "Mauris",
    },
    {

        "sku": "massa",
        "description": "Vestibulum",
        "asin_no": "lacinia",
        "misc": "arcu",
        "warehouse_b": "arcu",
    }]


class DemoUserView(BaseView):

    @staticmethod
    def index(request: HttpRequest):
        return render(request, 'pages/index.html',
                      {"output_list": output_list, "total": 100, "query": request.GET.get('query', "")})

    @staticmethod
    def search(request: HttpRequest):
        return render(request, 'pages/index.html',
                      {"output_list": output_list, "total": 100, "query": request.GET.get('query', "")})

    @staticmethod
    def upload(request: HttpRequest):
        if request.FILES['excel_file_upload']:
            excel_file = request.FILES['excel_file_upload']
            df = pd.read_excel(excel_file)
            print("*"*99)
            print(df)
            print("*" * 99)
        return render(request, 'pages/index.html',
                      {"output_list": output_list, "total": 100, "query": request.GET.get('query', "")})
