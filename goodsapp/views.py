from django.shortcuts import render
from django.views import View

from goodsapp.models import Category, Goods


# Create your views here.
class IndexView(View):
    def get(self, request,cid=2):
        cid = int(cid)
        # 查询所有类别信息
        categoryList = Category.objects.all()

        # 查询当前类别下的所有商品信息、
        goodsList=Goods.objects.filter(category_id=cid)


        return render(request, 'index.html', {'categoryList': categoryList,'cid':cid,'goodsList':goodsList})
