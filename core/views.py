from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse('Hello World')
def soma(request, valor1, valor2):
    resultado = valor1 + valor2
    return HttpResponse('O resultado da soma é {}.'.format(resultado))
def subtracao(request, valor1, valor2):
    resultado = valor1 - valor2
    return HttpResponse('O resultado da subtracao é {}.'.format(resultado))
def multiplicacao(request, valor1, valor2):
    resultado = valor1 * valor2
    return HttpResponse('O resultado da multiplicacao é {}.'.format(resultado))
def divisao(request, valor1, valor2):
    resultado = valor1 // valor2
    return HttpResponse('O resultado da divisao é {}.'.format(resultado))
