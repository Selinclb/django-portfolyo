from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from .models import Project, Contact, About, Skill, Experience, Education, Certificate

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'url')
    search_fields = ('title', 'description')
    list_filter = ('title', 'description')
    ordering = ('title', 'description')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'message')
    search_fields = ('email', 'message')
    list_filter = ('email', 'message')
    ordering = ('email', 'message')
    readonly_fields = ('instagram', 'youtube', 'tiktok', 'pinterest', 'behance')


class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'message','avatar_url','has_resume')
    search_fields = ('name', 'message')
    list_filter = ('name', 'message')
    ordering = ('name', 'message')

    def has_resume(self, obj):
        return bool(obj.resume_pdf)
    has_resume.short_description = 'CV Yüklü'
    has_resume.boolean = True

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'level', 'years_of_experience')
    list_editable = ('level', 'years_of_experience')
    search_fields = ('name',)
    list_filter = ('level', 'parent')
    ordering = ('name',)

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'years_of_experience')
    search_fields = ('name', 'description', 'years_of_experience')
    list_filter = ('name', 'description', 'years_of_experience')
    ordering = ('name', 'description', 'years_of_experience')

class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'degree', 'field_of_study')
    search_fields = ('institution', 'degree', 'field_of_study')
    list_filter = ('institution', 'degree', 'field_of_study')
    ordering = ('institution', 'degree', 'field_of_study')

class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date', 'url')
    search_fields = ('name', 'description', 'date', 'url')
    list_filter = ('name', 'description', 'date', 'url')
    ordering = ('name', 'description', 'date', 'url')



admin.site.register(Project, ProjectAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Certificate, CertificateAdmin)

