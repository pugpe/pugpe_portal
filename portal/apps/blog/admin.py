from django.contrib import admin

from models import Post
from forms import PostAddForm

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug':['title'] }
    list_display = ['title', 'author', 'pub_date', 'tags']
    search_fields = ['title', 'author__username']

    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            kwargs['exclude'] = ['author']
        return super(PostAdmin, self).get_form(request, obj, **kwargs)

    def get_readonly_fields(self, request, obj=None):
        if obj is None:
            return []
        return ['author']

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()

admin.site.register(Post, PostAdmin)