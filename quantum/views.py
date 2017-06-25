#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    text = """<h1>blah blah</h1>"""
    return HttpResponse(text)
