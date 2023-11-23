# from django.db import models


# class Product(models.Model):
#     title = models.CharField(
#         'Название товара',
#         max_length=200
#     )
#     description = models.TextField(
#         'Описание товара'
#     )
#     price = models.IntegerField(
#         'Цена товара'
#     )
#     image = models.ImageField(
#         'Картинка',
#         upload_to='product/',
#         blank=True
#     )

#     def __str__(self):
#         return self.title

#     def get_absolute_url(self):
#         # return reverse('project_detail', kwargs={'post_pk': self.pk})

#     class Meta:
#         verbose_name = 'Товар'
#         verbose_name_plural = 'Товары'
