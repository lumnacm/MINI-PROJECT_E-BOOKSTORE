import datetime

import razorpay
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.db.models import Count
from django.http import HttpResponse, JsonResponse
from myapp.models import *



def public(request):
    a=Category.objects.all()
    b=Book.objects.all()[:6]
    paginator = Paginator(b, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  # Get the posts for that page

    return render(request,'publicindex.html',{'data':a,'data1':b,'page_obj': page_obj})

def public1(request):
    a=Category.objects.all()
    b=Book.objects.all()
    return render(request,'publicindex.html',{'data':a,'data1':b})

def viewmorebook(request,id):
    a=Category.objects.get(id=id)
    b=Book.objects.get(id=id)

    ob=Review.objects.filter(BOOK__id=b.id)
    tr=0
    for j in ob:
        tr+=float(j.rating)
    if len(ob)>0:
        tr=round(tr/len(ob),2)
    b.tr=tr
    b.c=len(ob)
    obb = Feedback.objects.filter(BOOK__id=id)
    return render(request,'view more book.html',{'data':a,'i':b,"f":obb})






def login(request):
    if request.method == 'POST':  # Only process if form is submitted
        username = request.POST['username']
        password = request.POST['password']

        user = Login.objects.filter(username=username, password=password).first()

        if user:
            request.session['lid'] = user.id

            if user.type == 'admin':
                return HttpResponse('''<script>window.location='/adminhome'</script>''')
            elif user.type == 'user':
                return HttpResponse('''<script>window.location='/user_home'</script>''')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password.'})

    return render(request, 'login.html')




def admin_home(request):


    a=Book.objects.all()
    book=a.count()
    request.session['book'] = book

    u=User.objects.all()
    user=u.count()
    request.session['user']=user

    c=Category.objects.all()
    cat=c.count()
    request.session['cat']=cat



    com=Complaints.objects.filter(reply='pending')
    complaint=com.count()
    request.session['complaint']=complaint

    book_data = (
        Book.objects.values('adddate')
            .annotate(count=Count('id'))
            .order_by('adddate')
    )

    labels = [str(item['adddate']) for item in book_data]  # Convert to string
    data = [item['count'] for item in book_data]

    request.session['lab'] = labels
    request.session['data'] = data

    user_data = (
        User.objects.values('registerationdate')  # Assuming 'registration_date' is the field for user registration
            .annotate(count=Count('id'))
            .order_by('registerationdate')
    )
    user_labels = [str(item['registerationdate']) for item in user_data]  # Convert to string
    user_data_values = [item['count'] for item in user_data]
    request.session['user_lab'] = user_labels
    request.session['user_data'] = user_data_values

    return render(request,'admin/adminhome.html',{'data':a,'complaint':complaint,'book':book,'user':user,'cat':cat})




# def admin_add_category(request):
#     if 'submit' in request.POST:
#         category=request.POST['category']
#         var=Category()
#         var.category=category
#         var.save()
#         return HttpResponse('''<script>alert("Category Added Successfully");window.location='/admin_add_category';</script>''')
#     return render(request,'admin/add category.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Category  # Adjust this import based on your project structure

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Category  # Adjust this import based on your project structure


def admin_add_category(request):
    cat = Category.objects.all()
    if 'submit' in request.POST:
        category = request.POST['category']

        if Category.objects.filter(category=category).exists():
            messages.error(request, "Category already exists!")
            return redirect('/admin_add_category')

        var = Category()
        var.category = category
        var.save()
        messages.success(request, "Category Added Successfully!")
        return redirect('/admin_add_category')  # Redirect to the same page
    return render(request, 'admin/add category.html',{'cat':cat})


def admin_add_books(request):
    c=Category.objects.all()
    if request.method == 'POST':
        CATEGORY=request.POST['category']
        title=request.POST['title']
        price=request.POST['price']
        quantity=request.POST['quantity']
        isbn=request.POST['isbn']
        author=request.POST['author']
        publish_year=request.POST['publish_year']
        language=request.POST['language']
        publisher=request.POST['publisher']
        description=request.POST['description']
        image=request.FILES['image']

        fs = FileSystemStorage()
        date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.jpg'
        fs.save(date, image)
        path = fs.url(date)

        b=Book()
        b.CATEGORY=Category.objects.get(id=CATEGORY)
        b.image=path
        b.title=title
        b.isbn=isbn
        b.price=float(price)
        b.quantity=quantity
        b.adddate=datetime.now().date().today().year
        b.author=author
        b.publish_year=publish_year
        b.language=language
        b.publisher=publisher
        b.description=description


        b.save()
        return HttpResponse('''<script>alert("Book Added Successfully");window.location='/admin_add_books';</script>''')
    return render(request,'admin/add  books.html',{'data':c,"d":datetime.now().strftime("%Y-%m-%d")})



def admin_view_books(request):
    a=Book.objects.all().order_by('-id')
    return render(request,'admin/admin_view_books.html',{'data':a})

def admin_view_more_book(request,id):
    a = Book.objects.get(id=id)
    return render(request, 'admin/admin_view_more_book.html',{'i':a})


def admin_search_books(request):
    aa = request.POST.get('a')  # Get the search term from the form
    books = Book.objects.all()  # Get all books initially

    if aa:  # If there's a search term
        # Filter books based on the search term for title, author, publish year, or price
        books = books.filter(
            Q(title__icontains=aa) |  # Search by title
            Q(author__icontains=aa) |  # Search by author
            Q(publish_year__year__icontains=aa) |  # Search by publish year (we'll extract the year)
            Q(price__icontains=aa) |  # Search by price
            Q(CATEGORY__category__icontains=aa)  # Search by category (assuming Category model has 'category' field)
        )
    return render(request,'admin/admin_view_books.html',{'data':books})







def admin_view_user(request):
    a=User.objects.all().order_by('-id')
    return render(request,'admin/view_users.html',{'data':a})


def admin_view_complaints(request):
    a=Complaints.objects.all().order_by('-id')
    return render(request,'admin/View_complaint.html',{'data':a})


def send_complaint_reply(request,id):
    request.session['cid']=id
    complaint = Complaints.objects.get(id=id)
    return render(request, 'admin/send_reply.html',{'complaint':complaint})


def send_complaint_reply_post(request):
    reply=request.POST['reply-details']
    ob=Complaints.objects.get(id=request.session['cid'])
    ob.reply=reply
    ob.save()
    return HttpResponse('''<script>window.location='/admin_view_complaints'</script>''')

def admin_view_feedbacks(request):
    a=Feedback.objects.all()
    return render(request, 'admin/view_feedback.html', {'data': a})


def blockuser(request,id):
    ob=Login.objects.get(id=id)
    ob.type='block'
    ob.save()
    return redirect('/admin_view_user')


def unblockuser(request,id):
    ob = Login.objects.get(id=id)
    ob.type = 'user'
    ob.save()

    return redirect('/admin_view_user')


def admin_edit_books(request,id):
    a=Book.objects.get(id=id)
    a1=Category.objects.all()

    return render(request,'admin/edit  books.html',{'data':a,'data1':a1})

def admin_edit_books_post(request):
    CATEGORY = request.POST['category']
    title = request.POST['title']
    price = request.POST['price']
    quantity = request.POST['quantity']
    isbn = request.POST['isbn']
    author = request.POST['author']
    publish_year = request.POST['publish_year']
    language = request.POST['language']
    publisher = request.POST['publisher']
    description = request.POST['description']
    id = request.POST['id']

    b = Book.objects.get(id=id)

    if 'image' in request.FILES:
        image = request.FILES['image']
        fs = FileSystemStorage()
        date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.jpg'
        fs.save(date, image)
        path = fs.url(date)
        b.image = path
        b.save()

    b.CATEGORY = Category.objects.get(id=CATEGORY)
    b.title = title
    b.price = float(price)
    b.quantity = quantity
    b.isbn = isbn
    b.author = author
    b.publish_year = publish_year
    b.language = language
    b.publisher = publisher
    b.description = description

    b.save()
    return HttpResponse('''<script>window.location='/admin_view_books'</script>''')


def admin_delete_book(request,id):
    var=Book.objects.get(id=id)
    var.delete()

    return HttpResponse('''<script>window.location='/admin_view_books'</script>''')


def userreg(request):
    if 'submit' in request.POST:
        fname = request.POST['fname']
        gender = request.POST['gender']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        default_image_path = "user1.jpg"  # Default image path

        # Check if the email already exists
        uu = User.objects.filter(email=email)
        if uu.exists():
            return redirect('/userreg')

        a = Login.objects.filter(username=email)
        if a.exists():
            return redirect('/userreg')
        if password == confirmpassword:
            l = Login()
            l.username = email
            l.password = confirmpassword
            l.type = 'user'
            l.save()

            u = User()
            if 'image' in request.FILES and request.FILES['image']:
                image = request.FILES['image']
                fs = FileSystemStorage()
                date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.jpg'
                fs.save(date, image)
                path = fs.url(date)
                u.image = path
            else:
                u.image = '/media/user1.jpg'  # Use default image if none is uploaded

            u.LOGIN = l
            u.fname = fname
            u.lname = lastname
            u.gender = gender
            u.email = email
            u.phonenumber = phone
            u.registerationdate = datetime.now().date().today().year
            u.save()

            # Add a success message and redirect to the login page
            messages.success(request, 'You have successfully registered! Please log in.')
            return HttpResponse('''<script>window.location='/login'</script>''')
        else:
            return HttpResponse('''<script>alert("Passwords do not match");window.location='/userreg'</script>''')

    return render(request, 'registerindex.html')


def terms(request):
    return render(request, 'term.html')

def user_home(request):
    a=Book.objects.all()
    b=Category.objects.all()

    # c = Category.objects.all()
    # cat = c.count()
    # request.session['cat'] = cat


    c=Bill_details.objects.filter(ORDER__USER__LOGIN_id=request.session['lid'])
    cc=c.count()
    request.session['bid']=cc
    return render(request,'user/userindex.html',{'data':a,'data1':b,'data2':cc})


#
#





from django.db.models import Q

def search_books(request):
    # Get search inputs from the form
    cat = request.POST.get('cat', '')  # Search by category
    query_string = request.POST.get('a', '')  # Single search input field

    # Start with all books
    books = Book.objects.all()

    # If the query_string is provided, search across multiple fields
    if query_string:
        books = books.filter(
            Q(title__icontains=query_string) |            # Search by title
            Q(author__icontains=query_string) |           # Search by author
            Q(publish_year__year__icontains=query_string) |  # Search by published year
            Q(price__icontains=query_string)               # Search by price
        )

    # Apply the category filter if a category is selected
    if cat and cat != "----SEARCH----":
        books = books.filter(CATEGORY_id=cat)

    # Get all categories for the dropdown
    categories = Category.objects.all()

    # Get count of orders for the current user
    bill_details = Bill_details.objects.filter(ORDER__USER__LOGIN_id=request.session['lid'])
    bill_count = bill_details.count()

    # Store the count in the session
    request.session['bid'] = bill_count

    # Render the user index with filtered books and categories
    return render(request, 'user/userindex.html', {
        'data': books,      # Filtered books based on search criteria
        'data1': categories,  # All categories for the dropdown
        'data2': bill_count,  # Count of user orders
    })


def user_view_profile(request):
    a=User.objects.get(LOGIN_id=request.session['lid'])
    c = Bill_details.objects.filter(ORDER__USER__LOGIN_id=request.session['lid'], ORDER__status='cart')
    cc = c.count()
    request.session['cid'] = cc
    return render(request,'user/pro.html',{'i':a,'cid':cc})


def user_edit_profile(request):
    a=User.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'user/edit profile.html',{'i':a})

