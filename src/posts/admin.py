from django.contrib import admin

from posts.models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ["title", "timestamp", "updated"]
	list_display_links = ["timestamp"]
	list_editable = ["title"]
	list_filter = ["timestamp", "updated"]
	search_fields = ["title", "content"]
	class Meta:
		model = Post

admin.site.register(Post, PostAdmin)