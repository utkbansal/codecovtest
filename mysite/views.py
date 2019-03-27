from django.shortcuts import HttpResponse


def first_view(request):
    if request.method == 'GET':
        return HttpResponse('This is the first view!', status=200)


def second_view(request):
    if request.method == 'GET':
        return HttpResponse('This is the second view!', status=200)


def third_view(request):
    if request.method == 'GET':
        return HttpResponse('This is the third view!', status=200)


def fourth_view(request):
    if request.method == 'GET':
        a = 1/2
        b = False

        if b > a:
            print('foo')

        return HttpResponse('This is the fourth view!', status=200)