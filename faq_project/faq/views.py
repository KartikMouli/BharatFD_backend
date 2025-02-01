# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer
from django.core.cache import cache

class FAQListView(APIView):
    def get(self, request):
        lang = request.query_params.get("lang", "en")  # Default to English
        # Create a unique cache key based on the language
        cache_key = f"faq_list_{lang}"

        # Check if data is already cached
        cached_faqs = cache.get(cache_key)

        if cached_faqs:
            # If cached data is found, return it
            return Response(cached_faqs)
        faqs = FAQ.objects.all()

        # Serialize FAQ objects
        serializer = FAQSerializer(faqs, many=True)

        # Cache the serialized data for 15 minutes (or adjust the timeout as needed)
        cache.set(cache_key, serializer.data, timeout=60)

        # Return the serialized data
        return Response(serializer.data)
