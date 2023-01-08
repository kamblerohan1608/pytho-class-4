from django.shortcuts import redirect, render
from django.views import View
from .models import ProductCategory,ProductModel
from .forms import LoginForm,RegisterForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
import re

# Create your views here.

class home(View):

    def get(self,request):

        data = ProductCategory.objects.all()
        men_ptr = r"Men's[A-z a-z]*"
        women_ptr = r"Women's[A-z a-z]*"
        kids_ptr = r"Kids's[A-z a-z]*"
        other_ptr = r"Other[A-z a-z]*"

        all_data_str = ""
        for i in data:
            all_data_str = all_data_str + "," + str(i)
        print(all_data_str)

        mens_cat = re.findall(men_ptr,all_data_str)
        print(mens_cat)
        womens_cat = re.findall(women_ptr,all_data_str)
        print(womens_cat)
        kids_cat = re.findall(kids_ptr,all_data_str)
        print(kids_cat)
        other = re.findall(other_ptr,all_data_str)
        print(other)

        men_cat_id = []
        women_cat_id = []
        kids_cat_id = []
        others_cat_id =[]


        for i in data:
            if str(i) in mens_cat:
                men_cat_id.append(data.get(id=i.id))

        for i in data:
            if str(i) in womens_cat:
                women_cat_id.append(data.get(id=i.id))

        # for i in data:
        #     if str(i) in mens_cat:
        #         men_cat_id.append(data.get(id=i.id))

        # for i in data:
        #     if str(i) in mens_cat:
        #         men_cat_id.append(data.get(id=i.id))



        print(men_cat_id)
        print(women_cat_id)                

        # data.filter()
            


        return render(request,'oneapp/home.html',{'men_data':men_cat_id,'women_data':women_cat_id})
        
    def post(self,request):
        pass


class all_products(View):

    def get(self,request):
        
        data = ProductModel.objects.all()
        # print(data.p_brand)

        return render(request,'oneapp/all_products.html',{'data':data})

    def post(self,request):
        pass


class display_products(View):

    def get(self,request,category_name):
        
        # print(category_name)

        cat_id = ProductCategory.objects.get(product_catagory = category_name)
        # print(cat_id.id)

        category_all_products = ProductModel.objects.filter(p_category = cat_id)
        # print(category_all_products)

        return render(request,'oneapp/category_display_products.html',{'data':category_all_products})

        # return render(request,'oneapp/category_display_products')
        
    def post(self,request):
        pass

class view_product(View):

    def get(self,request,pk):
        
        data = ProductModel.objects.get(id = pk)
        # print(data.p_brand)

        return render(request,'oneapp/view_product.html',{'data':data})

    def post(self,request):
        pass


class register(View):

    def get(self,request):

        form = RegisterForm()

        return render(request,'oneapp/register.html',{'form':form})
        
    def post(self,request):
        print('You are at post of request')
        form = RegisterForm(request.POST)
        if form.is_valid():
            print('form is valid')
            form.save()
            print('form saved')

            messages.success(request,'Registered Successfully !!! You Can Login Now')
            return redirect ('log_in')
        messages.warning(request,'Something Went Wrong !!!')
        return render(request,'oneapp/register.html',{'form':form})


class log_in(View):

    def get(self,request):
        
        form = LoginForm()

        return render(request,'oneapp/login.html',{'form':form})
        
    def post(self,request):
        print('you are in post of log in')
        form = LoginForm(request.POST,data=request.POST)
        if form.is_valid():
            print('your data is valid')
            u_name = form.cleaned_data['username']
            u_pass = form.cleaned_data['password']
            print(u_name)
            print(u_pass)
            user = authenticate(username=u_name,password = u_pass)
            if user is not None:
                login(request,user)
                messages.success(request,'Logged in successfully')
                return redirect('home')
        print('Your data is invalid')
        messages.warning(request,'Wrong Email Id Or Password !!!')
        return render(request,'oneapp/login.html',{'form':form})



class l_out(View):

    def get(self,request):
        logout(request)
        messages.success(request,'Logged out succesfully')
        return redirect('home')


