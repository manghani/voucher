from django.shortcuts import render
from django.http import HttpResponse
import string
import random
from random import randrange
from vouch.models import Voucher, contact
from vouch.forms import ConsumerForm
from datetime import datetime, timedelta

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def save(request):
    for i in range(0,10):
        a = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 7))  
        code = str(a)
        mobile = random.randint(870000000, 999999999)
        import datetime
        date1 = datetime.date(2021, 1, 1)
        date2 = datetime.date(2021, 1, 31)
        date3 = datetime.date(2021, 12, 1)
        date4 = datetime.date(2021, 12, 31)
        e1 = random_date(date1, date2)
        e2 = random_date(date3, date4)
        p = Voucher( code = code, amount = 500, start_time = e1, end_time = e2)
        q = contact(mobile = mobile)
    p.save()    
    q.save()
    return HttpResponse("saved")


def get_voucher(request):
    u = Voucher.objects.all()
    v = contact.objects.all()
    context = {'u': u, 'v': v}
    if request.method == 'GET':
        return render(request, 'tableview.html', context)

def assign_vouch(request):
    form = ConsumerForm()
    return render(request, 'assign.html', {'form': form})

def delete(request):
    u = Voucher.objects.all()
    v = contact.objects.all()
    u.delete()
    v.delete()
    return HttpResponse("Delete Call")

def valid_voucher(request, code, redeemed, start_time, end_time):
    date = datetime.date.today()
    for i in range(0,10):
        if redeemed == False and start_time<date<end_time:
            return True
        else:
            return False


def front(request):
    return render(request, 'front.html')


def front_page(request):
    return render(request, 'front_page.html')