from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import DetailsForm, IOTForm, EHForm, ARForm, MLForm
from .models import Detail, IOT, EH, AR, ML

abc = None
xyz=None
pqr=None

# Create your views here.
@login_required(login_url='/login')
def details(request):
    if request.method == 'POST':
        form = DetailsForm(request.POST)
        post = Detail()
        global abc
        global pqr
        global xyz
        abc=request.POST.get('name')
        xyz=request.POST.get('phone')
        pqr=request.POST.get('course')
        post.course = request.POST.get('course')
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
        return redirect("/details/{}/".format(str(post.course)))
    else:
        form = DetailsForm()
        return render(request, 'fpage/details.html')


@login_required(login_url='/details')
def iot(request):
    ch = 0
    
    if request.method == 'POST':
        form = IOTForm(request.POST)
        post = Detail
        
        
        
        post.q1 = request.POST.get('q1')
        IOT.objects.filter(name=abc, phone=xyz).update(q1=post.q1)
        if post.q1=='1':
            ch+=1
            IOT.objects.filter(name=abc, phone=xyz).update(score=ch)
        
        post.q2 = request.POST.get('q2')
        IOT.objects.filter(name=abc, phone=xyz).update(q2=post.q2)
        if post.q2=='2':
            ch+=1
            IOT.objects.filter(name=abc, phone=xyz).update(score=ch)
        
        post.q3 = request.POST.get('q3')
        IOT.objects.filter(name=abc, phone=xyz).update(q3=post.q3)
        if post.q3=='3':
            ch+=1
            IOT.objects.filter(name=abc, phone=xyz).update(score=ch)
        
        post.q4 = request.POST.get('q4')
        IOT.objects.filter(name=abc, phone=xyz).update(q4=post.q4)
        if post.q4=='4':
            ch+=1
            IOT.objects.filter(name=abc, phone=xyz).update(score=ch)
        
        post.q5 = request.POST.get('q5')
        IOT.objects.filter(name=abc, phone=xyz).update(q5=post.q5)
        if post.q5=='1':
            ch+=1
            IOT.objects.filter(name=abc, phone=xyz).update(score=ch)
        
        post.q6 = request.POST.get('q6')
        IOT.objects.filter(name=abc, phone=xyz).update(q6=post.q6)
        if post.q6=='2':
            ch+=1
            IOT.objects.filter(name=abc, phone=xyz).update(score=ch)

        post.q7 = request.POST.get('q7')
        IOT.objects.filter(name=abc, phone=xyz).update(q7=post.q7)
        if post.q7=='3':
            ch+=1
            IOT.objects.filter(name=abc, phone=xyz).update(score=ch)
        
        post.q8 = request.POST.get('q8')
        IOT.objects.filter(name=abc, phone=xyz).update(q8=post.q8)
        if post.q8=='4':
            ch+=1
            IOT.objects.filter(name=abc, phone=xyz).update(score=ch)

        post.q9 = request.POST.get('q9')
        IOT.objects.filter(name=abc, phone=xyz).update(q9=post.q9)
        if post.q9=='1':
            ch+=1
            IOT.objects.filter(name=abc, phone=xyz).update(score=ch)

        post.q10 = request.POST.get('q10')
        IOT.objects.filter(name=abc, phone=xyz).update(q10=post.q10)
        if post.q10=='4':
            ch+=1
            IOT.objects.filter(name=abc, phone=xyz).update(score=ch)
        
        Detail.objects.filter(name=abc,phone=xyz,course=pqr).update(score=ch)
        IOT.objects.filter(name=abc, phone=xyz).update(score=ch)
        return redirect('/logout/')
    else:
        post2 = IOT(name=abc, phone=xyz)
        post2.user = request.user
        post2.save()
        return render(request, 'quest/IOT.html')


