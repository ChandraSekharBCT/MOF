from django.shortcuts import render,redirect
from testapp.models import User,Normal_User,Whole_Seller,Products,Bank_Detail
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.models import auth
# Create your views here.
def home(request):
    try:
        role=request.user.role
        print("Role Of User",role)
        return render(request,"index.html",{'role':role})
    except:
        role="no"
        print("Role Of User",role)
        param={'role':role}
        return render(request,'index.html',param)
def about(request):
    try:
        role=request.user.role
        print("Role Of User",role)
        return render(request,"index.html",{'role':role})
    except:
        role="no"
        print("Role Of User",role)
        param={'role':role}
        return render(request,'about.html',param)
@csrf_exempt
def registerwithnormaluser(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        first_name=request.POST['f_name']
        last_name=request.POST['l_name']
        password=request.POST['pwd']
        cnf_password=request.POST['cnf_password']
        role="farmer"
        mobile=request.POST['mobile']
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username Taken')
            return redirect('/registerwithnormaluser')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email Id Taken') 
            return redirect('/registerwithnormaluser')
        elif password!=cnf_password:
        	messages.info(request,"Password not Match")
        	return redirect("/registerwithnormaluser")
        else:
            result=User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password,role=role)
            result.save() 
            user_id=result.id
            data=Normal_User(user_id=user_id,mobile=mobile)   
            data.save()
            return redirect("/login")
    else:
        return render(request,'user_registration.html')
@csrf_exempt
def login(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		user=auth.authenticate(username=username,password=password)
		if user:
			auth.login(request,user)
			if user.role=='farmer':
				return redirect('/product')
			elif user.role=='wholeseller':
				return redirect('/dashboard')
			else:
				return redirect("/login")
		else:
			messages.info(request,'Invalid credential')  
			return redirect('/login')  
	else:
		return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/login')
def register(request):
    try:
        role=request.user.role
        print("Role Of User",role)
        return render(request,"register.html",{'role':role})
    except:
        role="no"
        print("Role Of User",role)
        param={'role':role}
        return render(request,'register.html',param)
@csrf_exempt
def registerwithwholeseller(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        first_name=request.POST['f_name']
        last_name=request.POST['l_name']
        password=request.POST['pwd']
        cnf_password=request.POST['cnf_password']
        role="wholeseller"
        mobile=request.POST['mobile']
        gst_no=request.POST['gst']
        city=request.POST['city']
        zip_code=request.POST['zip_code']
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username Taken')
            return redirect('/registerwithwholeseller')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email Id Taken') 
            return redirect('/registerwithwholeseller')
        elif password!=cnf_password:
        	messages.info(request,"Password not Match")
        	return redirect("/registerwithwholeseller")
        elif gst_no==15:
        	messages.info(request,"GST Number Should Be 15 Digits")
        	return redirect("/registerwithwholeseller")
        elif mobile==10:
        	messages.info(request,"Mobile Number Should Be 10 Digits")
        	return redirect("/registerwithwholeseller")
        elif zip_code==6:
        	messages.info(request,"Zip Code Should Be 6 Digit")
        	return redirect("/registerwithwholeseller")
        else:
            result=User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password,role=role)
            result.save() 
            user_id=result.id
            data=Whole_Seller(user_id=user_id,city=city,mobile=mobile,zip_code=zip_code,gst_no=gst_no)   
            data.save()
            return redirect("/login")
    else:
        return render(request,'registerwithwholeseller.html')
def product(request):
    try:
        role=request.user.role
        print("Role Of User",role)
        all_data=Products.objects.all()
        param={'role':role,'all_data':all_data}
        return render(request,"product.html",param)
    except:
        role="no"
        print("Role Of User",role)
        all_data=Products.objects.all()
        param={'role':role,'all_data':all_data}
        return render(request,'product.html',param)
    # all_data=Products.objects.all()
    # param={'all_data':all_data}
    # return render(request,'product.html',param)
def search_product(request):
    try:
        role=request.user.role
        print("Role Of User",role)
        queryString=request.GET['q']
        all_data=Products.objects.filter(product_name__contains=queryString)
        param={'role':role,'all_data':all_data}
        return render(request,"product.html",param)
    except:
        role="no"
        print("Role Of User",role)
        queryString=request.GET['q']
        all_data=Products.objects.filter(product_name__contains=queryString)
        param={'role':role,'all_data':all_data}
        return render(request,'product.html',param)
    # queryString=request.GET['q']
    # all_data=Products.objects.filter(product_name__contains=queryString)
    # param={'all_data':all_data}
    # return render(request,'product.html',param)
def dashboard(request):
    return render(request,'dashboard.html')

def add_product(request):
    if request.method=='POST':
        product_name=request.POST['product_name']
        product_price=request.POST['product_price']
        product_quantity=request.POST['product_quantity']
        product_description=request.POST['product_description']
        product_image=request.FILES['product_image']
        product_image1=request.FILES['product_image1']
        product_image2=request.FILES['product_image2']
        user_id=request.user.id
        data=Products(user_id=user_id,product_name=product_name,product_price=product_price,product_quantity=product_quantity,product_description=product_description,product_image=product_image,product_image1=product_image1,product_image2=product_image2)
        data.save()
        return redirect('/add_product')
    else:
        return render(request,'product_add.html')
def show_all_product(request):
    user_data=request.user.id
    data=Products.objects.filter(user_id__in=[user_data])
    print("All Product Data",data)
    param={'data':data}
    return render(request,'show_all_product.html',param)
def delete_product(request,id):
    data=Products.objects.get(id=id)
    data.delete()
    return redirect('/show_all_product')

def add_bank_details(request):
    if request.method=="POST":
        name=request.POST['name']
        acc_no=request.POST['acc_no']
        ifcs_code=request.POST['ifcs_code']
        branch_name=request.POST['branch_name']
        bank_name=request.POST['bank_name']
        user_id=request.user.id
        data=Bank_Detail(user_id=user_id,name=name,acc_no=acc_no,ifcs_code=ifcs_code,branch_name=branch_name,bank_name=bank_name)
        data.save()
        messages.info(request,"Bank Details Save Successfully")
        return redirect('/add_bank_details')
    else:
        return render(request,"add_bank_detail.html")
