from django.db import models

class Category(models.Model):
    cname = models.CharField(max_length=10)

    def __str__(self):
        return f'<Category {self.cname}>'

class Goods(models.Model):
    gname = models.CharField(max_length=100, unique=True)
    gdesc = models.CharField(max_length=100)
    oldprice = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'<Goods: {self.gname}>'

class GoodsDetailName(models.Model):
    gdname = models.CharField(max_length=30)

    def __str__(self):
        return self.gdname

class GoodsDetail(models.Model):
    gdurl = models.ImageField(upload_to='goods_details/')
    goodsdname = models.ForeignKey(GoodsDetailName, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)

class Size(models.Model):
    sname = models.CharField(max_length=10)

    def __str__(self):
        return self.sname

class Color(models.Model):
    colorname = models.CharField(max_length=10)
    colorurl = models.ImageField(upload_to='color/')

    def __str__(self):
        return self.colorname

class Inventory(models.Model):
    count = models.PositiveIntegerField(default=100)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)