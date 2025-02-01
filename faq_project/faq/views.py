# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FAQ


class FAQListView(APIView):
    def get(self, request):
        lang = request.query_params.get("lang", "en")  # Default to English
        faqs = FAQ.objects.all()
        translated_faqs = []

        for faq in faqs:
            translated_faqs.append(faq.get_translated(lang))

        return Response(translated_faqs)
