from .models import Container, Booking, UserDetails
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

# LoginPage function is to log in the user onn the website portal
def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('input-username')
        pass1 = request.POST.get('input-password')
        try:
            user = authenticate(request, username=username, password=pass1)

            if user is not None and user.is_staff:
                # Login Admin
                login(request, user)
                return redirect('/adminpanel')  # Redirect to admin dashboard
            elif user is not None:
                # Login User
                login(request, user)
                return redirect('home')  # Redirect to USER dashboard

            else:
                return render(request, 'UserLogin.html', {'error': 'UserName or Password Wrong Try Again!'})
        except:
            return render(request, 'UserLogin.html', {'error': 'UserName or Password Wrong Try Again!'})

    return render(request, 'UserLogin.html')


# The SignupPage function using to SignUp User
def SignupPage(request):
    if request.method == 'POST':
        username = request.POST.get('input-username')
        fullname = request.POST.get('input-firstname')
        phone = request.POST.get('input-phone')
        gender = request.POST.get('input-gender')
        address = request.POST.get('input-address')
        email = request.POST.get('input-email')
        pass1 = request.POST.get('input-password')
        check = request.POST.get('input-check') == 'on'

        # Check if the username already exists

        if User.objects.filter(username=username).exists():
            return render(request, 'UserRegistrations.html', {'error_message': 'Username already exists.'})
        if User.objects.filter(email=email).exists():
            return render(request, 'UserRegistrations.html', {'error_message': 'Email already exists.'})
        if User.objects.filter(email=email).exists():
            return render(request, 'UserRegistrations.html', {'error_message': 'Email already exists.'})
        if UserDetails.objects.filter(Phone=phone).exists():
            return render(request, 'UserRegistrations.html', {'error_message': 'Phone Number already exists'})
        # Store the user data inn User model
        my_user = User.objects.create_user(username=username, email=email, password=pass1)
        my_user.save()
        # get the user ID
        user_id = my_user.id  # Get the newly created user's ID

        # Retrieve the User instance using the user_id
        user_instance = User.objects.get(id=user_id)
        # Store the newly created user details to store UserDetails model
        details = UserDetails(user=user_instance, FullName=fullname, Phone=phone, Gender=gender, Address=address,
                              TermAndConditions=check)
        details.full_clean()  # Validate the model instance
        details.save()  # save data

        return redirect('login')

    return render(request, 'UserRegistrations.html')


# verify the user login or not
@login_required(login_url='login')
# Once login the user to open the home page to view all containers with available containers
def HomePage(request):
    details = Container.objects.all()
    containers = []
    for container in details:
        available_quantity = container.available_quantity()
        containers.append((container, available_quantity))
    return render(request, 'Home.html', {'products': details, 'containers': containers})


# verify the user login or not
@login_required(login_url='login')
# user booking containers to store the bookig details in Booking model
def book_container(request, container_id):
    if request.method == 'POST':
        user = request.user
        container = Container.objects.get(id=container_id)
        quantity = int(request.POST.get('quantity', 1))
        userdetail, _ = UserDetails.objects.get_or_create(user=user)
        booking = Booking(user=user, container=container, userdetail=userdetail, No_of=quantity)
        booking.save()
        return redirect('home')
    else:
        return redirect('login')


# verify the user login or not
@login_required(login_url='login')
# This is the user id based to filter all containers' data to return the user booking containers
def Booking_view(request):
    user_id = request.user.id
    container = Booking.objects.filter(user=user_id)
    return render(request, 'Booking.html', {'container': container})


# verify the user login or not
@login_required(login_url='login')
# The about page is to display what about company
def AboutPage(request):
    return render(request, 'About.html')


# Terms and conditions
def Conditions(request):
    return render(request, 'Conditions.html')


# User when they leave the website to click on the logout link to redirect the login page to remove the temporary site
# user data
def LogoutPage(request):
    logout(request)
    return redirect('login')


# To login admin only

def AdminLoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('input-username')
        password = request.POST.get('input-password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            # Login user
            login(request, user)
            return redirect('/adminpanel')  # Redirect to admin dashboard

        else:
            # Invalid credentials
            return render(request, 'Adminlogin.html', {"Error": "Invalid username or password"})

    return render(request, 'Adminlogin.html')


# When admin login using the login page to redirect to admin panel this is admin home page this panel to add containers
@login_required(login_url="adminlogin")
def AdminPanel(request):
    if request.method == 'POST':
        name = request.POST.get('input-name')
        price = request.POST.get('input-price')
        desc = request.POST.get('input-desc')
        image = request.FILES['input-image']

        ADD_PRODUCT = Container(Name=name, Price=price, Image=image, description=desc)
        ADD_PRODUCT.save()

    return render(request, 'Admin_Product.html')


# When admin delete the containers to called this function
@login_required(login_url="adminlogin")
def delete_product(request, id):
    product = Container.objects.get(id=id)
    product.delete()
    return redirect('/adminpanel/adminProduct')  # Redirect to the product list view


# When order delete the containers to call this function
@login_required(login_url="adminlogin")
def delete_order(request, id):
    product = Booking.onject.get(id=id)
    product.delete()
    return redirect('/adminorders')


# when click on the button show containers to display the all containers details and add containers
@login_required(login_url="adminlogin")
def Product_Data(request):
    if request.method == 'POST':
        name = request.POST.get('input-name')
        price = request.POST.get('input-price')
        desc = request.POST.get('input-desc')
        image = request.FILES['input-image']
        no_of = request.POST.get('input-no_of')

        ADD_PRODUCT = Container(Name=name, Price=price, Image=image, description=desc, No_of=no_of)
        ADD_PRODUCT.save()
        return redirect('adminProduct')

    details = Container.objects.all()
    return render(request, 'Admin_Product.html', {'product': details})


# show containers to display the all containers details
@login_required(login_url="adminlogin")
def Producr_Data_sep(request):
    details = Container.objects.all()
    return render(request, 'Admin_Product_sep.html', {'product': details})


# Display the all orders
@login_required(login_url="adminlogin")
def Admin_Orders(request):
    Orders = Booking.objects.all()
    return render(request, 'Admin_Orders.html', {'order': Orders})


# When Admin click on the approve button to call this function to approve the containers
@login_required(login_url="adminlogin")
def Approve_product(request, id):
    product = Booking.objects.get(id=id)
    product.confirm = True
    product.save()
    return redirect('adminOrders')  # Redirect to the product list view


# Once Admin Approve the container Decline back to Approval
def Decline_Approve_Product(request, id):
    product = Booking.objects.get(id=id)
    product.confirm = False
    product.save()
    return redirect('adminOrders')  # Redirect to the product list view


# All users data to Display the admin site
@login_required(login_url="adminlogin")
def Admin_Users(request):
    users = UserDetails.objects.all()
    return render(request, 'Admin_Users.html', {'users': users})


# the Admin is leave the website to call the logout button click to call the function
def AdminLogoutPage(request):
    logout(request)
    return redirect('adminlogin')
