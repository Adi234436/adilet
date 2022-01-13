from django.db import models
from django.db.models import Choices



class CreatedAtModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        abstract = True

class Product(CreatedAtModel):
    # STATUS = Choices("Available", "Not exicted")
    title = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products', null=True, blank=True)
    # status = Statusfield()
    description = models.TextField()

    class Meta:
        ordering = ['title', 'price']

    def __str__(self):
        return self.title

class ProductReview(CreatedAtModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    reting = models.PositiveIntegerField(default=1)

    def __str__(self):
        return  self.reting