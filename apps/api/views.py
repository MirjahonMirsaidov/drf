from django.http import JsonResponse

from apps.product.models import Product


def api_home(request):
    data = Product.objects.all().order_by('?').first()
    return JsonResponse({'msg': data.title})
