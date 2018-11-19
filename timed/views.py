from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    times = 1538301600
    time=times-datetime.timestamp(datetime.now())
    days=int(time//(3600*24))
    hours=int((time-(3600*24*days))//(60*60))
    minutes=int((time-(3600*24*days)-(60*60*hours))//60)
    seconds=int((time-(3600*24*days)-(60*60*hours)-60*minutes))
    content={
        'days':days,
        'hours':hours,
        'minutes':minutes,
        'seconds':seconds,
    }
    return render(request,'index.html',context=content)
    # return HttpResponse("您离假期还有%s天%s小时%s分钟%s秒"%(days,hours,minutes,seconds))




