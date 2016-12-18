from django.db import models

# Create your models here.


class MyUser(models.Model):
    account = models.CharField(max_length=20)
    name = models.CharField(max_length=15)
    image = models.ImageField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Product(models.Model):
    # 类别
    kind = models.CharField(max_length=128)
    name = models.CharField(max_length=60)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='image')
    publisher = models.ForeignKey(MyUser)
    # True
    on_sale = models.BooleanField()
    publish_time = models.DateTimeField()
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(MyUser)
    product = models.ForeignKey(Product)
    content = models.TextField()

    def __str__(self):
        return self.content