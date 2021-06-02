from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Client(models.Model):
    email = models.EmailField(max_length=200, unique=True, blank=False, null=False)
    nome = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return "{} - {}".format(self.nome, self.email)

class Product(models.Model):
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.CharField(max_length=200, blank=False, null=False)
    brand = models.CharField(max_length=100, blank=False, null=False)
    title = models.CharField(max_length=100, blank=False, null=False)
    product_code = models.IntegerField(unique=True, blank=False, null=False)

    def __str__(self):
        return "{}".format(self.title)

    def avg_note(product):
        products = Product.objects.all()
        contador = 0
        total = 0
        for product in products:
            review_products = Review.objects.filter(client__id=product.id)
            for review_product in  review_products:
                total += review_product.note
                contador += 1

        return total / contador


class Review(models.Model):
    client = models.ForeignKey(Client, models.DO_NOTHING, blank=False, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=False)
    note = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)], blank=False, null=False)
    
    def __str__(self):
        return "{} - {}".format(self.client, self.product)

    class Meta:
        unique_together = [['client', 'product']]

class ListProduct(models.Model):
    client = models.OneToOneField(Client, models.DO_NOTHING, blank=False, null=False)
    product = models.ManyToManyField('store.Product')

    def __str__(self):
        return "{} - {}".format(self.id, self.client)

   
    