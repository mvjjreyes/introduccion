from django.views.generic import View
from django.shortcuts import render
#request: es para peticiones
#args: para parametros
class HomeView(View):
    def get(self, request, *args, **kwargs):
        #Disccionario de datos
        context = {}
        return render(request, 'index.html', context)
