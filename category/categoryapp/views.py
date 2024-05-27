from django.shortcuts import redirect, render
from .models import Customer,Product,Category
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test


# Create your views here.
def home (request):
    return render(request,'home.html')
def signup (request):
    if request.method=="POST":
        Username=request.POST.get('username')
        Password=request.POST.get('password')
        Confirmpassword=request.POST.get('confirmpassword')

        if Customer.objects.filter(username=Username).exists():
            message ="username existed"
            return render(request,'signup.html',{'message':message})
    
        
        if Password == Confirmpassword :
            user=Customer.objects.create_user(username=Username,password=Password )
            return redirect('signin')


    
    return render(request,'signup.html')
def signin (request):
    if request.method=="POST":
        Username = request.POST.get ('username')
        Password = request.POST.get ('password')

        user= authenticate(request,username=Username,password=Password)
        if user is not None:
            message="sucessfully logined"
            login(request,user)
            return render(request,'products.html',{'message':message})
        else:
            errormessage="username password missmathch or not registerd"
            return render(request,'signin.html',{'errormessage':errormessage})

    return render(request,'signin.html')
@login_required
def products (request):
    products=Product.objects.all()
    return render(request,'products.html',{'products':products})
@login_required
# @user_passes_test(check_admin,login_url='signin')
def addproducts (request):
    categories = Category.objects.all() 

    if request.method=="POST":
        Image=request.FILES.get ('image')
        Title= request.POST.get ('title')
        Description= request.POST.get ('description')
        Price= request.POST.get ('price')
        category_id= request.POST.get ('categories')

        Categories=Category.objects.get(id=category_id)
        product=Product(
             image=Image,
             title=Title,
             description=Description,
             price=Price,
             categories=Categories,
        )
        product.save()
        return redirect('products')
    
    return render(request,'addproducts.html',{'categories':categories})
@login_required
def viewproduct (request ,product_id):
    product=Product.objects.get(id=product_id)
    return render(request,'viewproduct.html',{'product':product})
def editproduct (request,product_id):
    categories = Category.objects.all() 
    product=Product.objects.get(id=product_id)
    if request.method=="POST":
         if 'image' in request.FILES:
            product.image=request.FILES['image']
         product.title = request.POST.get ('title')
         product.description = request.POST.get ('description')
         category_id=request.POST.get ('categories')
         categories=Category.objects.get(id=category_id)
         product.save()
         return redirect('products')
    return render(request,'editproduct.html',{'categories':categories,'product':product})
def deleteproduct(request ,product_id):
    product=Product.objects.get(id=product_id)
    if request.method=="POST":
        product.delete()
        
        return redirect('products')
    else:
        return render(request,'viewproduct.html',{'product':product})
def UserLogout(request):
    logout(request)
    return redirect('signin')