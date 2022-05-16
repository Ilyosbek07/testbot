from django.contrib import admin
from .models import User, Tests, Subjects, Direction, DirectionSubjects, Language


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "name", "language", "is_active")
    list_filter = ("user_id", "id")
    list_editable = ("language", "is_active")
    list_display_links = ("id", "user_id")


@admin.register(Subjects)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("id", "subject_name")
    list_filter = ("subject_name",)


class DirectionInline(admin.TabularInline):
    model = DirectionSubjects
    extra = 5
    min_num = 5
    max_num = 5


@admin.register(Tests)
class TestAdmin(admin.ModelAdmin):
    inlines = [DirectionInline]
    list_display = ("id", "directions", "price")
    list_filter = ("id", "directions", "price")
    list_display_links = ("id", "directions")
    list_editable = ("price",)


@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ("id", "direction_name")


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("id", "language_name", "language_code")
    list_editable = ("language_name", "language_code")