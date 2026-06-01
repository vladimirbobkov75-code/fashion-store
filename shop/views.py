from django.shortcuts import render
from .models import Product
from django.core.mail import send_mail


def home(request):
    products = Product.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")

        send_mail(
            subject="Новая заявка с сайта",
            message=f"Имя: {name}\nТелефон: {phone}",
            from_email=None,  # возьмется из settings
            recipient_list=["vladimirbobkov75@gmail.com"],
            fail_silently=False,
        )

    context = {
        'products': products
    }

    return render(request, 'shop/index.html', context)