def user_edit_profile_post(request):
    try:
        fname = request.POST['textfield']
        gender = request.POST['gender']
        lastname = request.POST['lname']
        email = request.POST['textfield3']
        phone = request.POST['textfield2']
        image = request.FILES['file']

        fs = FileSystemStorage()
        date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.jpg'
        fs.save(date, image)
        path = fs.url(date)

        u=User.objects.get(LOGIN_id=request.session['lid'])
        u.image = path
        u.fname = fname
        u.lname = lastname
        u.gender = gender
        u.email = email
        u.phonenumber = phone
        u.save()
        # return redirect('/user_view_profile')

        return HttpResponse('''
                    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/sweetalert2@10">
                    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@10"></script>
                    <script>
                        document.addEventListener("DOMContentLoaded", function() {
                            Swal.fire({
                                icon: 'success',
                                title: 'Successfully Updated!',
                                confirmButtonText: 'OK',
                                reverseButtons: true
                            }).then((result) => {
                                if (result.isConfirmed) {
                                    window.location = '/user_view_profile';
                                }
                            });
                        });
                    </script>
                ''')
    except:
        fname = request.POST['textfield']
        gender = request.POST['gender']
        lastname = request.POST['lname']
        email = request.POST['textfield3']
        phone = request.POST['textfield2']

        u = User.objects.get(LOGIN_id=request.session['lid'])

        u.fname = fname
        u.lname = lastname
        u.gender = gender
        u.email = email
        u.phonenumber = phone
        u.save()
        return HttpResponse('''
                    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/sweetalert2@10">
                    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@10"></script>
                    <script>
                        document.addEventListener("DOMContentLoaded", function() {
                            Swal.fire({
                                icon: 'success',
                                title: 'Successfully Updated!',
                                confirmButtonText: 'OK',
                                reverseButtons: true
                            }).then((result) => {
                                if (result.isConfirmed) {
                                    window.location = '/user_view_profile';
                                }
                            });
                        });
                    </script>
                ''')
        # return redirect('/user_view_profile')

