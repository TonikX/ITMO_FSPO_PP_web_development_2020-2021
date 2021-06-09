from django.shortcuts import render
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.views import View
from django.shortcuts import get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import check_password
from django.contrib.postgres.lookups import Unaccent
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from main.models import Articles, Books, Review, Discussion, Writer, Message, Likes, LikesReview
from main.forms import ArticlesForm


User = get_user_model()

def index(request):
    article = Articles.objects.all()
    books = Books.objects.all()
    context = {'article':article, 'books':books}
    if request.method == 'POST':
        data = request.POST
        if data.get("register"):
            user = User.objects.create_user(data.get('login'), data.get('email'), data.get('password'))
            # user.profile.phone = data.get('phone')
            user.save()
        if data.get("enter"):
            print(data)
            user = authenticate(request, username=data.get('login'), password=data.get('password'))
            if user is not None:
                login(request, user)
            else:
                # context = {'error': "Неправильные параметры входа. Проверьте логин и пароль."}
                print("Неправильные параметры входа. Проверьте логин и пароль.")
                # return render(request, 'main/index.html', context)

        if data.get("search"):
            books = Books.objects.filter(title = data.get('search'))
            article = Articles.objects.filter(article_title = data.get('search'))
            context['books'] = books
            context['article'] = article
            print(data)

    return render(request, 'main/index.html', context)

def books(request):
    books = Books.objects.all()
    context = {'books':books}
    if request.method == 'POST':
        data = request.POST
        if data.get('rating'):
            books = Books.objects.order_by('-plus_rating')
            context['books'] = books
            print(data)
        if data.get('name'):
            books = Books.objects.order_by('title')
            context['books'] = books
            print(data)
        if data.get('search_book'):
            books = Books.objects.filter(title = data.get('search_book'))
            context['books'] = books
            print(data.get('search_book'))
    return render(request, 'main/books.html',  context)

def articles(request):
    article = Articles.objects.all()
    context = {'article':article}
    if request.method == 'POST':
        data = request.POST
        if data.get('name'):
            article = Articles.objects.order_by('article_title')
            context['article'] = article
            print(data)
        if data.get('search_article'):
            article = Articles.objects.filter(article_title = data.get('search_article'))
            context['article'] = article
            print(data.get('search_article'))
    return render(request, 'main/articles.html', context)


class writer(View):
    template_name = 'main/writer.html'

    def get(self, request, *args, **kwargs):
        writer = get_object_or_404(Writer, pk=kwargs['pk'])
        rewies = Review.objects.all()
        discussion = Discussion.objects.all()
        data = {'writer':writer}
        return render(request, self.template_name, context=data)

class read_book(View):
    template_name = 'main/read_book.html'

    def get(self, request, *args, **kwargs):
        books = get_object_or_404(Books, pk=kwargs['pk'])
        rewies = Review.objects.all()
        discussion = Discussion.objects.all()
        likes = Likes.objects.all()
        data = {'books':books, 'rewies':rewies, 'discussion': discussion, 'likes': likes}
        return render(request, self.template_name, context=data)
    def post(self, request, *args, **kwargs):
        books = get_object_or_404(Books, pk=kwargs['pk'])
        rewies = Review.objects.all()
        discussion = Discussion.objects.all()
        likes = Likes.objects.all()
        context = {'books':books, 'rewies':rewies, 'discussion': discussion, 'likes': likes}
        data = request.POST
        print(data)
        if request.POST.get('like'):
            like = Likes.objects.get(id=data.get('like'))
            like.type = 'LIK'
            like.save()
            book = Books.objects.get(id=data.get('like_input'))
            book.plus_rating += 1
            book.minus_rating -= 1
            book.save()
        if request.POST.get('like2'):
            like = Likes()
            like.type = 'LIK'
            like.user = User.objects.get(id=request.user.id)
            like.book = Books.objects.get(id=data.get('like2'))
            like.save()
            book = Books.objects.get(id=data.get('like2'))
            book.plus_rating += 1
            book.save()
        if request.POST.get('dislike'):
            like = Likes.objects.get(id=data.get('dislike'))
            like.type = 'DIS'
            like.save()
            book = Books.objects.get(id=data.get('dislike_input'))
            book.plus_rating -= 1
            book.minus_rating += 1
            book.save()
        if request.POST.get('dislike2'):
            like = Likes()
            like.type = 'DIS'
            like.user = User.objects.get(id=request.user.id)
            like.book = Books.objects.get(id=data.get('dislike2'))
            like.save()
            book = Books.objects.get(id=data.get('dislike2'))
            book.minus_rating += 1
            book.save()
        return render(request, self.template_name, context)

