from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import OrderForm, CreateUserForm, BookForm
from .filters import OrderFilter, BookFilter


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Был создан аккаунт для ' + user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Введены неверные даннные')

        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    paginator = Paginator(orders, 5)

    total_orders = orders.count()
    delivered = orders.filter(status='Выполнено').count()
    pending = orders.filter(status='В ожидании').count()

    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    context = {'orders': page_obj, 'customers': customers,
               'total_orders': total_orders, 'delivered': delivered,
               'pending': pending, 'prev': page_obj.number - 1,
               'next': (page_obj.number + 1 if page_obj.has_next() else 0)}

    return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='login')
def books(request):

    books = Book.objects.all()

    bookFilter = BookFilter(request.GET, queryset=books)
    books = bookFilter.qs

    return render(request, 'accounts/books.html', {'books': books, 'bookFilter': bookFilter})


@login_required(login_url='login')
def createBook(request):
    if not request.user.is_superuser:
        return redirect('books')
    else:
        form = BookForm()
        if request.method == 'POST':
            form = BookForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('books')

        context = {'form': form}
        return render(request, 'accounts/book_form.html', context)


@login_required(login_url='login')
def updateBook(request, pk):
    if not request.user.is_superuser:
        return redirect('books')
    else:
        book = Book.objects.get(id=pk)
        form = BookForm(instance=book)

        if request.method == 'POST':
            form = BookForm(request.POST, instance=book)
            if form.is_valid():
                form.save()
                return redirect('books')

        context = {'form': form}
        return render(request, 'accounts/book_form.html', context)


@login_required(login_url='login')
def deleteBook(request, pk):
    if not request.user.is_superuser:
        return redirect('books')
    else:
        book = Book.objects.get(id=pk)
        if request.method == "POST":
            book.delete()
            return redirect('books')

        context = {'item': book}
        return render(request, 'accounts/delete_book.html', context)


@login_required(login_url='login')
def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)

    orders = customer.order_set.all()
    order_count = orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {'customer': customer, 'orders': orders, 'order_count': order_count,
               'myFilter': myFilter}
    return render(request, 'accounts/customer.html', context)


@login_required(login_url='login')
def createOrder(request, pk):
    if not request.user.is_superuser:
        return redirect('/')
    else:
        OrderFormSet = inlineformset_factory(Customer, Order, fields=('book', 'status'), extra=10)
        customer = Customer.objects.get(id=pk)
        formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
        # form = OrderForm(initial={'customer':customer})
        if request.method == 'POST':
            # print('Printing POST:', request.POST)
            form = OrderForm(request.POST)
            formset = OrderFormSet(request.POST, instance=customer)
            if formset.is_valid():
                formset.save()
                return redirect('/')

        context = {'form': formset}
        return render(request, 'accounts/order_form.html', context)


@login_required(login_url='login')
def updateOrder(request, pk):
    if not request.user.is_superuser:
        return redirect('/')
    else:
        order = Order.objects.get(id=pk)
        form = OrderForm(instance=order)

        if request.method == 'POST':
            form = OrderForm(request.POST, instance=order)
            if form.is_valid():
                form.save()
                return redirect('/')

        context = {'form': form}
        return render(request, 'accounts/order_form.html', context)


@login_required(login_url='login')
def deleteOrder(request, pk):
    if not request.user.is_superuser:
        return redirect('/')
    else:
        order = Order.objects.get(id=pk)
        if request.method == "POST":
            order.delete()
            return redirect('/')

        context = {'item': order}
        return render(request, 'accounts/delete.html', context)
