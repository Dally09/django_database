import uuid

from django.db import models

def gen_unique_path(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = f'{uuid.uuid4()}.{ext}' # universal unique id
    return f'products/{new_filename}'

from myapp import migrations

CATEGORIES = [
    ('Food', 'Food Category'),
    ('Drinks', 'Drinks Category'),
    ('Cleaning', 'Cleaning Category'),
    ('Hardware', 'Hardware Category'),
]

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50, unique=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField(default=0)
    for_sale = models.BooleanField(default=False)
    category = models.CharField(max_length=50, choices=CATEGORIES)
    pic = models.ImageField(upload_to=gen_unique_path) # removed , default='products/default.jpg'
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'products'

#Run migrations each time you edit models
#python manage.py makemigrations
#python manage.py migrate