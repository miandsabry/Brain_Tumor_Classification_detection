import cv2
import imutils
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os
from tensorflow import keras
import numpy as np

# load ml models.

biModel = keras.models.load_model((os.path.dirname(os.path.dirname(__file__))) +
                                  r'\mlModels\bi_model.h5')


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
    img = PreprocessData(testimage)
    img = np.reshape(img, [1, 224, 224, 3])
    img = np.array(img)
    bi_prediction = biModel.predict(img)

    context = {'testImgPath': testImgPath, 'bi_prediction': bi_prediction}
    return render(request, 'Result/result.html', context)


def Home(request):
    return render(request, 'Home/home.html')


def New(request):
    return render(request, 'New-patiant/patiant.html')


def Search(request):
    return render(request, 'Search/search.html')


def PreprocessData(ImagePath):
    # str1 = ImagePath + '.JPG'
    img = cv2.imread(str(ImagePath))
    # cv2.imshow('x',img)
    # cv2.waitKey(0)
    img_resized = cv2.resize(img, (224, 224))
    gray = cv2.cvtColor(img_resized, cv2.COLOR_RGB2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=2)
    outline = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    outline = imutils.grab_contours(outline)
    area = max(outline, key=cv2.contourArea)
    max_left = tuple(area[area[:, :, 0].argmin()][0])
    max_right = tuple(area[area[:, :, 0].argmax()][0])
    max_top = tuple(area[area[:, :, 1].argmin()][0])
    max_bottom = tuple(area[area[:, :, 1].argmax()][0])
    ADD_PIXELS = 0
    final_image = img_resized[max_top[1] - ADD_PIXELS:max_bottom[1] + ADD_PIXELS,
                  max_left[0] - ADD_PIXELS:max_right[0] + ADD_PIXELS].copy()
    final_image = cv2.resize(final_image, (224, 224))
    return final_image
