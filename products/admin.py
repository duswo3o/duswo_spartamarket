from django.contrib import admin

from .models import Post

# Register your models here.
# admin.site.register(Post) # 관리자 페이지에 생성


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_time") # 관라자 페이지에서 제목과 작성시간을 보여줌
    search_fields = ("title", "content") # 검색을 할 때 제목 또는 내용에 걸리는 내용이 있으면 보여줌
    list_filter = ("created_time",)
    date_hierarchy = "created_time"
    ordering = ("-created_time",)
