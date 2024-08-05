from django.shortcuts import render
from django.views import View

from database_app.models import Award, Gallery


class IndexView(View):

    def get(self, request):
        return render(request, 'index.html', context={
            'awards': Award.objects.all(),
            'gallery': Gallery.objects.all()
        })