def user_view_books(request,id):
    request.session['bid']=id
    a=Book.objects.filter(id=id)
    for i in a:
        ob=Review.objects.filter(BOOK__id=i.id).order_by('-id')
        tr=0
        for j in ob:
            tr+=float(j.rating)
        if len(ob)>0:
            tr=round(tr/len(ob),2)
        i.tr=tr
        i.c=len(ob)

    c = Bill_details.objects.filter(ORDER__USER__LOGIN_id=request.session['lid'],ORDER__status='cart')
    cc = c.count()
    request.session['cid'] = cc

    obb=Feedback.objects.filter(BOOK__id=id).order_by('-id')
    return render(request,'user/user_view_books.html',{'data':a,'cid':cc,"f":obb})





def user_home2(request):
    c = Bill_details.objects.filter(ORDER__USER__LOGIN_id=request.session['lid'])
    cc = c.count()
    request.session['bid'] = cc
    return render(request,'user/userindex2.html',{'bid':cc})


def user_booking(request,id):

    request.session['bid']=id
    c = Bill_details.objects.filter(ORDER__USER__LOGIN_id=request.session['lid'],ORDER__status='cart')
    cc = c.count()
    request.session['cid'] = cc

    a=Book.objects.filter(id=id)
    return render(request,'user/booking1.html',{'data':a,'cid':cc})


