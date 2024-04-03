from django.shortcuts import redirect, render , HttpResponse
from .models import ShopIT
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail, EmailMessage

from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from . tokens import generate_token
from ShopIT import settings

from django.shortcuts import render ,get_object_or_404
from cart.cart import Cart
from  home.models import ShopIT
from django.http import JsonResponse

# Create your views here.
def index(request):
    shopIT = ShopIT.objects.all() 
   
    return render(request,"index.html",{'shopIT':shopIT})
    # return HttpResponse(" My self Piyush yadav")
def about(request):
    #return HttpResponse("zoro is lost again!!! ")
    return render ( request, 'about.html')

def add(request):
    return render ( request, 'add.html')

def contact(request):
    return render ( request, 'contact.html')
def base(request):
    return render ( request, 'base.html')
def cart(request):
    return render ( request, 'cart/cart_summary.html')
def product_page(request):
    return render ( request, 'product_page.html')

def products(request):
    cart =  Cart(request)
    if request.POST.get('action')=='post':
        ShopIT_id=str(request.POST.get('ShopIT_id'))

        shopIT = get_object_or_404(ShopIT, id=ShopIT_id)
        cart.add(ShopIT=shopIT)

        cart_quantity=cart.__len__()
        response =JsonResponse({'Product Name:': ShopIT.name })
        response =JsonResponse({'qty:': cart_quantity })
        return response()
    

def recently(request):
    shopIT = ShopIT.objects.all()  
    return render ( request, 'recently.html', {'shopIT':shopIT})

def footer(request):
    if request.method == "POST":
        yourname = request.POST['yourname']
        youremail = request.POST['youremail']
        yourmessage = request.POST['yourmessage']

    

        

        subject = "Mail Received From "+yourname+" !!!"
        message = "MESSAGE \n\n" +yourmessage+ "\n\n**END OF MESSAGE**\nReceived From: " + youremail
        from_email = settings.EMAIL_HOST_USER
        to_list =[settings.EMAIL_HOST_USER] 
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        messages.success(request, "Message sent succesfully.")

        subject = "Mail Received Successfully "+yourname+" !!!"
        message = "Your Problem/question will be answered by our team as soon as possible.\nThankyou For visiting our website."
        from_email = settings.EMAIL_HOST_USER
        to_list =[youremail] 
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        messages.success(request, "Message sent succesfully.")

        return redirect('home')

    return render ( request, 'footer.html')

def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        # email = request.POST['email']
        password = request.POST['password']
        # username = request.POST['username']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged In Sucessfully!")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials!")
            return redirect('signin')

    return render ( request, 'auth/signin.html')

def sign_up(request):

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        # username = request.POST['username']
        email = email.lower()


        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username")
            return redirect('sign_up')

        elif User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return redirect('sign_up')

        elif len(username)>20:
            messages.error(request, "Username must be under 20 characters") 
            return redirect('sign_up')  

        elif password != confirmPassword:
            messages.error(request, "Passwords didn't match!") 
            return redirect('sign_up')

        elif not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!")
            return redirect('sign_up')
        
        
        
        
        else:
            myuser = User.objects.create_user(username, email, password)
            # myuser.firstname=fname
            # myuser.lastname=lname
            myuser.is_active=False

            myuser.save()

            messages.success(request, "Your Account Has Been Created Successfully.")

            subject = "Welcome to STYLEIT "+myuser.username
            message = "Hello " + myuser.username + " !! \n" + "Welcome to STYLEIT!!\nThank you for visiting our website\nWe have sent u a confirmation email"
            from_email = settings.EMAIL_HOST_USER
            to_list =[myuser.email] 
            send_mail(subject, message, from_email, to_list, fail_silently=True)

            current_site = get_current_site(request)
            email_subject = "Confirm your email @ StyleIT login!!"
            message2 = render_to_string('auth/email_confirmation.html',{
                'name':myuser.username,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(myuser.pk)),
                'token': generate_token.make_token(myuser)
            })
            email = EmailMessage(
                email_subject,
                message2,   
                settings.EMAIL_HOST_USER,
                [myuser.email],
            )
            email.fail_silently = True
            email.send()

            return redirect('signin')


    return render( request, 'auth/sign_up.html')

def signout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully!")
    return redirect('home')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('signin')
    else:
        return render(request, 'auth/activation_failed.html')

def admin(request):
    return HttpResponse('admin/.urls')
