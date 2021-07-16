from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.views.generic.detail import DetailView
from django.contrib.auth.models import Group,User
from django.contrib import messages
from .forms import createUserForm,addProductForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,allowed_users,admin_only

# Create your views here.

#inherit home page
def inherit(request):
    return render(request, 'inherit.html')

#Login and Register
@unauthenticated_user
def theLogin(request):

    #REGISTRATION
    reg_form = createUserForm()

    if request.method == 'POST':
        reg_form = createUserForm(request.POST)
        if reg_form.is_valid():
            newUser = reg_form.save()

            #Adding To Group(Customers)
            group = Group.objects.get(name='customer')
            newUser.groups.add(group)
            
            #Creating a customer
            Profile.objects.create(
                user=newUser,
            )

            #Auto Login
            username = reg_form.cleaned_data.get('username')
            password = reg_form.cleaned_data.get('password1')

            userreg = authenticate(username=username, password=password)
            login(request, userreg)
            return redirect('adminProf')

    context = {'reg_form':reg_form}

    #LOGIN SECTION
    if request.method == 'POST':

        username1 = request.POST.get('username')
        password1 = request.POST.get('password')

        user1 = authenticate(username=username1, password=password1)

        if user1 is not None:
            login(request, user1)
            return redirect('adminProf')
        else:
            messages.info(request, 'Username Or Password Is INCORRECT!!!')   

    return render(request, 'login.html', context)  

#logout user 
def logOutUser(request):
    logout(request)    
    return redirect('login')

#Cart
def cart(request):
    return render(request, 'cart.html')    

#Pannel Inherit
@login_required(login_url='login')
def pannelInherit(request):
    return render(request, 'Pannel/panHerit.html')    

#Admin Profile
@login_required(login_url='login')
def adminProf(request):

    #all customers
    profiles = Profile.objects.all()
    allProfiles = profiles.count()

    #all products
    products = Products.objects.all()
    allProducts = products.count()

    context = {'allProfiles':allProfiles, 'allProducts':allProducts}

    return render(request, 'Pannel/profile.html', context) 

#All Customers in a List
@login_required(login_url='login')
@admin_only
def allCustomers(request):

    profiles = Profile.objects.all()

    context = {'profiles':profiles}

    return render(request, 'Pannel/customers.html',context)


#Customer Delete
@login_required(login_url='login')
@admin_only
def delCustomer(request, username):

    specificCust = User.objects.get(username = username)

    context = {'specificCust':specificCust }

    if request.method == 'POST':
        specificCust.delete()
        return redirect('allCustomers')
        

    return render(request, 'Pannel/delCust.html', context)


#Add Product 
@login_required(login_url='login')
@admin_only
def addProduct(request):

    productAddForm = addProductForm()
    if request.method == 'POST':
        productAddForm = addProductForm(request.POST, request.FILES)
        if productAddForm.is_valid():
            productAddForm.save()

    context = {'productAddForm':productAddForm}

    return render(request, 'Pannel/addproducts.html', context)


#A single shoe detail
class shoeInfo(DetailView):
    model = Products
    template_name = 'Pannel/shoeInf.html'
    context_object_name = 'productDesc'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        productUp = Products.objects.get(pk=self.kwargs.get('pk'))

        return context


#All Products in a List
def allProducts(request):

    products = Products.objects.all()

    context = {'products':products}

    return render(request, 'products.html', context)    


#delete products
@login_required(login_url='login')
@admin_only
def delProduct(request, pk):
    
    specProd = Products.objects.get(shoe_id=pk)

    context = {'specProd':specProd}

    if request.method == 'POST':
        specProd.delete()
        return redirect('allProducts')

    return render(request, 'Pannel/delProduct.html', context)    