def user_booking1(request):
    qty=request.POST['qty']
    request.session['qty']=qty
    id=request.session['bid']
    a=Book.objects.get(id=id)
    vv=a.price

    total=float(vv)*float(qty)
    request.session['amt']=str(total).split(".")[0]
    c = Bill_details.objects.filter(ORDER__USER__LOGIN_id=request.session['lid'], ORDER__status='cart')
    cc = c.count()
    request.session['cid'] = cc

    first_order = Order.objects.filter(USER__LOGIN=request.session["lid"]).order_by('-id').first()
    if first_order is not None:
        print(first_order.place)
        return render(request,'user/booking.html',{'data':a,'amt':total,'cid':cc,"orderad":first_order})
    else:
        first_order=""
        return render(request, 'user/booking.html', {'data': a, 'amt': total, 'cid': cc, "orderad": first_order})


def user_booking_post(request):
    id=request.POST['id']
    # title=request.POST['title']
    place=request.POST['place']
    landmark=request.POST['landmark']
    qty=float(request.session['qty'])
    pin=request.POST['pin']
    address=request.POST['address']

    cc=Book.objects.get(id=id)
    aa=float(cc.price)
    pp=float(qty*aa)

    a=Order()
    a.BOOK=cc
    a.USER=User.objects.get(LOGIN_id=request.session['lid'])

    a.price=pp
    a.place=place
    a.pin=pin
    a.qty=qty
    a.address=address
    a.landmark=landmark
    a.status='ordered'
    a.date=datetime.now().today().date()
    a.save()
    ob1=Bill_details()
    ob1.ORDER = a
    ob1.BOOK = cc
    ob1.quantity =qty
    ob1.save()
    return redirect('/user_home')

