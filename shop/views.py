from django.shortcuts import render
from .models import Product
from django.core.mail import send_mail
import os


def home(request):
    products = Product.objects.all()

    # Проверка файлов изображений
    for p in products:
        try:
            print("URL:", p.image.url)
            print("PATH:", p.image.path)
            print("EXISTS:", os.path.exists(p.image.path))
        except Exception as e:
            print("ERROR:", e)

    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")

        send_mail(
            subject="Новая заявка с сайта",
            message=f"Имя: {name}\nТелефон: {phone}",
            from_email=None,
            recipient_list=["vladimirbobkov75@gmail.com"],
            fail_silently=False,
        )

    context = {
        'products': products
    }

    return render(request, 'shop/index.html', context)