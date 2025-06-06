from django.views import View
from django.http import HttpResponse
# Create your views here.
class TestView(View):
    def get(self, request):
        print(request.headers)
        return HttpResponse(
            'hello world'
        )