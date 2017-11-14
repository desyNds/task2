from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.

class TryView(View):
    def get(self, request):
        return HttpResponse('<h1>hello world</h1>')

class TryView1(View):
    def get(self, request):
        return HttpResponse('<h2>hello google</h2>')

class TryView2(View):
    def get(self, request):
        return HttpResponse('<h3>hello world python')

class TryTplView(View):
    def get(self, request):
        template = 'member/index.html'
        data = {
            'words':'we are going to try about python and django',
            'array': [1,2,3,4,5],
            'logic': True
        }
        return render(request, template, data)
