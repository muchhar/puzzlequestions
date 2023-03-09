from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context, Template,RequestContext
import datetime
from django.views.decorators import csrf
import time
from django.views.decorators.csrf import csrf_exempt



def index(request):
	a={'product':'rrbclerk','rrbpo':'rrbpo','ibpsclerk':'ibpsclerk','ibpspo':'ibpspo','rrbclerkmain':'rrbclerkmain','rrbpomain':'rrbpomain','ibpsclerkmain':'ibpsclerkmain','ibpspomain':'ibpspomain','sbipo':'sbipo','sbiclerk':'sbiclerk','sbipomain':'sbipomain','sbiclerkmain':'sbiclerkmain'}
	  

	return render(request,'usersite/index.html',{'a':a})



def puzzlelist(request,fd):
	a={'product':'rrbclerk','rrbpo':'rrbpo','ibpsclerk':'ibpsclerk','ibpspo':'ibpspo','rrbclerkmain':'rrbclerkmain','rrbpomain':'rrbpomain','ibpsclerkmain':'ibpsclerkmain','ibpspomain':'ibpspomain','sbipo':'sbipo','sbiclerk':'sbiclerk','sbipomain':'sbipomain','sbiclerkmain':'sbiclerkmain'}
	
	lbl=''
	if fd=='rrbclerk':
		log=product.objects.all()
	
		lbl="IBPS RRB CLERK PRELIMS"
	elif fd=='rrbpo':
		log=rrbpo.objects.all()
		lbl="IBPS RRB PO PRELIMS"
	elif fd=='ibpsclerk':
		log=ibpsclerk.objects.all()
		lbl="IBPS CLERK PRELIMS"
	elif fd=='ibpspo':
		log=ibpspo.objects.all()
		lbl="IBPS PO PRELIMS"
	##############################
	elif fd=='rrbclerkmain':
		log=rrbclerkmain.objects.all()
		lbl="RRB CLERK MAINS"
	elif fd=='rrbpomain':
		log=rrbpomain.objects.all()
		lbl="RRB PO MAINS"
	elif fd=='ibpsclerkmain':
		log=ibpsclerkmain.objects.all()
		lbl="IBPS CLERK MAINS"
	elif fd=='ibpspomain':
		log=ibpspomain.objects.all()
		lbl="IBPS PO MAINS"

	elif fd=='sbiclerk':
		log=sbiclerk.objects.all()
		lbl="SBI CLERK PRELIMS"
	elif fd=='sbipo':
		log=sbipo.objects.all()
		lbl="SBI PO PRELIMS"
	elif fd=='sbiclerkmain':
		log=sbiclerkmain.objects.all()
		lbl="SBI CLERK MAINS"
	elif fd=='sbipomain':
		log=sbipomain.objects.all()
		lbl="SBI PO MAINS"

	################################
	det=[0]
	
	

	jo=0
	for i in log:
		jo=jo+1
		if str(i.id)+'_'+str(fd) in request.session:

		
			fav_color = request.session[str(str(i.id)+'_'+str(fd))]
			i.time=fav_color
		else:
			i.time="--:--"
		i.numr=jo

	
	return render(request,'usersite/rrbclerk.html',{'cart':log,'fd':fd,'lbl':lbl,'a':a})


