from django.views import View
from .models import Goods
from django.forms.models import model_to_dict
import json
from django.core import serializers
from django.http import HttpResponse,JsonResponse
class GoodsListView(View):
    def get(self,request):
        '''
        通过django的view实现商品列表页
        :param request:
        :return:
        '''
        json_list = []
        goods = Goods.objects.all()[:10]

        for good in goods:
            json_dict = model_to_dict(good)
            json_list.append(json_dict)

        json_data = serializers.serialize('json',goods)
        json_data = json.loads(json_data)
        return JsonResponse(json_data,safe=False)