from django.db import models
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.


Choice_Size = (
    ('SMALL', 'small'),
    ('LARG', 'larg'),
    ('MEDIUM', 'medium'),
    ('EXTRA LARG', 'extra larg'),
)


class products(models.Model):

    title           = models.CharField(max_length=50)
    description     = models.TextField(max_length=600)
    size            = models.CharField(max_length=10 , choices=Choice_Size, default='SMALL')
    price           = models.DecimalField(max_digits=6, decimal_places=2)
    sold            = models.IntegerField()
    category        = models.ForeignKey('category', on_delete=models.SET_NULL, null=True)
    pleceـavailable = models.IntegerField()
    image           = models.ImageField(upload_to='products/')
    pub_date        = models.DateTimeField(default=timezone.now)
    slug            = models.SlugField(blank=True, null=True)
    published       = models.BooleanField(default=True)


    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        super(products, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


class category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categorys'


    def __str__(self):
        return self.name