@login_required(login_url='/details')
def eh(request):
    ch = 0
    if request.method == 'POST':
        form = EHForm(request.POST)
        post = Detail
        
        post.q1 = request.POST.get('q1')
        EH.objects.filter(name=abc, phone=xyz).update(q1=post.q1)
        if post.q1=='1':
            ch+=1
            EH.objects.filter(name=abc,phone=xyz).update(score=ch)
        
        post.q2 = request.POST.get('q2')
        EH.objects.filter(name=abc, phone=xyz).update(q2=post.q2)
        if post.q2=='2':
            ch+=1
            EH.objects.filter(name=abc,phone=xyz).update(score=ch)
        
        post.q3 = request.POST.get('q3')
        EH.objects.filter(name=abc, phone=xyz).update(q3=post.q3)
        if post.q3=='3':
            ch+=1
            EH.objects.filter(name=abc,phone=xyz).update(score=ch)
        
        post.q4 = request.POST.get('q4')
        EH.objects.filter(name=abc, phone=xyz).update(q4=post.q4)
        if post.q4=='4':
            ch+=1
            EH.objects.filter(name=abc,phone=xyz).update(score=ch)
        
        post.q5 = request.POST.get('q5')
        EH.objects.filter(name=abc, phone=xyz).update(q5=post.q5)
        if post.q5=='1':
            ch+=1
            EH.objects.filter(name=abc,phone=xyz).update(score=ch)
        
        post.q6 = request.POST.get('q6')
        EH.objects.filter(name=abc, phone=xyz).update(q6=post.q6)
        if post.q6=='2':
            ch+=1
            EH.objects.filter(name=abc,phone=xyz).update(score=ch)

        post.q7 = request.POST.get('q7')
        EH.objects.filter(name=abc, phone=xyz).update(q7=post.q7)
        if post.q7=='3':
            ch+=1
            EH.objects.filter(name=abc,phone=xyz).update(score=ch)
        
        post.q8 = request.POST.get('q8')
        EH.objects.filter(name=abc, phone=xyz).update(q8=post.q8)
        if post.q8=='4':
            ch+=1
            EH.objects.filter(name=abc,phone=xyz).update(score=ch)

        post.q9 = request.POST.get('q9')
        EH.objects.filter(name=abc, phone=xyz).update(q9=post.q9)
        if post.q9=='1':
            ch+=1
            EH.objects.filter(name=abc,phone=xyz).update(score=ch)

        post.q10 = request.POST.get('q10')
        EH.objects.filter(name=abc, phone=xyz).update(q10=post.q10)
        if post.q10=='4':
            ch+=1
            EH.objects.filter(name=abc,phone=xyz).update(score=ch)
        
        Detail.objects.filter(name=abc,phone=xyz,course=pqr).update(score=ch)
        EH.objects.filter(name=abc,phone=xyz).update(score=ch)
        return redirect('/logout/')
    else:
        post2 = EH(name=abc, phone=xyz)
        post2.user = request.user
        post2.save()
        return render(request, 'quest/EH.html')

    

@login_required(login_url='/details')
def ar(request):
    ch = 0
    if request.method == 'POST':
        form = ARForm(request.POST)
        post = Detail
        
        
        post.q1 = request.POST.get('q1')
        AR.objects.filter(name=abc, phone=xyz).update(q1=post.q1)
        if post.q1=='1':
            ch+=1
            AR.objects.filter(name=abc,phone=xyz).update(score=ch)
        
        post.q2 = request.POST.get('q2')
        AR.objects.filter(name=abc, phone=xyz).update(q2=post.q2)
        if post.q2=='2':
            ch+=1
            AR.objects.filter(name=abc,phone=xyz).update(score=ch)
        
        post.q3 = request.POST.get('q3')
        AR.objects.filter(name=abc, phone=xyz).update(q3=post.q3)
        if post.q3=='3':
            ch+=1
            AR.objects.filter(name=abc,phone=xyz).update(score=ch)
        
        post.q4 = request.POST.get('q4')
        AR.objects.filter(name=abc, phone=xyz).update(q4=post.q4)
        if post.q4=='4':
            ch+=1
            AR.objects.filter(name=abc,phone=xyz).update(score=ch)
        
        post.q5 = request.POST.get('q5')
        AR.objects.filter(name=abc, phone=xyz).update(q5=post.q5)
        if post.q5=='1':
            ch+=1
            AR.objects.filter(name=abc,phone=xyz).update(score=ch)
        
        post.q6 = request.POST.get('q6')
        AR.objects.filter(name=abc, phone=xyz).update(q6=post.q6)
        if post.q6=='2':
            ch+=1
            AR.objects.filter(name=abc,phone=xyz).update(score=ch)

        post.q7 = request.POST.get('q7')
        AR.objects.filter(name=abc, phone=xyz).update(q7=post.q7)
        if post.q7=='3':
            ch+=1
            AR.objects.filter(name=abc,phone=xyz).update(score=ch)
        
        post.q8 = request.POST.get('q8')
        AR.objects.filter(name=abc, phone=xyz).update(q8=post.q8)
        if post.q8=='4':
            ch+=1
            AR.objects.filter(name=abc,phone=xyz).update(score=ch)

        post.q9 = request.POST.get('q9')
        AR.objects.filter(name=abc, phone=xyz).update(q9=post.q9)
        if post.q9=='1':
            ch+=1
            AR.objects.filter(name=abc,phone=xyz).update(score=ch)

        post.q10 = request.POST.get('q10')
        AR.objects.filter(name=abc, phone=xyz).update(q10=post.q10)
        if post.q10=='4':
            ch+=1
            AR.objects.filter(name=abc,phone=xyz).update(score=ch)
        
        Detail.objects.filter(name=abc,phone=xyz,course=pqr).update(score=ch)
        AR.objects.filter(name=abc,phone=xyz).update(score=ch)
        return redirect('/logout/')
    else:
        post2 = AR(name=abc, phone=xyz)
        post2.user = request.user
        post2.save()
        return render(request, 'quest/AR.html')



