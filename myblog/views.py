from django.shortcuts import HttpResponse,render
import os
import sys





def test_view(request):
    dirlist = []
    dirlist.extend(os.listdir("./blog/static/math"))
    print(dirlist)
    # print(os.listdir("./blog/static/math"))

    return render(request,"test1.html",locals())