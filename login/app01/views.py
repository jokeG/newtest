from django.shortcuts import render, HttpResponse, reverse


# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        # print(request.POST)#<QueryDict: {'name': ['joke'], 'pwd': ['123']}>
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        return HttpResponse('登录成功')
