from django.shortcuts import render

import requests
import openai
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from .models import Log  

openai.api_key = settings.OPENAI_API_KEY

def analyze_logs(request):
    logs = requests.get('http://0.0.0.0:0000/logs/').json()
    
    response = openai.Completion.create(
        engine="gpt-4o-mini",
        prompt=f"Analyze these logs: {logs}",
        max_tokens=150
    )

    analysis = response["choices"][0]["text"]

    send_mail(
        "Log Analysis Report",
        analysis,
        "sender@gmail.com",
        ["reciever@gmail.com"],
        fail_silently=False,
    )

    return JsonResponse({"message": "Analysis sent to email!"})

