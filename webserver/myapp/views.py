from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

def name_view(request):
    return HttpResponse("Olani Siyum")

def hobby_view(request):
    return JsonResponse({"hobby": "Building innovative web applications"})

def dream_view(request):
    return HttpResponse("I dream to build impactful technologies that empower communities.")

