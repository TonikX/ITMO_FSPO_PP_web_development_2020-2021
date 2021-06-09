from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from main.models import Profile, Articles, Writer, Books, Review, Message, Discussion, Likes, LikesReview
 
@admin.register(Profile)
class ProfileAdmin(GuardedModelAdmin):
    pass

@admin.register(Articles)
class ArticlesAdmin(GuardedModelAdmin):
    pass

@admin.register(Writer)
class WriterAdmin(GuardedModelAdmin):
    pass

@admin.register(Books)
class BooksAdmin(GuardedModelAdmin):
    pass

@admin.register(Review)
class ReviewAdmin(GuardedModelAdmin):
    pass

@admin.register(Message)
class MessageAdmin(GuardedModelAdmin):
    pass

@admin.register(Discussion)
class DiscussionAdmin(GuardedModelAdmin):
    pass

@admin.register(Likes)
class LikesAdmin(GuardedModelAdmin):
    pass

@admin.register(LikesReview)
class LikesReviewAdmin(GuardedModelAdmin):
    pass
