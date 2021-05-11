from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import police, criminal, searches
from .ml import *
from playsound import playsound

# Create your views here.
pol = police.objects.all()
C = criminal.objects.all()
pname = {}
cn = ""
crn = ""


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
    playsound("static./yw.mp3")
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
    if pname == NULL:
        global cn
        cn = ""

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

        if police.objects.filter(email=email).exists() & police.objects.filter(password=password).exists():
            data = {}
            messages.success(request, "Login Success")

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


def sbp(request):
    crn = "NOT"
    if request.method == 'POST':
        image = request.FILES['image']
        print("XXXXXXX", image)
        toSearch = "Searched_Criminals/" + str(image)
        print("To Search bef check:", toSearch)
        if searches.objects.filter(image=image).exists():
            messages.warning(request, "Change Image Name")
        else:

            S = searches.objects.addImg(
                image=image)
            # S.save()
            # messages.success(request, "Image Saved")
            print("SAved image as:", toSearch)
            # print(f'../media/{toSearch}')
            crn = detect(toSearch)
            if crn == 'NOT FOUND':
                messages.warning(request, "Criminal Not Found In Database")
                crn = "NOT FOUND"
                playsound('static/cnf.mp3')
            else:
                messages.warning(request, "Criminal Found")
                print(f'Data agaya :{crn}')
                crn = "Criminal_Images/" + crn
                print("AB KYA AYA:", crn)
                crn = criminal.objects.filter(image=crn).values('name')
                print('##########', crn)
                playsound('static/audio.mp3')
                playsound('static/dcf.mp3')

            # global cn
        print("To Search af check:", toSearch)
    print("im working")
    return render(request, 'sbp.html', {'pol': pol, 'na': pname, 'C': C, 'crn': crn})


def logout(request):
    auth.logout(request)
    messages.success(request, "Logut Success")

    return redirect('login')
