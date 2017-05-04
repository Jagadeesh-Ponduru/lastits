from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from .models import Sensor
from .models import Sensorgroup2
from django.db.models import Avg, Max, Min

from math import ceil, floor
# Create your views here.
import datetime
import sqlite3
import smtplib

def float_round(num, places = 0, direction = floor):
    return direction(num * (10**places)) / float(10**places)

def current_datetime(request):
 now = datetime.datetime.now()
 html = "<html><body>It is now %s.</body></html>" % now
 return HttpResponse(html)


def hours_ahead(request, offset):
 offset = int(offset)
 dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
 html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
 return HttpResponse(html)


'''class IOT(TemplateView):
	#Sensor.objects.all().aggregate(Max('price'))
	#raw_input("hello")
	template_name = "myapp/header_first.html"'''

def IOT(request):
	#Sensor.objects.all().aggregate(Max('price'))
	#raw_input("hello")
	sensors1=Sensor.objects.all()
	count = Sensor.objects.all().count()
	sensors=sensors1.reverse()[count-1:]
	sensors1=Sensor.objects.all()[:1]
	avg_1=Sensor.objects.all().aggregate(Avg('Sensor_value'))
    	max1=Sensor.objects.all().aggregate(Max('Sensor_value'))
    	min1=Sensor.objects.all().aggregate(Min('Sensor_value'))
    	avg1=round(avg_1.get('Sensor_value__avg'),3)
    #print avg1
    #raw_input("hello")
	sensors12=Sensorgroup2.objects.all()
	count2 = Sensorgroup2.objects.all().count()
	sensors2=sensors12.reverse()[count2-1:]
	sensors12=Sensorgroup2.objects.all()[:1]
	avg_12=Sensorgroup2.objects.all().aggregate(Avg('Sensor_value'))
    	max12=Sensorgroup2.objects.all().aggregate(Max('Sensor_value'))
    	min12=Sensorgroup2.objects.all().aggregate(Min('Sensor_value'))
    	avg12=round(avg_1.get('Sensor_value__avg'),3)
    	context  = {"sensors1":sensors1,"sensors":sensors,"count":range(count),"avg1":avg1,"max1":max1,"min1":min1,"sensors12":sensors12,"sensors2":sensors2,"count2":range(count2),"avg12":avg12,"max12":max12,"min12":min12,}
        return render(request,"myapp/header_first.html",context)



def get_context_data(self, **kwargs):
	context= super(IOT, self).get_context_data(**kwargs)
	context = {'name':["Sarvani", "pranavi"]}
	return context


def index2(request,group,name,value):
	temp_sen_data = Sensorgroup2()
	temp_sen_data.Sensorgroup2_name = name
	temp_sen_data.Sensorgroup2_value = value
	temp_sen_data.save()


def allsensors(request):
    sensors = Sensor.objects.all()
    count = Sensor.objects.count()


    context  = {
        "sensors":sensors,"count":range(count),
    }
    return render(request,"myapp/sensor_data.html",context)

def sensors(request):
    sensors = Sensor.objects.all()
    count = Sensor.objects.count()

    context  = {
        "sensors":sensors,"count":range(count),
    }
    return render(request,"myapp/sensors.html",context)


def previous(request):
    #sensors = Sensor.objects.all().filter(Sensor.Sensor_date > "March 27, 2017, 11:57 a.m.")
    sensors1 = Sensor.objects.filter(Sensor_date__gte = '2016-03-29 11:58')
    count1 = Sensor.objects.filter(Sensor_date__gte = '2016-03-29 11:58').count()


    sensors2 = Sensor.objects.filter(Sensor_date__gte = '2016-10-01 11:58')
    count2 = Sensor.objects.filter(Sensor_date__gte = '2016-10-01 11:58').count()

    sensors3 = Sensor.objects.filter(Sensor_date__gte = '2017-01-01 11:58')
    count3 = Sensor.objects.filter(Sensor_date__gte = '2017-01-01 11:58').count()

    sensors4 = Sensor.objects.filter(Sensor_date__gte = '2017-04-01 11:58')
    count4 = Sensor.objects.filter(Sensor_date__gte = '2017-04-01 11:58').count()

    sensors = Sensor.objects.filter(Sensor_date__gte = '2017-04-01 11:58')
    count = Sensor.objects.filter(Sensor_date__gte = '2017-04-01 11:58').count()

    avg_1=Sensor.objects.all().aggregate(Avg('Sensor_value'))
    max1=Sensor.objects.all().aggregate(Max('Sensor_value'))
    min1=Sensor.objects.all().aggregate(Min('Sensor_value'))
    avg1=round(avg_1.get('Sensor_value__avg'),3)
    #print avg1
    #raw_input("hello")

    context  = {
        "sensors1":sensors1,"count1":range(count1+1),"sensors2":sensors,"count2":range(count2+1),"sensors3":sensors,"count3":range(count3+1),"sensors4":sensors,"count4":range(count4+1),"sensors":sensors,"count":range(count+1),"avg1":avg1,"max1":max1,"min1":min1,
    }
    return render(request,"myapp/previous_data.html",context)