def user_booking_post1(request):
    id=request.POST['id']
    # title=request.POST['title']
    place=request.POST['place']
    landmark=request.POST['landmark']
    qty=int(request.session['qty'])
    pin=request.POST['pin']
    address=request.POST['address']

    cc=Book.objects.get(id=id)
    aa=int(cc.price)
    pp=int(qty)*int(aa)
    if cc.quantity >= int(qty):
        a=Order()

        a.USER=User.objects.get(LOGIN_id=request.session['lid'])

        a.price=pp
        a.place=place
        a.pin=pin

        a.address=address
        a.landmark=landmark
        a.status='ordered'
        a.date=datetime.now().today().date()
        a.save()
        ob1=Bill_details()
        ob1.ORDER = a
        ob1.BOOK = cc
        ob1.quantity =qty
        ob1.save()
        request.session['oid']=a.id

        return redirect('/user_pay_proceed/'+str(a.id)+"/"+str(pp))
    else:
        c = Bill_details.objects.filter(ORDER__USER__LOGIN_id=request.session['lid'], ORDER__status='cart')
        cc = c.count()
        request.session['cid'] = cc

        a = Book.objects.filter(id=id)

        return render(request, 'user/booking1.html', {'data': a, 'cid': cc,"s":True})

#cart booking


def user_booking_post2(request):
    id=request.POST['id']
    # title=request.POST['title']
    place=request.POST['place']
    landmark=request.POST['landmark']

    pin=request.POST['pin']
    address=request.POST['address']


    a=Order.objects.get(id=id)


    a.place=place
    a.pin=pin

    a.address=address
    a.landmark=landmark
    a.status='ordered'
    a.date=datetime.now().today().date()
    a.save()

    request.session['oid']=a.id

    return redirect('/user_pay_proceed/'+str(a.id)+"/"+str(a.price))

#cart booking






def admin_view_booking(request):
    # a=Bill_details.objects.all()

    a=Order.objects.filter(Q(status='ordered') | Q(status="paid")).order_by('-id')
    return render(request,'admin/view bookings.html',{'bookings':a})


def admin_view_booking1(request,id):
    request.session['oid']=id
    # a=Bill_details.objects.all()

    a=Bill_details.objects.filter(ORDER__id=id)
    return render(request,'admin/view bookings1.html',{'bookings':a})

#
# def purchase(request,id):
#     a=Order.objects.filter(status='cart',USER__LOGIN__id=request.session['lid'])
#     if len(a)==0:
#         a=Order()
#         a.USER = User.objects.get(LOGIN__id=request.session['lid'])
#         a.price = 0
#         a.qty = 0
#         a.date = datetime.today()
#         a.place = ''
#         a.pin = 0
#         a.landmark = ''
#         a.address = ''
#         a.status = 'cart'
#         a.save()
#     obb=Book.objects.get(id=id)
#     ob=Bill_details()
#     # ob.ORDER = Order.objects.get(id=a.id)
#     ob.ORDER = Order.objects.get(id=a.id)
#     ob.BOOK = obb
#     ob.quantity =1
#     ob.save()
#     a.price+=obb.price
#     a.save()
#
#
#     return redirect("/user_home")




def purchase(request, id):
    # Get the order for the current user where the status is 'cart'
    a = Order.objects.filter(status='cart', USER__LOGIN__id=request.session['lid']).first()

    # If no cart exists for the user, create a new one
    if not a:  # Check if 'a' is None
        a = Order()
        a.USER = User.objects.get(LOGIN__id=request.session['lid'])
        a.price = 0
        a.qty = 0
        a.date = datetime.today()
        a.place = ''
        a.pin = 0
        a.landmark = ''
        a.address = ''
        a.status = 'cart'
        a.save()

    # Fetch the book that the user wants to add to the cart
    obb = Book.objects.get(id=id)

    # Create a new Bill_details entry with the book and order details
    OB=Bill_details.objects.filter(ORDER = a,BOOK = obb)
    if len(OB)==0:
        ob = Bill_details()
        ob.ORDER = a  # Now 'a' is the correct Order object
        ob.BOOK = obb
        ob.quantity = 1
        ob.save()

        # Update the total price of the order by adding the book's price
        a.price += obb.price
        a.save()

    return redirect("/user_home")


