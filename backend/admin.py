from django.contrib import admin

from backend.models import Company, Participants, Project, Skill, Student, User

# from backend.models import (User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'phone',)
    search_fields = ('username',)
    list_filter = ('username',)
    empty_value_display = '-пусто-'


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name',
                    'birth_date', 'email', 'phone',)
    search_fields = ('username',)
    list_filter = ('username',)
    empty_value_display = '-пусто-'


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'name',
                    'activities', 'email', 'phone',)
    search_fields = ('username', 'name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Skill._meta.get_fields()]
    search_fields = ('skill', 'student',)
    list_filter = ('skill',)
    empty_value_display = '-пусто-'


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'description', 'precondition',
        'result', 'criterias', 'host_company',
    )
    # list_display = [field.name for field in Project._meta.get_fields()]
    search_fields = ('title', 'host_company',)
    list_filter = ('title', 'host_company',)
    empty_value_display = '-пусто-'


@admin.register(Participants)
class ParticipantsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Participants._meta.get_fields()]
    search_fields = ('student', 'project',)
    list_filter = ('student', 'project',)
    empty_value_display = '-пусто-'