def previous2(request):
    #sensors = Sensor.objects.all().filter(Sensor.Sensor_date > "March 27, 2017, 11:57 a.m.")
    sensors1 = Sensorgroup2.objects.filter(Sensor_date__gte = '2016-03-29 11:58')
    count1 = Sensorgroup2.objects.filter(Sensor_date__gte = '2016-03-29 11:58').count()


    sensors2 = Sensorgroup2.objects.filter(Sensor_date__gte = '2016-10-01 11:58')
    count2 = Sensorgroup2.objects.filter(Sensor_date__gte = '2016-10-01 11:58').count()

    sensors3 = Sensorgroup2.objects.filter(Sensor_date__gte = '2017-01-01 11:58')
    count3 = Sensorgroup2.objects.filter(Sensor_date__gte = '2017-01-01 11:58').count()

    sensors4 = Sensorgroup2.objects.filter(Sensor_date__gte = '2017-04-01 11:58')
    count4 = Sensorgroup2.objects.filter(Sensor_date__gte = '2017-04-01 11:58').count()

    sensors = Sensorgroup2.objects.filter(Sensor_date__gte = '2017-04-01 11:58')
    count = Sensorgroup2.objects.filter(Sensor_date__gte = '2017-04-01 11:58').count()

    avg_1=Sensorgroup2.objects.all().aggregate(Avg('Sensor_value'))
    max1=Sensorgroup2.objects.all().aggregate(Max('Sensor_value'))
    min1=Sensorgroup2.objects.all().aggregate(Min('Sensor_value'))
    avg1=round(avg_1.get('Sensor_value__avg'),3)
    #print avg1
    #raw_input("hello")

    context  = {
        "sensors1":sensors1,"count1":range(count1+1),"sensors2":sensors,"count2":range(count2+1),"sensors3":sensors,"count3":range(count3+1),"sensors4":sensors,"count4":range(count4+1),"sensors":sensors,"count":range(count+1),"avg1":avg1,"max1":max1,"min1":min1,
    }
    return render(request,"myapp/g2_previous_data.html",context)




def multi(request):

    if request.method == 'POST':
        low = request.POST['low']
        high = request.POST['high']
    else:
        low='50'
        high='60'


    #sensors = Sensor.objects.all().filter(Sensor.Sensor_date > "March 27, 2017, 11:57 a.m.")
    sensors1 = Sensor.objects.filter(Sensor_value__lt = low)
    count1 = Sensor.objects.filter(Sensor_value__lt = low).count()
    sensors2 = Sensor.objects.filter(Sensor_value__gte = low,Sensor_value__lte = high)
    count2 = Sensor.objects.filter(Sensor_value__gte = low,Sensor_value__lte = high).count()
    sensors3 = Sensor.objects.filter(Sensor_value__gt = high)
    count3 = Sensor.objects.filter(Sensor_value__gt = high).count()

    context  = {
        "sensors1":sensors1,"count1":range(count1),"sensors2":sensors2,"count2":range(count2),"sensors3":sensors3,"count3":range(count3),'low':low,'high':high,

    }
    return render(request,"myapp/new_multi_data.html",context)


def multi2(request):

    if request.method == 'POST':
        low = request.POST['low']
        high = request.POST['high']
    else:
        low='50'
        high='60'


    #sensors = Sensor.objects.all().filter(Sensor.Sensor_date > "March 27, 2017, 11:57 a.m.")
    sensors1 = Sensorgroup2.objects.filter(Sensor_value__lt = low)
    count1 = Sensorgroup2.objects.filter(Sensor_value__lt = low).count()
    sensors2 = Sensorgroup2.objects.filter(Sensor_value__gte = low,Sensor_value__lte = high)
    count2 = Sensorgroup2.objects.filter(Sensor_value__gte = low,Sensor_value__lte = high).count()
    sensors3 = Sensorgroup2.objects.filter(Sensor_value__gt = high)
    count3 = Sensorgroup2.objects.filter(Sensor_value__gt = high).count()

    context  = {
        "sensors1":sensors1,"count1":range(count1),"sensors2":sensors2,"count2":range(count2),"sensors3":sensors3,"count3":range(count3),'low':low,'high':high,

    }
    return render(request,"myapp/group2_multi_data.html",context)



