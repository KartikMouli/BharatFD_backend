# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator
from django.core.cache import cache


class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()

    question_hi = models.TextField(null=True, blank=True)
    answer_hi = RichTextField(null=True, blank=True)

    question_bn = models.TextField(null=True, blank=True)
    answer_bn = RichTextField(null=True, blank=True)

    def get_translated(self, language_code):
        cache_key = f"faq_{self.id}_{language_code}"
        cached_translation = cache.get(cache_key)

        if not cached_translation:
            question_field = f"question_{language_code}"
            answer_field = f"answer_{language_code}"
            question = getattr(self, question_field, self.question)
            answer = getattr(self, answer_field, self.answer)

            translated = {"question": question, "answer": answer}
            cache.set(cache_key, translated, timeout=3600)

        return cached_translation

    async def save(self, *args, **kwargs):
        translator = Translator()
        if not self.question_hi:
            self.question_hi = (
                await translator.translate(self.question, src="en", dest="hi")
            ).text
            self.answer_hi = (
                await translator.translate(self.answer, src="en", dest="hi")
            ).text
        if not self.question_bn:
            self.question_bn = (
                await translator.translate(self.question, src="en", dest="bn")
            ).text
            self.answer_bn = (
                await translator.translate(self.answer, src="en", dest="bn")
            ).text
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question
