from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.name
    '''def __unicode__(self):  # Python 3: def __str__(self):
        return str(self.name)  3.5python 不適用
'''

class Food(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=3,decimal_places=0)
    comment = models.CharField(max_length=50, blank=True)
    is_spicy = models.BooleanField(default=False)
    restaurant = models.ForeignKey(Restaurant)
    def __str__(self):
        return self.name

class Meta:
    ordering = ['price']

class Comment(models.Model):
    content = models.CharField(max_length=255)
    visitor = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    date_time = models.DateTimeField()
    restaurant = models.ForeignKey(Restaurant)
    def __str__(self):
        return self.content
    class Meta:
        ordering = ['date_time']
        permissions = (
            ("can_comment", "Can_comment"),

        )
#from restaurants.models import Restaurant, Food
#創物件方法1
#r1 = Restaurant(name='雪碧餐廳', phone_number='02-6666666', address='天龍國天龍區天龍路100號')
#r1.save()
#創物件方法2
#r2 = Restaurant.objects.create(name='金魚餐廳', phone_number='02-6666666', address='天龍國天龍區天龍路100號')
#restaurants = Restaurant.objects.all()
#restaurants
#r2 = restaurants[1]
#r = Restaurant.objects.get(name='雪碧餐廳')
#f1 = Food(name='牛排', price=120, comment='本店招牌', is_spicy="False",restaurant = r)
#f2 = Food(name='炒馬鈴薯', price=60, comment='好吃小點', is_spicy="False",restaurant = r)
