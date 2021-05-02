from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import police, criminal

# Create your views here.
pol = police.objects.all()
C = criminal.objects.all()
pname = {}
cn = ""


def true(uname):
    for na in pol:
        if na.email == uname:
            print("If true so number:", na)


def index2(request):
    if request.method == 'POST':
        searchC = request.POST['searchC']

        if criminal.objects.filter(name=searchC).exists():
            messages.warning(request, "Criminal Found ")
            global cn
            cn = searchC
    return redirect('index')


def index(request):

    if request.method == 'POST':
        name = request.POST['name']
        gender = request.POST['gender']
        contact = request.POST['contact']
        relativeContact = request.POST['relativeContact']
        image = request.FILES['image']
        address = request.POST['address']
        crimeDetail = request.POST['crimeDetail']
        # searchC = request.POST['searchC']
        # print('################### SearchC:', searchC)

        # return render(request, 'index.html')

        if criminal.objects.filter(name=name).exists():
            messages.warning(request, "Criminal Already Exists")
            return redirect('index')
        else:
            Cr = criminal.objects.create_user(
                name=name, gender=gender, image=image, contact=contact, relativeContact=relativeContact, crimeDetail=crimeDetail, address=address)
            print("Criminal Name:", name)
            print("Gender:", gender)
            print("Contact:", contact)
            print("Relative Contact:", relativeContact)
            print("Crime Detail:", crimeDetail)
            print("Crime Address:", address)
            print(Cr)
            # pol.is_active = False
            Cr.save()
            print("Created CREATED")
            messages.success(request, 'Criminal Registered Successfully')
        return redirect('')
    else:
        # return HttpResponse("This is homePage")
        return render(request, 'index.html', {'pol': pol, 'na': pname, 'C': C, 'cn': cn})


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
        searchC = request.POST['searchC']

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

        if police.objects.filter(email=email).exists() & police.objects.filter(password=password).exists():
            data = {}
            messages.success(request, "Login Success")
            # pol = police.objects.filter(email=email).values()
            # print("XXXXXXXX:", pol)
            true(email)
            for na in pol:
                if na.email == email:
                    data = na
            print('=========:', data)
            global pname
            pname = data
            print(pname)
            # return render(request, 'index.html', {'pol': pol, 'na': data, 'C': C})
            return redirect('index')
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