def  live(request):
        sensors1=Sensor.objects.all()
        count = Sensor.objects.all().count()

        sensors=sensors1.reverse()[count-1:]
        sensors2=sensors1.reverse()[count-5:]
	count2=sensors1.reverse()[count-5:].count()
	avg_1=sensors1.reverse()[count-5:].aggregate(Avg('Sensor_value'))
    	max1=sensors1.reverse()[count-5:].aggregate(Max('Sensor_value'))
    	min1=sensors2.aggregate(Min('Sensor_value'))
    	avg1=round(avg_1.get('Sensor_value__avg'),3)
	#print (max1)
	#print(avg1)
	#print(min1)
	#raw_input("hello")
        context  = {
        "sensors":sensors,"sensors2":sensors2,"count2":range(count2),"curr_time":datetime.datetime.now(),"avg1":avg1,"max1":max1,"min1":min1,
        }
        return render(request,"myapp/live_data.html",context)

def  live2(request):
        sensors1=Sensorgroup2.objects.all()
        count = Sensorgroup2.objects.all().count()

        sensors=sensors1.reverse()[count-1:]
        sensors2=sensors1.reverse()[count-5:]
	count2=sensors1.reverse()[count-5:].count()
	avg_1=sensors1.reverse()[count-5:].aggregate(Avg('Sensor_value'))
    	max1=sensors1.reverse()[count-5:].aggregate(Max('Sensor_value'))
    	min1=sensors2.aggregate(Min('Sensor_value'))
    	avg1=round(avg_1.get('Sensor_value__avg'),3)
	#print (max1)
	#print(avg1)
	#print(min1)
	#raw_input("hello")
        context  = {
        "sensors":sensors,"sensors2":sensors2,"count2":range(count2),"curr_time":datetime.datetime.now(),"avg1":avg1,"max1":max1,"min1":min1,
        }
        return render(request,"myapp/live2_data.html",context)

def  livemap(request):
        sensors1=Sensor.objects.all()
        count = Sensor.objects.all().count()

        sensors=sensors1.reverse()[count-1:]
        sensors2=sensors1.reverse()[count-5:]

        context  = {
        "sensors":sensors,"sensors2":sensors2,
        }
        return render(request,"myapp/live_map.html",context)


def index(request,name,value):

	temp_sen_data = Sensor()
	temp_sen_data2= Sensorgroup2()

	if (name=='z1s1'):

		temp_sen_data.Sensor_name = name
		temp_sen_data.Sensor_value = value
		temp_sen_data.save()
		if(int(value) > 40):
			to = 'sarvani.ch@iiits.in'
			gmail_user = 'its.group001'
			gmail_pwd = 'temporary'
			smtpserver = smtplib.SMTP("smtp.gmail.com",587)
			smtpserver.ehlo()
			smtpserver.starttls()
			smtpserver.ehlo
			smtpserver.login(gmail_user, gmail_pwd)
			header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:WARNING FROM SENSOR '+name+'\n'
			print header
			msg = header + '\n value exceeded 90 Kindly take measures \n\n'
			smtpserver.sendmail(gmail_user, to, msg)
			print 'done!'
			smtpserver.close()

		return HttpResponse("<h3>the data is entered</h3>")
	elif(name=='z1s2'):

		temp_sen_data2.Sensor_name = name
		temp_sen_data2.Sensor_value = value
		temp_sen_data2.save()
		if(int(value) > 40):
			to = 'sarvani.ch@iiits.in'
			gmail_user = 'its.group001'
			gmail_pwd = 'temporary'
			smtpserver = smtplib.SMTP("smtp.gmail.com",587)
			smtpserver.ehlo()
			smtpserver.starttls()
			smtpserver.ehlo
			smtpserver.login(gmail_user, gmail_pwd)
			header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:WARNING FROM SENSOR '+name+'\n'
			print header
			msg = header + '\n value exceeded 90 Kindly take measures \n\n'
			smtpserver.sendmail(gmail_user, to, msg)
			print 'done!'
			smtpserver.close()

		return HttpResponse("<h3>the data is entered</h3>")
	else:
		return HttpResponse("<h3>the data is NOT entered</h3>")
