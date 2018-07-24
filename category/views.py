from django.shortcuts import render,redirect,HttpResponse
import operator
from sale import settings
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from category.forms import RegistrationForm,EditProfileForm
from computer.models import Item as Dat
from automobiles.models import Item as Amob
from mobiles.models import Item as Mob
from electronics.models import Item as Elec
from apparels.models import Item as Appa

def index(request):
    data = Dat.objects.all().order_by('-pk')[0:3]
    dataa= Dat.objects.all().order_by('-pk')[4:7]
    datab = Dat.objects.all().order_by('-pk')[8:11]
    data1= Amob.objects.all().order_by('-pk')[0:3]
    data1a = Amob.objects.all().order_by('-pk')[4:7]
    data1b = Amob.objects.all().order_by('-pk')[8:11]
    data2 = Mob.objects.all().order_by('-pk')[0:3]
    data2a = Mob.objects.all().order_by('-pk')[4:7]
    data2b = Mob.objects.all().order_by('-pk')[8:11]
    data3 = Appa.objects.all().order_by('-pk')[0:3]
    data3a = Appa.objects.all().order_by('-pk')[4:7]
    data3b = Appa.objects.all().order_by('-pk')[8:11]
    data4 = Elec.objects.all().order_by('-pk')[0:3]
    data4a = Elec.objects.all().order_by('-pk')[4:7]
    data4b = Elec.objects.all().order_by('-pk')[8:11]


    context = {'item_list':data,'item_lista':dataa,'item_listb':datab ,'item_list1':data1,'item_list1a':data1a,'item_list1b':data1b,'item_list2':data2,'item_list2a':data2a,'item_list2b':data2b,'item_list3':data3,'item_list3a':data3a,'item_list3b':data3b,'item_list4':data4,'item_list4a':data4a,'item_list4b':data4b, }
    return render(request, 'category/index.html', context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/categry')

    else:
        form= RegistrationForm()

        args= {'form':form}
        return render(request,'category/reg_form.html',args)


def login(request):
    if request.method == 'GET':
        form = UserCreationForm(request.GET)
        if form.is_valid():
            form.save()
            return redirect('/categry')

    else:
        form= UserCreationForm()

        args= {'form':form}
        return render(request,'category/login.html',args)

def logout(request):
    return render(request, 'category/logout.html')

@login_required
def view_profile(request):
    args ={'user:request.user'}
    return render(request,'category/profile.html',args)

def view_profile(request):
    args={'user':request.user}
    return render(request,'category/profile.html',args)

def edit_profile(request):
    if request.method == 'POST':
        form=EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/categry/profile')
    else:
        form=EditProfileForm(instance= request.user)
        args={'form':form}
        return render(request,'category/edit_profile.html',args)