def cart_booking(request):

    # qty=request.POST['qty']
    # request.session['qty']=qty
    # id=request.session['bid']
    # a=Book.objects.get(id=id)
    # vv=a.price
    #
    # total=float(vv)*float(qty)
    # request.session['amt']=total
    # c = Bill_details.objects.filter(ORDER__USER__LOGIN_id=request.session['lid'], ORDER__status='cart')
    # cc = c.count()
    # request.session['cid'] = cc
    # return render(request,'user/view cart.html',{'data':a,'amt':total,'cid':cc})

    return render(request,'user/cart_booking.html')



def view_cart(request):
    cart_items = Bill_details.objects.filter(ORDER__USER__LOGIN_id=request.session['lid'], ORDER__status='cart')
    id=0
    if len(cart_items)>0:
        id=cart_items[0].ORDER.id
    request.session['oid']=id
    cart_data = []
    total_cart_price = 0
    car = cart_items.count()
    print(car)

    for item in cart_items:
        item_total_price = item.quantity * item.BOOK.price  # Calculate item total price
        total_cart_price += item_total_price  # Add item total to the cart total

        # Append item data with total price to the list
        cart_data.append({
            'item': item,
            'item_total_price': item_total_price,
        })

    # Pass the cart data and total cart price to the template
    return render(request, 'user/view cart.html', {'cart_data': cart_data, 'total_cart_price': total_cart_price,'car':car})

def update_quantity(request):
    item_id = request.POST.get('item_id')
    action = request.POST.get('action')
    print(item_id,action)
    if item_id and action:
        cart_item = Bill_details.objects.get(id=item_id)
        obproduct=cart_item.BOOK

        if action == 'increase':
            if obproduct.quantity>0:
                cart_item.quantity += 1
                obproduct.quantity-=1
                obproduct.save()
        elif action == 'decrease' and cart_item.quantity > 1:
            cart_item.quantity -= 1
            obproduct.quantity += 1
            obproduct.save()
        else:
            return JsonResponse({'error': 'Invalid action or quantity too low.'}, status=400)

        cart_item.save()
        item_total_price = cart_item.quantity * cart_item.BOOK.price
        total_cart_price = sum(item.BOOK.price * item.quantity for item in Bill_details.objects.filter(ORDER=cart_item.ORDER))

        return JsonResponse({
            'success': True,
            'new_quantity': cart_item.quantity,
            'item_total_price': item_total_price,
            'total_cart_price': total_cart_price
        })

    return JsonResponse({'error': 'Missing item ID or action.'}, status=400)


def remove_cart(request, id):
    # Get the cart item to be removed
    item = Bill_details.objects.get(id=id)

    # Calculate the total price of the item being removed
    item_total_price = item.quantity * item.BOOK.price

    # Get the associated order to access its total price
    order = item.ORDER

    # Delete the item from the cart
    item.delete()

    # Update the order total price by subtracting the item's total price
    order.price -= item_total_price
    order.save()  # Save the updated order

    # Redirect back to the view cart page
    return redirect("/view_cart")


def user_pay_proceed(request,id,amt):
    request.session['rid'] = id
    request.session['pay_amount'] = str(amt).split(".")[0]
    client = razorpay.Client(auth=("rzp_test_edrzdb8Gbx5U5M", "XgwjnFvJQNG6cS7Q13aHKDJj"))
    print(client)
    payment = client.order.create({'amount': request.session['pay_amount']+"00", 'currency': "INR", 'payment_capture': '1'})
    res=User.objects.get(LOGIN__id=request.session['lid'])
    #
    # ob=Order.objects.get(id=request.session['rid'])
    # ob.status='paid'
    # ob.save()
    return render(request,'user/UserPayProceed.html',{'p':payment,'val':res,"lid":request.session['lid'],"id":request.session['rid']})


def on_payment_success(request):
    request.session['rid'] = request.GET['id']
    request.session['lid'] = request.GET['lid']

    event = str(request.body);
    if 'payment_failed' in event:
        ob = Order.objects.get(id=request.GET['id'])
        ob.status = 'payment failed'
        ob.save()

        ob1 = Payment()
        ob1.ORDER = ob
        ob1.date = datetime.today()
        ob1.status = 'payment failed'
        ob1.save()
    else:
        ob = Order.objects.get(id=request.GET['id'])
        ob.status = 'paid'
        ob.save()

        ob1 = Payment()
        ob1.ORDER = ob
        ob1.date = datetime.today()
        ob1.status = 'paid'
        ob1.save()
    return redirect('/user_home')

    # return HttpResponse('''
    #             <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/sweetalert2@10">
    #             <script src="https://cdn.jsdelivr.net/npm/sweetalert2@10"></script>
    #             <script>
    #                 document.addEventListener("DOMContentLoaded", function() {
    #                     Swal.fire({
    #                         icon: 'success',
    #                         title: 'Order placed successfully...!!!',
    #                         confirmButtonText: 'OK',
    #                         reverseButtons: true
    #                     }).then((result) => {
    #                         if (result.isConfirmed) {
    #                             window.location = '/user_home';
    #                         }
    #                     });
    #                 });
    #             </script>
    #         ''')




    # return HttpResponse('''<script>alert("Success! Thank you for your Contribution");window.location="/userhome"</script>''')


