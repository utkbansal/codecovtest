from django.shortcuts import HttpResponse


def foo_view(request):
    if request.method == 'GET':
        return HttpResponse('This is the foo view!', status=200)