@login_required(login_url='/details')
def ml(request):
    ch = 0
    if request.method == 'POST':
        form = MLForm(request.POST)
        post = Detail
        
        
        post.q1 = request.POST.get('q1')
        ML.objects.filter(name=abc, phone=xyz).update(q1=post.q1)
        if post.q1=='1':
            ch+=1
            ML.objects.filter(name=abc,phone=xyz).update(score=ch)
        
        post.q2 = request.POST.get('q2')
        ML.objects.filter(name=abc, phone=xyz).update(q2=post.q2)
        if post.q2=='2':
            ch+=1
            ML.objects.filter(name=abc,phone=xyz).update(score=ch)
        
        post.q3 = request.POST.get('q3')
        ML.objects.filter(name=abc, phone=xyz).update(q3=post.q3)
        if post.q3=='3':
            ch+=1
            ML.objects.filter(name=abc,phone=xyz).update(score=ch)
        
        post.q4 = request.POST.get('q4')
        ML.objects.filter(name=abc, phone=xyz).update(q4=post.q4)
        if post.q4=='4':
            ch+=1
            ML.objects.filter(name=abc,phone=xyz).update(score=ch)
        
        post.q5 = request.POST.get('q5')
        ML.objects.filter(name=abc, phone=xyz).update(q5=post.q5)
        if post.q5=='1':
            ch+=1
            ML.objects.filter(name=abc,phone=xyz).update(score=ch)
        
        post.q6 = request.POST.get('q6')
        ML.objects.filter(name=abc, phone=xyz).update(q6=post.q6)
        if post.q6=='2':
            ch+=1
            ML.objects.filter(name=abc,phone=xyz).update(score=ch)

        post.q7 = request.POST.get('q7')
        ML.objects.filter(name=abc, phone=xyz).update(q7=post.q7)
        if post.q7=='3':
            ch+=1
            ML.objects.filter(name=abc,phone=xyz).update(score=ch)
        
        post.q8 = request.POST.get('q8')
        ML.objects.filter(name=abc, phone=xyz).update(q8=post.q8)
        if post.q8=='4':
            ch+=1
            ML.objects.filter(name=abc,phone=xyz).update(score=ch)

        post.q9 = request.POST.get('q9')
        ML.objects.filter(name=abc, phone=xyz).update(q9=post.q9)
        if post.q9=='1':
            ch+=1
            ML.objects.filter(name=abc,phone=xyz).update(score=ch)

        post.q10 = request.POST.get('q10')
        ML.objects.filter(name=abc, phone=xyz).update(q10=post.q10)
        if post.q10=='4':
            ch+=1
            ML.objects.filter(name=abc,phone=xyz).update(score=ch)
        
        Detail.objects.filter(name=abc,phone=xyz,course=pqr).update(score=ch)
        ML.objects.filter(name=abc,phone=xyz).update(score=ch)
        return redirect('/logout/')
    else:
        post2 = ML(name=abc, phone=xyz)
        post2.user = request.user
        post2.save()
        return render(request, 'quest/ML.html')




