from django.shortcuts import render, redirect
from .models import RegModel,Address
# Create your views here.

def indexr(request):
    return render(request, 'index.html')

def regr(request):
    return render(request, 'register.html')

def doctor_reg(request):
    return render(request, 'doctor-reg.html')

def patient_reg(request):
    return render(request, 'patient-reg.html')

def reg(request):
    if request.method == 'POST':
        fn=request.POST.get('fname')
        ln=request.POST.get('lname')
        pic=request.FILES['propic']
        un=request.POST.get('uname')
        em=request.POST.get('mail')
        pas=request.POST.get('cpsw')
        line=request.POST.get('line1')
        city=request.POST.get('city')
        state=request.POST.get('state')
        pincode=request.POST.get('pincode')
        type=request.POST.get('utype')

        user_instance=RegModel(fname=fn,lname=ln,propic=pic,uname=un,email=em,psw=pas,utype=type)
        user_instance.save()
        Address(user=user_instance,line=line,city=city,state=state,pincode=pincode).save()
    return redirect(indexr)


def loginr(request):
    return render(request,'login.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['psw']
        try:
            user = RegModel.objects.get(uname=username, psw=password)
            request.session['user_id'] = user.id
            address = Address.objects.get(user=user)
            if user.utype == 'doctor':
                return render(request, 'doctor-dashboard.html', {'data': user,'address': address})
            else:
                return render(request, 'patient-dashboard.html', {'data': user,'address': address})

        except RegModel.DoesNotExist:
            error_message = "Invalid username or password. Please try again."
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')


def logout(request):
    del request.session['user_id']
    return redirect(indexr)
