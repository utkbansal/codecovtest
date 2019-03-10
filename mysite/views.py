from django.shortcuts import HttpResponse


def foo_view(request):
    if request.method == 'GET':
        return HttpResponse('This is the foo view!', status=200)


def bar_view(request):
    if request.method == 'GET':
        return HttpResponse('This is the bar view!', status=200)

def hello2_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello World!')