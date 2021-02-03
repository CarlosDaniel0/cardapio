from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.backends.db import SessionStore
from django.shortcuts import render
from django.utils import timezone
from django.http import Http404, HttpResponse, JsonResponse
from .models import Item
from django.core import serializers
import json
# Create your views here.


def home(request):
    items = Item.objects.all()
    return render(request, 'cardapio/itens.html', {'items': items})

def contato(request):
    return render(request, 'cardapio/contato.html', {})

def sobre(request):
    return render(request, 'cardapio/sobre.html', {})

def lanche(request, id):
    item = Item.objects.filter(id=id).values()
    item = item[0]
    new_item = item
    new_item['pk'] = id
    ingredientes = item['ingredientes'].split(',')
    return render(request, 'cardapio/lanche.html', {'id': id, 'item': new_item, 'ingredientes': ingredientes})


def carrinho(request):
    itens = request.session.get('itens')
    items = []
    total = 0
    none = False
    if itens != None:
        for i in itens:
            item = Item.objects.filter(id=i['id']).values()
            new_item = item[0]
            new_item['quantidade'] = i['quantidade']
            new_item['pk'] = itens.index(i)
            new_item['total'] = float(new_item['valor']) * int(new_item['quantidade'])
            items.append(new_item)
            total += float(new_item['total'])
    else:
        none = True
    
    
    return render(request, 'cardapio/carrinho.html', {'items':items, 'total': total, 'none': none})

@csrf_exempt
def carrinho_add(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        quantidade = request.POST.get('quantidade')
        
        if request.session.get('itens') == None:
            itens = []
            itens.append({'id':id, 'quantidade':quantidade})
            request.session['itens'] = itens
            request.session['quantidade'] = 1
            request.session.set_expiry(300)
        else:
            request.session['quantidade'] += 1
            request.session['itens'].append({'id':id, 'quantidade':quantidade})
        message = 'O Item {} foi adicionado com sucesso!'.format(id)
        request.session.modified = True
        return JsonResponse({'message': request.session['itens']})
        itens = []
        

@csrf_exempt
def carrinho_remove(request):
    if request.method == 'POST':
        if len(request.session['itens']) == 1:
            del request.session['itens']
            del request.session['quantidade']
            message = 'Todos os itens foram apagados com sucesso!'
            request.session.modified = True
            return JsonResponse({'message': message})
        else:
            id = int(request.POST.get('id'))
            request.session['itens'].pop(id)
            request.session['quantidade'] -= 1
            message = 'O Item {} foi apagado com sucesso!'.format(id)
            request.session.modified = True
            return JsonResponse({'message': message})

@csrf_exempt
def carrinho_quantidade(request):
    if request.method == 'POST':
        if request.session.get('itens') != None:
            quantidade = len(request.session['itens'])
            return JsonResponse({'quantidade': quantidade})
        return JsonResponse({'quantidade': 0})