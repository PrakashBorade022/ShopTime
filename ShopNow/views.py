from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from . models import Product,MyCart,MyOrdersNew,Review,Rating

def search(request):
    myOrders = MyCart.objects.get(user=request.user)
    totalItemsInCart = myOrders.productName.count()
    allProducts = Product.objects.all()
    query = request.GET.get('search')
    if query:
        find_product = allProducts.filter(productName__icontains=query)
        return render(request,'searchResult.html',{'find_product':find_product,'totalItemsInCart':totalItemsInCart})
    return render(request,'searchResult.html')


def addRatingandReview(request,id):
    myOrders = MyCart.objects.get(user=request.user)
    totalItemsInCart = myOrders.productName.count()
    product = Product.objects.filter(id=id)
    if request.method=="POST":

        product1 = Product.objects.get(id=id)
        rating = request.POST.get('rating')
        review = request.POST.get('review')



        newRaview = Review.objects.create(
            product=product1,
            reviewBy= request.user,
            review= review
            )
        newRaview.save()

        newRating = Rating.objects.create(
            product=product1,
            rating=rating
        )
        newRating.save()
        return redirect('/')
    return render(request,'addRatingandReview.html',{'product':product,'totalItemsInCart':totalItemsInCart})

def myOrdersPage(request):
    myOrders = MyCart.objects.get(user=request.user)
    totalItemsInCart = myOrders.productName.count()
    currentUser = request.user
    myAllOrders  =MyOrdersNew.objects.filter(orderByUser=currentUser)
    
    return render(request,'myOrderPage.html',{'myAllOrders':myAllOrders,'totalItemsInCart':totalItemsInCart})


    
def productPage(request,id):
    myOrders = MyCart.objects.get(user=request.user)
    totalItemsInCart = myOrders.productName.count()

    product = Product.objects.filter(id=id)
    getProduct = None
    for i in product:
        getProduct = i.id
    
    reviewObj = User.objects.filter(id=id)
   
   
  
    return render(request,'productPage.html',{'product':product,'reviewObj':reviewObj,"totalItemsInCart":totalItemsInCart})


def addToMyOrder(request,id):
   
    id = request.POST.get('productId')
    cartItem = MyCart.objects.all()

    
    productId = Product.objects.get(id=id)
    currentUser = request.user
    # newOrder = MyOrdersNew.objects.get(orderByUser=currentUser)
       
    newOrder = MyOrdersNew.objects.create(orderByUser= currentUser,productOrder=productId)
    
   
    # itemIncart.remove()
    # print(itemIncart)
 
   
        


    return redirect('/')

def myCart(request):

    myOrders = MyCart.objects.get(user=request.user)
    totalItemsInCart = myOrders.productName.count()
    print(totalItemsInCart)
    
    currentUser = request.user
    # cartItem = MyCart.objects.filter(user=currentUser)
    cartItem = MyCart.objects.get(user=currentUser)
    ProductsInCart  =cartItem.productName.all()
    return render(request,'myCart.html',{'ProductsInCart':ProductsInCart,'totalItemsInCart':totalItemsInCart})


def addToCart(request,id):
    productId = Product.objects.get(id=id)
    currentUser = request.user
    try :
        newCartItem = MyCart.objects.get(user=currentUser)

        # here no post method is used but its working ?? kaise ???? kaise ???           
        newCartItem.productName.add(productId)
        newCartItem.save()
            
                
    except:
        newCartItem = MyCart.objects.create(user= currentUser)
        newCartItem.save()
        newCartItem.productName.add(productId)
    # if request.method=="POST":

    #     # newOrder = MyOrder.objects.create(user = currentUser)
    #     myOrders.productName.add(productId)
        
    #     myOrders.save()
        
    #     return redirect('/')
    

   
        
    # print('add this product tp my orders',productId)
    return redirect('/')
def removeFromCart(request,id):
    productId = Product.objects.get(id=id)
    currentUser = request.user
    itemtoRemove = MyCart.objects.get(user=currentUser)

        # here no post method is used but its working ?? kaise ???? kaise ???           
    itemtoRemove.productName.remove(productId)
    itemtoRemove.save()
    
        
            
                
            
    
    
    return redirect('/myCart')

def homePage(request):
    products = Product.objects.all()
    product = Product.objects.all()
    rating = Rating.objects.all()

    # calculate average rating logic starthere
    dict = {}
    for line in rating:
        if dict.get(line.product.productName):
            dict[line.product.productName] = (dict[line.product.productName] + line.rating)/2

        else:
            dict.update({line.product.productName:line.rating})


        
    averageRating = dict
   
    productNameList = []
    for i in product:
        
        productNameList.append(i.productName)
    for j in productNameList:
        # for k in dict
        k= Product.objects.get(productName=j)
        for key,val in dict.items():
            if key == k.productName:
                k.averageRating = val
                k.save()
               # print("name {} k.name {} ".format(key,k.name))
    # average rating logic ends here

    if request.user.is_authenticated:
        currentUser = request.user
        try:

            myOrders = MyCart.objects.get(user=currentUser)
            if myOrders:


                totalItemsInCart = myOrders.productName.count()
                return render(request,'homePage.html',{'products':products,'totalItemsInCart':totalItemsInCart})
            else:
                return render(request,'homePage.html',{'products':products})

        except:
            pass
    return render(request,'homePage.html',{'products':products})

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        createNewUser = User.objects.create_user(
        
            first_name = first_name, 
            last_name = last_name, 
            email = email, 
            username = username, 
            password = password 
            )
        createNewUser.save()
        return redirect('/')
    return render(request,'signup.html')


def signin(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        authUser = authenticate(
             
            username= username,
            password = password
            )
        if authUser is not None :
            login(request,authUser)
            return redirect('/')
        else :
            messages.error(request,'Invalid Credentials')

    return render(request,'signin.html')


def logoutView(request):
    logout(request)
    return redirect('/')