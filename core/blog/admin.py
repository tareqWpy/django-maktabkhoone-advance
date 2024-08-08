from blog.models import Category, Post
from django.contrib import admin


class PostAdmin(admin.ModelAdmin):
    """
    This is a class for presented data in admin panel.
    """

    list_display = [
        "author",
        "title",
        "title",
        "status",
        "category",
        "createde_date",
        "published_date",
    ]


"""
Registeration for Admin panel to present data.
"""
admin.site.register(Post)
admin.site.register(Category)