class discussion(View):
    template_name = 'main/discussion.html'

    def get(self, request, *args, **kwargs):
        discussion = get_object_or_404(Discussion, pk=kwargs['pk'])
        messages = Message.objects.all()
        paginator = Paginator(messages, 2)
        page = self.request.GET.get('page')
        try:
            messages = paginator.page(page)
        except PageNotAnInteger:
            # Если страница не является целым числом, поставим первую страницу  
            messages = paginator.page(1)
        except EmptyPage:
            # Если страница больше максимальной, доставить последнюю страницу результатов
            messages = paginator.page(paginator.num_pages)
        context = {'discussion': discussion, 'message':messages}
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        discussion = get_object_or_404(Discussion, pk=kwargs['pk'])
        messages = Message.objects.all()
        paginator = Paginator(messages, 2)
        page = self.request.GET.get('page')
        try:
            messages = paginator.page(page)
        except PageNotAnInteger:
            messages = paginator.page(1)
        except EmptyPage:
            messages = paginator.page(paginator.num_pages)
        data = request.POST
        print(data)
        message = Message()
        message.user = User.objects.get(id=request.user.id)
        message.discussion = discussion
        message.text = data.get('text')
        message.save()
        context = {'discussion': discussion, 'message':messages}
        return render(request, self.template_name, context)

class read_article(View):
    template_name = 'main/read_article.html'

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Articles, pk=kwargs['pk'])
        context = {'article': article}
        return render(request, self.template_name, context)

class read_one_book(View):
    template_name = 'main/read_one_book.html'

    def get(self, request, *args, **kwargs):
        books = get_object_or_404(Books, pk=kwargs['pk'])
        likes = Likes.objects.all()
        context = {'books': books, 'likes': likes}
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        books = get_object_or_404(Books, pk=kwargs['pk'])
        rewies = Review.objects.all()
        discussion = Discussion.objects.all()
        likes = Likes.objects.all()
        context = {'books':books, 'likes': likes}
        data = request.POST
        print(data)
        if request.POST.get('like'):
            like = Likes.objects.get(id=data.get('like'))
            like.type = 'LIK'
            like.save()
            book = Books.objects.get(id=data.get('like_input'))
            book.plus_rating += 1
            book.minus_rating -= 1
            book.save()
        if request.POST.get('like2'):
            like = Likes()
            like.type = 'LIK'
            like.user = User.objects.get(id=request.user.id)
            like.book = Books.objects.get(id=data.get('like2'))
            like.save()
            book = Books.objects.get(id=data.get('like2'))
            book.plus_rating += 1
            book.save()
        if request.POST.get('dislike'):
            like = Likes.objects.get(id=data.get('dislike'))
            like.type = 'DIS'
            like.save()
            book = Books.objects.get(id=data.get('dislike_input'))
            book.plus_rating -= 1
            book.minus_rating += 1
            book.save()
        if request.POST.get('dislike2'):
            like = Likes()
            like.type = 'DIS'
            like.user = User.objects.get(id=request.user.id)
            like.book = Books.objects.get(id=data.get('dislike2'))
            like.save()
            book = Books.objects.get(id=data.get('dislike2'))
            book.minus_rating += 1
            book.save()
        return render(request, self.template_name, context)

class read_one_review(View):
    template_name = 'main/read_one_review.html'

    def get(self, request, *args, **kwargs):
        review = get_object_or_404(Review, pk=kwargs['pk'])
        likes = LikesReview.objects.all()
        context = {'review': review, 'likes': likes}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        review = get_object_or_404(Review, pk=kwargs['pk'])
        likes = LikesReview.objects.all()
        context = {'review':review, 'likes': likes}
        data = request.POST
        print(data)
        if request.POST.get('like'):
            like = LikesReview.objects.get(id=data.get('like'))
            like.type = 'LIK'
            like.save()
            review = Review.objects.get(id=data.get('like_input'))
            review.plus_rating += 1
            review.minus_rating -= 1
            review.save()
        if request.POST.get('like2'):
            like = LikesReview()
            like.type = 'LIK'
            like.user = User.objects.get(id=request.user.id)
            like.review = Review.objects.get(id=data.get('like2'))
            like.save()
            review = Review.objects.get(id=data.get('like2'))
            review.plus_rating += 1
            review.save()
        if request.POST.get('dislike'):
            like = LikesReview.objects.get(id=data.get('dislike'))
            like.type = 'DIS'
            like.save()
            review = Review.objects.get(id=data.get('dislike_input'))
            review.plus_rating -= 1
            review.minus_rating += 1
            review.save()
        if request.POST.get('dislike2'):
            like = LikesReview()
            like.type = 'DIS'
            like.user = User.objects.get(id=request.user.id)
            like.review = Books.objects.get(id=data.get('dislike2'))
            like.save()
            review = Review.objects.get(id=data.get('dislike2'))
            review.minus_rating += 1
            review.save()
        return render(request, self.template_name, context)

