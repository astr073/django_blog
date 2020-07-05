from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View

class DefaultPage(View):
    def get(self, request):
        return redirect('post_lists_url', permanent=True)

