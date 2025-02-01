from django.test import TestCase
from unittest.mock import patch
from googletrans.models import Translated
from django.core.cache import cache
from models import FAQ  


class FAQModelTestCase(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a web framework.",
        )

    @patch("myapp.models.Translator.translate")
    def test_save_translations(self, mock_translate):
        """Test that translations are saved for the FAQ model."""
        # Mock translations
        mock_translate.side_effect = lambda text, src, dest: Translated(
            text=f"{text} in {dest}", src=src, dest=dest
        )

        # Save the model
        self.faq.save()

        # Assert translations are generated and saved
        self.assertEqual(self.faq.question_hi, "What is Django? in hi")
        self.assertEqual(self.faq.answer_hi, "Django is a web framework. in hi")
        self.assertEqual(self.faq.question_bn, "What is Django? in bn")
        self.assertEqual(self.faq.answer_bn, "Django is a web framework. in bn")

    def test_get_translated_with_cache(self):
        """Test get_translated returns cached translation if available."""
        # Add translation to the cache
        cache_key = f"faq_{self.faq.id}_hi"
        cached_data = {"question": "Cached question in hi", "answer": "Cached answer in hi"}
        cache.set(cache_key, cached_data, timeout=3600)

        # Call get_translated
        translated = self.faq.get_translated("hi")

        # Assert cached translation is returned
        self.assertEqual(translated, cached_data)

    @patch("myapp.models.Translator.translate")
    def test_get_translated_without_cache(self, mock_translate):
        """Test get_translated generates and caches translation if not cached."""
        # Mock translations
        mock_translate.side_effect = lambda text, src, dest: Translated(
            text=f"{text} in {dest}", src=src, dest=dest
        )

        # Ensure no cache exists initially
        cache_key = f"faq_{self.faq.id}_bn"
        cache.delete(cache_key)

        # Call get_translated
        translated = self.faq.get_translated("bn")

        # Assert the translation is correct and cached
        self.assertEqual(translated["question"], "What is Django? in bn")
        self.assertEqual(translated["answer"], "Django is a web framework. in bn")
        self.assertEqual(cache.get(cache_key), translated)

    def test_string_representation(self):
        """Test the string representation of the FAQ model."""
        self.assertEqual(str(self.faq), "What is Django?")
