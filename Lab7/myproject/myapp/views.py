from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request)
    return HttpResponse("<h1>ICT12367 SPU<h1>")

def about(request)
    return HttpResponse("<h1>เกี่ยวกับเรา<h1>")

def from(request)
    return HttpResponse("<h1>แบบฟอร์มบันทึกข้อมูล<h1>")