def user_view_orders(request):
    # a=Bill_details.objects.filter(ORDER__USER__LOGIN_id=request.session['lid'], ORDER__status='cart')
    # a=Bill_details.objects.filter(ORDER__USER__LOGIN_id=request.session['lid'], ORDER__status='paid')
    # cc = a.count()
    # request.session['cid'] = cc
    my_orders = Bill_details.objects.filter(ORDER__USER__LOGIN_id=request.session['lid'],ORDER__status='paid')
    return render(request,'user/view_oreders.html',{"bill":my_orders})

def user_return_product(request):
    detid=request.POST["book_id"]
    reson=request.POST["reason"]
    ob=Bill_details.objects.filter(id=detid).update(status="returned",reason=reson)
    return redirect('/user_view_orders')


def view_offline_purchases(request):
    offline = OfflinePurchaser.objects.all().order_by('-id')
    return render(request ,'admin/view_offline_buyers.html',{'ofline':offline})


from datetime import datetime
def add_offline_purchase(request):
    books = Book.objects.filter(quantity__gt=0)
    if request.method == 'POST':
        name = request.POST['name']
        number = request.POST['number']
        place = request.POST['place']
        book_id = request.POST['book_id']
        qty = int(request.POST['qty'])  # Convert to integer

        try:
            book = Book.objects.get(id=book_id)
            if book.quantity > 0:
                book.quantity -= qty
                book.save()
                OfflinePurchaser.objects.create(
                    BOOK=book,
                    name=name,
                    number=number,
                    qty=qty,
                    date=datetime.now(),
                    place=place
                )
                return redirect('/view_offline_purchases')
            else:
                return HttpResponse("<script>alert('Out of stock');window.location='/view_offline_purchases'</script>")
        except Book.DoesNotExist:
            return HttpResponse("<script>alert('Book not found');window.location='/view_offline_purchases'</script>")
    return render(request, 'admin/add_new_offline.html', {'books': books})





# def user_view_orders(request):
#     user = User.objects.get(LOGIN__id=request.session['lid'])
#     orders = Order.objects.filter(USER=user)
#     bill_details = Bill_details.objects.filter(ORDER__in=orders)
#
#     # Create a dictionary to store feedback and ratings for each book
#     feedback_dict = {}
#     rating_dict = {}
#
#     for bill in bill_details:
#         feedbacks = Feedback.objects.filter(USER=user, BOOK=bill.BOOK)
#         reviews = Review.objects.filter(USER=user, BOOK=bill.BOOK)
#
#         feedback_dict[bill.BOOK.id] = feedbacks.first().feedback if feedbacks.exists() else None
#         rating_dict[bill.BOOK.id] = reviews.first().rating if reviews.exists() else None
#     return render(request, 'user/view_oreders.html', {
#         'bill': bill_details,
#         'feedback_dict': feedback_dict,
#         'rating_dict': rating_dict
#     })


def add_feedback(request):
    if request.method == 'POST':
        # Get the user from session
        user = User.objects.get(LOGIN_id=request.session['lid'])
        book_id = request.POST['book_id']
        feedback_text = request.POST['feedback']

        # Retrieve the Bill_details related to the user and book
        bill_detail = Bill_details.objects.filter(BOOK__id=book_id, ORDER__USER=user).first()

        if bill_detail:
            # Create Feedback if the Bill_detail exists
            Feedback.objects.create(
                USER=user,
                BOOK=Book.objects.get(id=book_id),
                feedback=feedback_text,
                ORDER=bill_detail  # Associate with Bill_details
            )
        else:
            # Handle the case where the Bill_detail does not exist
            # You could return an error message or log this
            print("No Bill_detail found for this user and book.")

        return redirect('/user_view_orders')


