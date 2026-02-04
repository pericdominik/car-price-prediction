from django.shortcuts import render
import requests, json, os
from dotenv import load_dotenv
from django.conf import settings

load_dotenv()

SCORING_URI = settings.SCORING_URI
API_KEY = settings.API_KEY

def predict_view(request):
    print("DEBUG FILE =", __file__)
    print("DEBUG SCORING_URI =", SCORING_URI, type(SCORING_URI))

    predicted_price = None
    error = None

    if request.method == "POST":
        try:
            payload = {
                "brand": request.POST.get("brand"),
                "model": request.POST.get("model"),
                "model_year": int(request.POST.get("model_year")),
                "milage": float(request.POST.get("milage")),
                "fuel_type": request.POST.get("fuel_type"),
                "engine": request.POST.get("engine"),
                "transmission": request.POST.get("transmission"),
                "ext_col": request.POST.get("ext_col"),
                "int_col": request.POST.get("int_col"),
                "accident": request.POST.get("accident"),
                "clean_title": request.POST.get("clean_title"),
            }

            headers = {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
            }

            r = requests.post(SCORING_URI, headers=headers, json=payload, timeout=30)

            if r.status_code == 200:
                predicted_price = r.json().get("predicted_price")
            else:
                error = f"API error {r.status_code}: {r.text}"

        except Exception as e:
            error = str(e)

    return render(request, "carui/form.html", {"predicted_price": predicted_price, "error": error})