from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import police, criminal

# Create your views here.
pol = police.objects.all()
C = criminal.objects.all()


def true(uname):
    for na in pol:
        if na.email == uname:
            print("If true so number:", na)


def index(request):

    # return HttpResponse("This is homePage")
    # print("IDHAR HAI KYA:", email)

    return render(request, 'index.html', {'pol': pol, 'C': C})


def register(request):

    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['username']
        gender = request.POST['gender']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        image = request.FILES['image']
        idPic = request.FILES['idPic']
        position = request.POST['position']
        contact = request.POST['contact']

        if password1 == password2:
            if police.objects.filter(name=name).exists():
                messages.warning(request, "User Is Already Registered")
                return redirect('login')
            elif police.objects.filter(email=email).exists():
                messages.warning(request, 'Email already Regisered')
            else:
                pol = police.objects.create_user(
                    name=name, password=password1, gender=gender, email=email, image=image, idCardImg=idPic, contact=contact, position=position)
                print("Username:", name)
                print("password:", password1)
                print("email:", email)
                print(pol)
                # pol.is_active = False
                pol.save()
                print("USER CREATED")
                messages.success(request, 'User Registered Successfully')
        else:
            messages.warning(request, 'Password Missmatch')
            print("Password Missmatch")
        return redirect('login')
    else:
        # return HttpResponse("This is homePage")
        return render(request, 'login.html')


def login(request):

    if request.method == 'POST':

        email = request.POST['email']
        # email = request.POST['email']
        password = request.POST['password']
        # print("name Entered:",username)
        # print("email:", username)
        print("Password:", password)

        # user = auth.authenticate(email=email,password=password)

        # user = auth.authenticate(username=username, password=password)

        # if user is not None:
        #     auth.login(request, user)
        #     messages.success(request, "Login Successfull")
        #     print(user)
        #     return redirect('index')
        # else:
        #     messages.warning(request, 'Invalid Credentials')
        #     print(user)
        #     return redirect('login')

        if police.objects.filter(email=email).exists():
            data = {}
            messages.success(request, "Login Success")
            # pol = police.objects.filter(email=email).values()
            # print("XXXXXXXX:", pol)
            true(email)
            for na in pol:
                if na.email == email:
                    data = na
            print('=========:', na)
            return render(request, 'index.html', {'pol': pol, 'na': data, 'C': C})
            # return redirect('index')
        else:
            messages.warning(request, 'Invalid Credentials')
            return redirect('login')

    else:
        # return HttpResponse("This is homePage")
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    messages.success(request, "Logut Success")

    return redirect('login')