def add_rating(request):
    if request.method == 'POST':
        user = User.objects.get(LOGIN_id=request.session['lid'])
        book_id = request.POST['book_id']
        rating = request.POST['rating']

        bill_detail = Bill_details.objects.filter(BOOK__id=book_id, ORDER__USER=user).first()

        if bill_detail:
            Review.objects.create(
                USER=user,
                BOOK=Book.objects.get(id=book_id),
                rating=rating,
                ORDER=bill_detail
            )
        else:
            print("No Bill_detail found for this user and book.")
        return redirect('/user_view_orders')

def view_complaints(request):
    com = Complaints.objects.filter(USER__LOGIN_id=request.session['lid'])
    print(com)
    return render(request, 'user/complaint.html',{'com':com})

def send_complaint(request):
    return render(request, 'user/complaint.html')

def send_complaint_post(request):
    complaint=request.POST['complaint_details']
    complaint_details=Complaints()
    complaint_details.complaints=complaint
    complaint_details.date=datetime.now()
    complaint_details.reply='pending'
    complaint_details.USER=User.objects.get(LOGIN__id=request.session['lid'])
    complaint_details.save()
    return redirect('/view_complaints')

def admin_view_payments(request):
    # a=Bill_details.objects.all()
    a=Payment.objects.all().order_by('-id')
    return render(request,'admin/view bookings payment.html',{'data':a})
def admin_view_payments_more(request,orderid):
    # a=Bill_details.objects.all()
    a=Bill_details.objects.filter(ORDER=orderid)
    return render(request,'admin/view bookings payment_more.html',{'data':a})

def view_saled_book(request):
    saled_book = Bill_details.objects.filter(ORDER__status='paid').order_by('-id')
    return render(request, 'admin/view_saled_book.html',{'saled_book':saled_book})

def  View_return_request(request):
    obj=Bill_details.objects.filter(status="returned")
    ls=[]
    for i in obj:
        pr=Book.objects.get(id=i.BOOK.id)
        am=int(pr.price)*int(i.quantity)
        x={"id":i.id,"name":i.ORDER.USER.fname+" "+i.ORDER.USER.lname,
           "orddate":i.ORDER.date,
           "bookimg":i.BOOK.image,"title": i.BOOK.title,"amount":am,"reason":i.reason,"qty":i.quantity
           }

        ls.append(x)
    return render(request, 'admin/View_return_request.html',{'data':ls})


def accept_return(request, bill_id):
    # Fetch the specific bill detail
    try:
        bill_detail = Bill_details.objects.get(id=bill_id)
        book = bill_detail.BOOK  # Get the related book

        # Increase the book's quantity
        book.quantity += bill_detail.quantity
        book.save()  # Save the updated quantity

        # Update the status of the bill detail
        bill_detail.status = "accepted"
        bill_detail.save()  # Save the updated status

        return redirect('/View_return_request')  # Redirect to the return requests page
    except Bill_details.DoesNotExist:
        return HttpResponse("Return request not found", status=404)


def reject_return(request, bill_id):
    # Fetch the specific bill detail
    try:
        bill_detail = Bill_details.objects.get(id=bill_id)

        # Update the status of the bill detail
        bill_detail.status = "rejected"
        bill_detail.save()  # Save the updated status

        return redirect('/View_return_request')  # Redirect to the return requests page
    except Bill_details.DoesNotExist:
        return HttpResponse("Return request not found", status=404)


def public_post(request):
    aa = request.POST.get('a')  # Get the search term from the form
    books = Book.objects.all()  # Get all books initially
    categories = Category.objects.all()  # Get all categories

    if aa:  # If there's a search term
        # Filter books based on the search term for title, author, publish year, or price
        books = books.filter(
            Q(title__icontains=aa) |  # Search by title
            Q(author__icontains=aa) |  # Search by author
            Q(publish_year__year__icontains=aa) |  # Search by publish year (we'll extract the year)
            Q(price__icontains=aa)|  # Search by price
            Q(CATEGORY__category__icontains=aa)  # Search by category (assuming Category model has 'category' field)

        )

    return render(request, 'publicindex.html', {'data': categories, 'data1': books})

