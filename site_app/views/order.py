from django.shortcuts import redirect
from django.urls import reverse
from django.views import View

from database_app.models import Order


class OrderCreateView(View):

    def post(self, request, *args, **kwargs):
        try:
            Order.objects.create(
                fio=request.POST.get('fio'),
                age=request.POST.get('age'),
                experience=request.POST.get('experience'),
                phone_number=request.POST.get('phone_number'),
                is_agreed=True
            )
        except Exception as e:
            pass
        return redirect(reverse('index'))
