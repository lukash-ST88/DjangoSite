from django.db import models
from django.urls import reverse

# Create your models here.
class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Текст статьи')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_create = models.DateTimeField (auto_now_add=True, verbose_name="Время создания") # constant date
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения") # changing date
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.ForeignKey('Category',on_delete=models.PROTECT, verbose_name="Категория") #Null=True - necessary during the creation of new migration


    def __str__(self): # returns data of instances for users
        return self.title

    def get_absolute_url(self): # returns optimized subcataloge <int:post_id> according to tamplate 'post' in urls
        return reverse('post', kwargs = {'post_slug': self.slug}) # Here must be ecxactly this name (get_absolute_url)
                                                                # to work "СМОТРЕТЬ НА САЙТЕ" in admin panel correctly
    class Meta: # Assign data for class Women in Meta view of admin panel
        verbose_name = 'Известные женщины'
        verbose_name_plural = 'Известные женщины' # to set plural and get rid of "s"
        ordering = ['-time_create', 'title'] # reverse sorting "-"


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name = "Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    def __str__(self):
        return self.name

    def get_absolute_url(self): # returns optimized subcataloge <int:post_id> according to tamplate 'post' in urls
        return reverse('category', kwargs = {'cat_id': self.pk})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['id']
