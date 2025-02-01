from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

import asyncio

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()

    question_hi = models.TextField(null=True, blank=True)
    answer_hi = RichTextField(null=True, blank=True)

    question_bn = models.TextField(null=True, blank=True)
    answer_bn = RichTextField(null=True, blank=True)


    async def translate_fields(self, *args, **kwargs):
        async with Translator() as translator:
            # Translate to Hindi
            if not self.question_hi:
                translated_question_hi = await translator.translate(
                    self.question, src="en", dest="hi"
                )
                self.question_hi = translated_question_hi.text
            if not self.answer_hi:
                translated_answer_hi = await translator.translate(
                    self.answer, src="en", dest="hi"
                )
                print("--------------------------")
                print(translated_answer_hi)
                self.answer_hi = translated_answer_hi.text

            # Translate to Bengali
            if not self.question_bn:
                translated_question_bn = await translator.translate(
                    self.question, src="en", dest="bn"
                )
                self.question_bn = translated_question_bn.text
            if not self.answer_bn:
                translated_answer_bn = await translator.translate(
                    self.answer, src="en", dest="bn"
                )
                self.answer_bn = translated_answer_bn.text

    
    def save(self, *args, **kwargs):
        asyncio.run(self.translate_fields())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question