def admin_dev(request):
    return render(request, 'main/admin_panel.html')

def password_recovery(request):
    return render(request, 'main/password_recovery.html')

def profile(request):
    books = Books.objects.all()
    article = Articles.objects.all()
    review = Review.objects.all()
    likes = Likes.objects.all()
    data = {'article':article, 'books':books, 'review':review, 'likes':likes}
    return render(request, 'main/personal_account.html',  context=data)

def profile_edit(request):

    if request.method == 'POST':
        data = request.POST
        print(data)
        user = User.objects.get(id=request.user.id)
        user.username = data.get('login')
        user.first_name = data.get('name')
        user.last_name = data.get('surname')
        user.email = data.get('email')
        user.profile.image = request.FILES.get('image')
        user.save()


        if data.get('old_pass') != "":
            old_password = request.POST.get("old_pass")
            new_pass = request.POST.get("new_pass")
            if check_password(old_password, user.password):
                user.set_password(new_pass)
                update_session_auth_hash(request, user)
                user.save()

    return render(request, 'main/profile.html')

def create_author(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        author = Writer.objects.create()
        author.name = data.get('name')
        author.date_life = data.get('date_life')
        author.biografi = data.get('biografi')
        author.bibliografi = data.get('bibliografi')
        author.about_life = data.get('about_life')
        author.image = request.FILES.get('image')
        author.save()
    return render(request, 'main/create_author.html')

def article_confirmation(request):
    articles = Articles.objects.all()
    if request.method == 'POST':
        if request.POST.get('disline'):
            article_id = request.POST.get('disline')
            article = Articles.objects.get(id=article_id)
            article.delete()
        if request.POST.get('accept'):
            article_id = request.POST.get('accept')
            article = Articles.objects.get(id=article_id)
            article.status = True
            article.save()
    data = {'articles':articles}
    return render(request, 'main/article_confirmation.html', context=data)

def admin_create_composition(request):
    writer = Writer.objects.all()
    if request.method == 'POST':
        data = request.POST
        print(data)
        author_id = request.POST.get('author_id')
        book = Books()
        book.type = "DEF"
        book.author = Writer.objects.get(id=author_id)
        book.title = data.get('name')
        book.date = data.get('date')
        book.discription = data.get('discription')
        book.anatation = data.get('anatation')
        book.plus_rating = 0
        book.minus_rating = 0
        book.status = True
        book.image = request.FILES.get('image')
        book.user = User.objects.get(id=request.user.id)
        book.save()
    return render(request, 'main/admin_create_composition.html', {'writer':writer})

def confirmation_works(request):
    books = Books.objects.all()
    if request.method == 'POST':
        if request.POST.get('disline'):
            book_id = request.POST.get('disline')
            book = Books.objects.get(id=book_id)
            book.delete()
        if request.POST.get('accept'):
            book_id = request.POST.get('accept')
            book = Books.objects.get(id=book_id)
            book.status = True
            book.save()
    data = {'books':books}
    return render(request, 'main/confirmation_works.html', context=data)

def creat_composition(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        book = Books()
        book.type = "PRS"
        book.author = Writer.objects.get(id=1)
        book.title = data.get('title')
        book.discription = data.get('discription')
        book.anatation = data.get('anatation')
        book.text = data.get('text')
        book.plus_rating = 0
        book.minus_rating = 0
        book.words = data.get('words')
        book.chapters = data.get('chapters')
        book.status = False
        book.image = request.FILES.get('image')
        book.user = User.objects.get(id=request.user.id)
        book.save()
    return render(request, 'main/creat_composition.html')

def create_article(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        article = Articles()
        article.article_title = data.get('title')
        article.discription = data.get('discription')
        article.content = data.get('content')
        article.status = False
        article.image = request.FILES.get('image')
        article.type = data.get('type')
        article.user = User.objects.get(id=request.user.id)
        article.save()
    return render(request, 'main/create_article.html')

def create_discussion(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        book_id = request.POST.get('book_id')
        discussion = Discussion()
        discussion.title = data.get('title')
        discussion.book = Books.objects.get(id=book_id)
        discussion.save()
        last_discussion = Discussion.objects.last()
        message = Message()
        message.user = User.objects.get(id=request.user.id)
        message.discussion = Discussion.objects.get(id=last_discussion.id)
        message.text = data.get('text')
        message.save()
    return render(request, 'main/create_discussion.html')

def create_rewies(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        book_id = request.POST.get('book_id')
        review = Review()
        review.user = User.objects.get(id=request.user.id)
        review.book = Books.objects.get(id=book_id)
        review.title = data.get('title')
        review.discription = data.get('text')
        review.minus_rating = 0
        review.plus_rating = 0
        review.save()
    return render(request, 'main/create_review.html')
