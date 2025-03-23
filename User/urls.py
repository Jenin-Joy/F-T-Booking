from django.contrib import admin
from django.urls import path
from User import views
app_name='User'

urlpatterns = [
    path('Homepage/', views.Homepage,name='Homepage'),
    path('MyProfile/', views.MyProfile,name='MyProfile'),
    path('EditProfile/', views.EditProfile, name='EditProfile'),
    path('ChangePass/', views.ChangePass, name='ChangePass'),
    path('JobVacancy/',views.JobVacancy,name='JobVacancy'),
    path('JobList/<int:iid>',views.JobList,name='JobList'),
    path('Apply/<int:jid>',views.Apply,name='Apply'),
    path('Complaint/',views.Complaint,name='Complaint'),
    path('Menu/',views.Menu,name='Menu'),
    path('Feedback/',views.Feedback,name='Feedback'),
    path('deletefeed/<int:did>',views.deletefeed,name='deletefeed'),
    path('ViewTable/',views.ViewTable,name='ViewTable'),
    path('Reservation/<int:did>',views.Reservation,name='Reservation'),
    path('Addcart/<int:pid>',views.Addcart, name='Addcart'), 
    path('MyCart/',views.MyCart,name='MyCart'),
    path("CartQty/", views.CartQty,name="cartqty"), 
    path("DelCart/<int:did>", views.DelCart,name="delcart"),
    path("payment/<int:id>",views.payment,name="payment"),  
    path('loader/',views.loader, name='loader'),
    path('paymentsuc/',views.paymentsuc, name='paymentsuc'),
    path("productpayment/", views.productpayment,name="productpayment"),
    path("OrderAmount/",views.OrderAmount,name="OrderAmount"),
    path("MyOrders/<int:id>",views.MyOrders,name="MyOrders"),
    path("Rating/",views.Rating,name="Rating"),
    path("ajaxgettable/",views.ajaxgettable,name="ajaxgettable"),
    path("ajaxgettablecount/",views.ajaxgettablecount,name="ajaxgettablecount"),
    path("Head/",views.Head,name="Head"),
    path("Foot/",views.Foot,name="Foot"),
    path("Tablepayment/<int:id>",views.Tablepayment,name="Tablepayment"),
    path('bookchecking/',views.bookchecking,name="bookchecking"),
    path('viewtablebooking/',views.viewtablebooking,name="viewtablebooking"),
]