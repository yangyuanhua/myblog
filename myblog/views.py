from django.shortcuts import HttpResponse,render
import os
import sys





def test_view(request):
    dirlist = []
    dirlist.extend(os.listdir("./templates/math"))
#    print(dirlist)

    return render(request,"test1.html",locals())


def math_view(request):
    temp = request.GET.get('name','not found')
#    print("*"*20)
#    print(temp)
    return render(request,"math/%s"%(temp))
