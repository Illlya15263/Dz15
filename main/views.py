from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *


def index(request):
    return render(request, 'main/index.html')

def product(request, id):
    return render(request, 'main/product.html',
                  context={"product": get_product_dy_id(id), "review": get_review_for_item(id)})

from django.views.decorators.http import require_POST
from django.http import JsonResponse

@require_POST
def post_review(request):
    id_user = request.POST.get('id_user')
    id_product = request.POST.get('id_product')
    mark = request.POST.get('mark')
    mark_desc = request.POST.get('mark_desc')

    user = get_user_by_id(id_user)
    product = get_product_by_id(id_product)
    create_review(user, product, mark_desc, mark)
    create_review(user, product, mark, desc)
    return product(request, id_product)

def create_user(user, product, mark, desc):
    review = Reviews()
    review.user = user,
    review.product = product
    review.mark
    review.mark_text = mark_desc
    review.save()
    return None