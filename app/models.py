from django.db import models


class Translation(models.Model):
    source_text = models.TextField(null=False, blank=False, verbose_name="Source Text")
    source_lang = models.CharField(max_length=50, null=False, blank=False, verbose_name="Source Language")
    target_lang = models.CharField(max_length=50, null=False, blank=False, verbose_name="Target Language")
    translation = models.TextField(null=False, blank=False, verbose_name="Translated Text")
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.source_text

    class Meta:
        verbose_name = "Translation"
        verbose_name_plural = "Translations"
