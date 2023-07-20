from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Category, Rating, FavoriteBook           #, BookSearch
from .forms import CreateUserForm, RatingForm, BookForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
#from django.utils.text import slugify

# Create your views here.
def home(request):
    recommended_books = Book.objects.filter(recommended_books=True)
    ukrainian_books = Book.objects.filter(ukrainian_books=True)
    bestsellers_books = Book.objects.filter(bestsellers_books=True)
    return render(request, 'home.html', {'recommended_books': recommended_books,
                                         'ukrainian_books': ukrainian_books, 'bestsellers_books': bestsellers_books
                                         })
def all_books(request):
    books = Book.objects.all()
    return render(request, 'all_books.html', {'books': books})


def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    return render(request, 'genre_detail.html', {'category': category})


@login_required(login_url='login')
def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    favorite_book_exists = request.user.favoritebook_set.filter(book=book).exists()
    similar_books = Book.objects.filter(category__name__startswith=book.category.first())
    ratings = Rating.objects.filter(book=book)

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating_value = form.cleaned_data['rating']
            rating, created = Rating.objects.get_or_create(user=request.user, book=book)
            rating.rating = rating_value
            rating.save()
            book.update_average_rating()
    else:
        form = RatingForm()

    context = {
        'book': book,
        'similar_books': similar_books,
        'ratings': ratings,
        'form': form,
        'favorite_book_exists': favorite_book_exists
    }
    return render(request, 'book_detail.html', context)


def search_book(request):
    name_of_book = request.POST.get('name_of_book')
    print('Search term:', name_of_book)  # Add this print statement
    if name_of_book:
        searched_books = Book.objects.filter(title__icontains=name_of_book)
    else:
        searched_books = []
    return render(request, 'search_book.html', {'searched_books': searched_books})

def register_page(request):
    register_form = CreateUserForm()
    if request.method == 'POST':
        register_form = CreateUserForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.info(request, "Account Created Successfully!")
            return redirect('login')

    return render(request, 'register.html', {'register_form': register_form})


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Invalid Credentials")

    return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    return redirect('home')

def rate_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    rating = Rating.objects.filter(user=request.user, book=book).first()

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating_value = form.cleaned_data['rating']
            if rating:
                rating.rating = rating_value
                rating.save()
            else:
                Rating.objects.create(user=request.user, book=book, rating=rating_value)
            book.update_average_rating()
            return redirect('book_detail', slug=book.slug)
    else:
        form = RatingForm()

    context = {
        'book': book,
        'rating': rating,
        'form': form
    }
    return render(request, 'book_detail.html', context)


@login_required(login_url='login')
def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            #book.slug = slugify(book.title)
            book.save()
            form.save_m2m()

            print("Uploaded book data:")
            print("Title:", book.title)
            print("Cover Image:", book.cover_image)
            print("Author:", book.author)

            return redirect(reverse('book_detail', kwargs={'slug': book.slug}))
    else:
        form = BookForm()
    return render(request, 'upload_book.html', {'form': form})

@login_required(login_url='login')
def add_to_favorite(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    favorite, created = FavoriteBook.objects.get_or_create(user=request.user, book=book)
    if created:
        messages.success(request, 'Book added to favorites successfully.')
    else:
        messages.info(request, 'Book is already in favorites.')
    return redirect('book_detail', slug=book.slug)

@login_required(login_url='login')
def remove_from_favorite(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    favorite = FavoriteBook.objects.filter(user=request.user, book=book)
    favorite.delete()
    messages.success(request, 'Book removed from favorites successfully.')
    return redirect('book_detail', slug=book.slug)

def my_favorite_books(request):
    favorite_books = FavoriteBook.objects.filter(user=request.user).select_related('book')

    context = {
        'favorite_books': favorite_books,
    }
    return render(request, 'mylist.html', context)