@csrf_exempt
def puzzle(request,fd2,ped):
	fd=fd2
	
	if fd=='rrbclerk':
		log2=product.objects.all()
		pi=product.objects.get(id=ped)
	elif fd=='rrbpo':
		log2=rrbpo.objects.all()
		pi=rrbpo.objects.get(id=ped)
	elif fd=='ibpsclerk':
		log2=ibpsclerk.objects.all()
		pi=ibpsclerk.objects.get(id=ped)
	elif fd=='ibpspo':
		log2=ibpspo.objects.all()
		pi=ibpspo.objects.get(id=ped)
	##############################
	elif fd=='rrbclerkmain':
		log2=rrbclerkmain.objects.all()
		pi=rrbclerkmain.objects.get(id=ped)
	elif fd=='rrbpomain':
		log2=rrbpomain.objects.all()
		pi=rrbpomain.objects.get(id=ped)
	elif fd=='ibpsclerkmain':
		log2=ibpsclerkmain.objects.all()
		pi=ibpsclerkmain.objects.get(id=ped)
	elif fd=='ibpspomain':
		log2=ibpspomain.objects.all()
		pi=ibpspomain.objects.get(id=ped)

	elif fd=='sbiclerk':
		log2=sbiclerk.objects.all()
		pi=sbiclerk.objects.get(id=ped)
	elif fd=='sbipo':
		log2=sbipo.objects.all()
		pi=sbipo.objects.get(id=ped)
	elif fd=='sbiclerkmain':
		log2=sbiclerkmain.objects.all()
		pi=sbiclerkmain.objects.get(id=ped)
	elif fd=='sbipomain':
		log2=sbipomain.objects.all()
		pi=sbipomain.objects.get(id=ped)

	guy=[]
	jt=0
	for jr in log2:
		jt=jt+1
		if str(jr.id)==ped:
			vat=jt
		guy.append(str(jr.id))
	
	
	if request.method=="POST":
		num=request.POST.get('time')
		q1=request.POST.get('op')
		q2=request.POST.get('op2')
		q3=request.POST.get('op3')
		q4=request.POST.get('op4')
		q5=request.POST.get('op5')
		img_state=request.POST.get('img_state')


		#nex=int(ped)+1

		#if nex>len(log2):
		#	nex=1
		#else:
		#	pass
		if ped==guy[-1]:
			nex=guy[0]
		else:
			jp=0
			for uv in guy:
				if jp==1:
					nex=uv
					break
				if uv==ped:
					jp=1


		

		###########################

		right=0
		wrong=0
		if q1==pi.question1_answer:
			right=1+right
		else:
			wrong=1+wrong
		if q2==pi.question2_answer:
			right=1+right
		else:
			wrong=1+wrong
		if q3==pi.question3_answer:
			right=1+right
		else:
			wrong=1+wrong
		if q4==pi.question4_answer:
			right=1+right
		else:
			wrong=1+wrong
		if q5==pi.question5_answer:
			right=1+right
		else:
			wrong=1+wrong
		
		#response
		resp1="Unknow" ##time
		resp="Unknow" ##ques

		#####by time###############
		if num[0]=='0' and (num[1]=='0' or num[1]=='1' or num[1]=='2') :
			resp1="Excellent Timing,"

			#resp="Very Poor! Keep Try!"
		elif num[0]=='0' and num[1]=='3':
			resp1="Very Good Timing,"
		elif num[0]=='0' and num[1]=='4':
			resp1="Good Timing,"
		elif num[0]=='0' and num[1]=='5':
			resp1="Average Timing,"
		else:
			resp1="Poor Timing,"

		
			
		########################
		if right<3:
			resp="Very Poor Accuracy!"
		elif right==3 or right==4:
			resp=resp1+ " Increase your Accuracy"

		elif right==5:
			resp= resp1+" Excellent Accuracy"

		
		#########
		if img_state=='0':
			
			request.session[str(ped)+'_'+str(fd)] = 'Correct:'+str(right) + ' | Time:'+ num
		elif str(ped)+'_'+str(fd) in request.session:
			pass
		else:
			request.session[str(ped)+'_'+str(fd)] = "Answer Viewed!"


		#print("quatin1 ans====",pi.question1_answer)
		return render(request,'usersite/result.html',{'time':num,'sol':pi,'right':right,'wrong':wrong,'res':resp,'next':nex,'a':fd2})
	else:
		pass


	return render(request,'usersite/puzzle.html',{'puz':pi,'vat':vat})


#result display page
#def result(request):
	#return render(request,'usersite/result.html')