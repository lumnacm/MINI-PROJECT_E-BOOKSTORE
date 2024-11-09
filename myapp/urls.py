
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from bookstoremanagement import settings
from myapp import views

urlpatterns = [
    path('',views.public),
    path('public1',views.public1),
    path('public_post',views.public_post),
    path('login',views.login),
    path('userreg',views.userreg),
    path('adminhome',views.admin_home),
    path('blockuser/<id>',views.blockuser),
    path('unblockuser/<id>',views.unblockuser),
    path('admin_view_user',views.admin_view_user),
    path('admin_view_complaints',views.admin_view_complaints),
    path('send_complaint_reply/<id>',views.send_complaint_reply),
    path('send_complaint_reply_post',views.send_complaint_reply_post),
    path('admin_view_feedbacks',views.admin_view_feedbacks),
    path('admin_add_category',views.admin_add_category),
    path('admin_add_books',views.admin_add_books),
    path('admin_view_books',views.admin_view_books),
    path('admin_delete_book/<id>',views.admin_delete_book),
    path('admin_edit_books/<id>',views.admin_edit_books),
    path('admin_view_booking1/<id>',views.admin_view_booking1),
    path('admin_edit_books_post', views.admin_edit_books_post),
    path('admin_view_booking', views.admin_view_booking),
    path('admin_view_payments', views.admin_view_payments),
    path('admin_view_payments_more/<orderid>', views.admin_view_payments_more),
    path('viewmorebook/<int:id>', views.viewmorebook),
    path('view_offline_purchases',views.view_offline_purchases),
    path('add_offline_purchase',views.add_offline_purchase),
    path('view_complaints',views.view_complaints),
    path('admin_search_books',views.admin_search_books),
    path('admin_view_more_book/<id>',views.admin_view_more_book),


    path('user_home', views.user_home),
    path('search_books', views.search_books),
    path('terms', views.terms),
    path('user_view_profile', views.user_view_profile),
    path('user_edit_profile', views.user_edit_profile),
    path('user_edit_profile_post', views.user_edit_profile_post),
    path('user_view_books/<id>', views.user_view_books),
    path('user_home2', views.user_home2),
    path('user_booking_post', views.user_booking_post),
    path('view_cart', views.view_cart),
    path('user_booking1', views.user_booking1),
    path('user_booking/<id>', views.user_booking),
    path('purchase/<id>', views.purchase),
    path('remove_cart/<id>', views.remove_cart),
    path('on_payment_success', views.on_payment_success),
    path('user_view_orders', views.user_view_orders),
    path('send_complaint',views.send_complaint),
    path('send_complaint_post',views.send_complaint_post),
    path('user_pay_proceed/<id>/<amt>', views.user_pay_proceed),
    path('view_saled_book', views.view_saled_book),
    path('add_feedback/', views.add_feedback, name='add_feedback'),
    path('add_rating/', views.add_rating, name='add_rating'),
    path('cart_booking/', views.cart_booking, name='cart_booking'),
    path('user_booking_post1', views.user_booking_post1, name='user_booking_post1'),
    path('update_quantity', views.update_quantity, name='update_quantity'),
    path('user_booking_post2', views.user_booking_post2, name='user_booking_post2'),
    path('user_return_product', views.user_return_product, name='user_booking_post2'),
    path('View_return_request', views.View_return_request, name='View_return_request'),
    path('accept_return/<bill_id>', views.accept_return, name='accept_return'),
    path('reject_return/<bill_id>', views.reject_return, name='reject_return'),

]

