from django.db import models


class News(models.Model):
    title = models.TextField(verbose_name='Заголовок')
    text = models.TextField(verbose_name='Контент')
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        verbose_name='Добавить картинку',
        upload_to='news/',
        blank=True,
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.text[:15]