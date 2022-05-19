
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os


# load ml models.


# def Login(request):
# return render(request, 'Login/login.html')


# def Register(request):
# return render(request, 'Register/register.html')


def user(request):
    return render(request, 'user/index.html')


def Result(request):
    print('*************this is the req:' + str(request))
    print('*************this is the req:' + str(request.POST.dict()))
    if request.method == 'GET':
        return render(request, 'Result/result.html')

    fileObj = request.FILES['imgPath']
    fs = FileSystemStorage()
    testImgPath = fs.save(fileObj.name, fileObj)
    testImgPath = fs.url(testImgPath)
    testimage = '.' + testImgPath


    context = {'testImgPath': testImgPath}
    return render(request, 'Result/result.html', context)


def Home(request):
    return render(request, 'Home/home.html')


def New(request):
    return render(request, 'New-patiant/patiant.html')


def Search(request):
    return render(request, 'Search/search.html')


