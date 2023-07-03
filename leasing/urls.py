from django.urls import path
from .views import SignupPage, LoginPage, HomePage, LogoutPage, AdminLoginPage, AdminPanel, Product_Data, \
    delete_product, Producr_Data_sep, Admin_Orders, Approve_product, Decline_Approve_Product, Admin_Users, \
    book_container, Booking_view, AboutPage, Conditions

# URLs to redirect to the help of html pages

urlpatterns = [
    path('adminlogin', AdminLoginPage, name='adminlogin'),
    path('adminpanel', AdminPanel, name='adminpanel'),
    path('adminpanel/adminProduct/', Product_Data, name='adminProduct'),
    path('adminpanel/adminProduct/delete/<int:id>/', delete_product, name='delete_product'),
    path('adminproduct/', Producr_Data_sep, name='adminProductSep'),
    path('adminorders/', Admin_Orders, name='adminOrders'),
    path('adminorders/approve/<int:id>/', Approve_product, name='approve_product'),
    path('adminorders/declineapprove/<int:id>/', Decline_Approve_Product, name='decline_approve_product'),
    path('adminusers/', Admin_Users, name='adminusers'),

    path('Terms and Condition/',Conditions, name='TermsAndCondition'),

    path('', SignupPage, name='Signup'),
    path('login/', LoginPage, name='login'),
    path('home', HomePage, name='home'),
    path('book_container/<int:container_id>/', book_container, name='book_container'),
    path('Bookedcontainer', Booking_view, name='Bookedcontainer'),
    path('about/', AboutPage, name='about'),
    path('logout/', LogoutPage, name='logout'),
]
