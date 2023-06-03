from django.contrib import admin
from app.models import Translation


class TranslationAdmin(admin.ModelAdmin):
    list_display = ['source_text', 'source_lang', 'target_lang', 'translation', 'created_at']


admin.site.register(Translation, TranslationAdmin)