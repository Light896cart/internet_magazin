from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField
from taggit.managers import TaggableManager



class Product(models.Model):
    title = models.CharField(max_length=50,verbose_name='Заголовок')
    slug = models.SlugField(max_length=255,unique=True,db_index=True,verbose_name='URL')
    content = models.TextField(blank=True,verbose_name='Общее описание')
    structure = models.TextField(blank=True,verbose_name='Состав')
    care = models.TextField(blank=True,verbose_name='Уход')
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/",blank=True,verbose_name='Фото')
    photo2 = models.ImageField(upload_to="photo/%Y/%m/%d/",blank=True, verbose_name='Фото2')
    photo3 = models.ImageField(upload_to="photo/%Y/%m/%d/",blank=True, verbose_name='Фото3')
    SIZE_CHOICES = (('XXS', 'XXS'),
                    ('XS', 'XS'),
                    ('S', 'S'),
                    ('M', 'M'),
                    ('XL', 'XL'),
                    ('XXL', 'XXL'))

    sizes = MultiSelectField(choices=SIZE_CHOICES,null=True,max_choices=6,max_length=17)
    tags = TaggableManager(blank=True,verbose_name='Тег')
    sale = models.IntegerField('Скидка в процентах', blank=True, default=0)
    time_create = models.DateTimeField(auto_now_add=True,verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True,verbose_name='Время изменения')
    price = models.IntegerField(verbose_name='Ценa')
    available = models.BooleanField(default=True,verbose_name='Наличие')
    is_published = models.BooleanField(default=True,verbose_name='Публикация')
    prod_sub_category = models.ForeignKey('Category', on_delete=models.DO_NOTHING,verbose_name='Выберите категорию')
    subproduct = models.ForeignKey('Subcategory', on_delete=models.DO_NOTHING,verbose_name='Выберите подкатегорю')
    collecproduct = models.ForeignKey('Collections',null=True,on_delete=models.DO_NOTHING,verbose_name='Выберите коллекцию')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post',kwargs={'post_slug':self.slug})

    @property
    def get_sale(self):
        '''Расчитать стоимость со скидкой'''
        price = int(self.price * (100 - self.sale) / 100)
        return price

    class Meta:#для вида в админки
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталог'
        ordering = ['-time_create','title']


class Category(models.Model):
    name = models.CharField(max_length=100 , db_index = True,verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs = {'cat_slug': self.slug})

    def get_sub_category(self):
        return Subcategory.objects.filter(parent_category=self)

    class Meta:
        verbose_name = 'Kатегоpии'
        verbose_name_plural = 'Kaтегоpии'
        ordering = ['id']

# class ProductSizes(models.Model):
#     name = models.CharField(max_length=50)
#     product = models.ForeignKey("Product",  on_delete=models.DO_NOTHING )
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Размер'
#         verbose_name_plural = 'Размер'

class Subcategory(models.Model):
    sub = models.CharField(max_length=100,db_index=True,verbose_name='Подкатегория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    parent_category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True,verbose_name = 'Выберите категорию')

    def __str__(self):
        return self.sub

    def get_absolute_url(self):
        return reverse('subcategory', kwargs = {'catsub_slug': self.slug})

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегория'

class Collections(models.Model):
    title = models.CharField(max_length=40,db_index=True,verbose_name='Название коллекции')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('collections', kwargs = {'collections_slug': self.slug})

    def get_sub_category(self):
        return Product.objects.filter(collecproduct=self)

    class Meta:
        verbose_name = 'Коллекции'
        verbose_name_plural = 'Коллекции'