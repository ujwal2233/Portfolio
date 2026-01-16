from django.contrib import admin
from .models import Profile, Experience, Skill, Project, Certification, Education

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email')
    fields = ('name', 'title', 'bio', 'email', 'phone', 'location', 'profile_image_url', 'github_url', 'linkedin_url')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'is_current')
    list_filter = ('is_current', 'start_date')
    search_fields = ('title', 'company')
    fields = ('title', 'company', 'location', 'start_date', 'end_date', 'is_current', 'description')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency')
    list_filter = ('category', 'proficiency')
    search_fields = ('name',)
    fields = ('name', 'category', 'proficiency')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_completed')
    list_filter = ('date_completed',)
    search_fields = ('title', 'technologies')
    fields = ('title', 'short_description', 'description', 'technologies', 'date_completed', 'github_url', 'live_url', 'image_url')

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer', 'issue_date')
    list_filter = ('issue_date',)
    search_fields = ('title', 'issuer')
    fields = ('title', 'issuer', 'issue_date', 'expiry_date', 'credential_id', 'credential_url')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'end_date')
    list_filter = ('end_date',)
    search_fields = ('degree', 'institution')
    fields = ('degree', 'institution', 'field_of_study', 'start_date', 'end_date', 'gpa', 'description')
