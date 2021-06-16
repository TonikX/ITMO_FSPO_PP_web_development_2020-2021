from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import create_view
from .models import *


router = DefaultRouter()
router.register('authors', create_view(Author, ['name']), 'author')
router.register('books', create_view(Book, ['name', 'discipline']), 'book')
router.register('book_copies', create_view(BookCopy), 'book_copy')
router.register('book_revs', create_view(BookRevision), 'book_rev')
router.register('borrows', create_view(Borrow), 'borrow')
router.register('borrowers', create_view(Borrower, ['firstname', 'lastname', 'patronymic', 'telnumber']), 'borrower')
router.register('compilers', create_view(Compiler), 'compiler')
router.register('publishers', create_view(Publisher), 'publisher')
router.register('translators', create_view(Translator), 'translator')

auth_urls = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
]

urlpatterns = auth_urls + router.urls
