from django.db import models

# Create your models here.
class User(models.Model):
    _id = models.AutoField(verbose_name='Айді користувача', primary_key=True, blank=False)
    username = models.TextField(verbose_name="Юзернем")
    password = models.TextField(verbose_name="Пapoль")
    payments_data = models.TextField(verbose_name="Kapтoчka")
    delivery_data = models.TextField()
    phone = models.TextField()
    email = models.EmailField()

    def __str__(self):
        print(f"{self._id} - {self.username}")
        return f"{self._id} - {self.username}"


class Category(models.Model):
    _id = models.AutoField(primary_key=True)
    category_name = models.TextField()

    def __repr__(self):
        print(f" {self.category_name}")
        return f"{self.category_name}"


class Product (models.Model):
    _id = models.AutoField(primary_key=True)
    name = models.TextField()
    price = models.FloatField()
    description = models.TextField()
    small_description = models.CharField(max_length=30)
    count = models.IntegerField()
    image = models.ImageField()

    def __repr__ (self):
        return f"{self.name}"

class Order (models.Model):
    _id = models.AutoField(primary_key = True)
    import datetime
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_info = models.TextField()
    date = models.DateTimeField(default=datetime.datetime.now)
    status = models.TextField()

    def __repr__(self):
        return f"{self._id}-{self.status}-{self.date}"

class Reviews (models.Model):
    from django.core.validators import MaxValueValidator, MinValueValidator
    _id = models.AutoField (primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    mark = models.PositiveIntegerField(default=0, validators=[MinValueValidator (1), MaxValueValidator (5)])
    mark_text = models.TextField()


def get_product_by_id(id):
    from django.shortcuts import get_object_or_404
    return get_object_or_404(Product, _id=id)


def get_review_for_item(id):
    return Reviews.object.all().filter(product=get_product_by_id(id))


def get_user_by_id():
    return get_object_or_404(User, _id=id)


def create_review(user, product, mark_desc, mark):
    review = Reviews()
    review.user = user,
    review.product = product
    review.mark = mark
    review.mark_text = mark_desc
    review.save()
    return None