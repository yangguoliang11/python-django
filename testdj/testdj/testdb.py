# -*- coding: UTF-8 -*-

from django.http import HttpResponse

from TestModel.models import Test

def testdb(result):
    test1 = Test(name='guoliang')
    test1.save()
    return HttpResponse("Success")
