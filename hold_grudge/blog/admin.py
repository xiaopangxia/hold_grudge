from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Post, Category, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'is_nav', 'creator', 'create_time')
    fields = ('name', 'status', 'is_nav')

    def post_count(self, obj):
        return obj.post_set.count()
    post_count.short_description = "帖子数量"

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        return super(CategoryAdmin, self).save_model(request, obj, form, change)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'creator', 'create_time')
    fields = ('name', 'status')

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        return super(TagAdmin, self).save_model(request, obj, form, change)


class CategoryOwnerFilter(admin.SimpleListFilter):
    title = "类别"
    parameter_name = "owner_category"

    def lookups(self, request, model_admin):
        return Category.objects.filter(creator=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=category_id)
        return queryset


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'creator', 'category', 'operator')
    list_display_links = []

    list_filter = [CategoryOwnerFilter]
    search_fields = ['title', 'category__name']

    actions_on_top = True
    actions_on_bottom = True

    fields = (
        ('title', 'category'),
        'desc',
        'status',
        'content',
        'tag',
    )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>', reverse('admin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(admin.ModelAdmin, self).get_queryset(request)
        return qs.filter(creator=request.user)



