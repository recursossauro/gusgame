from django.db import models
from gameplace.models import Master, Gamer
from django.conf import settings

from dropbox.exceptions import ApiError
import traceback


class Word(models.Model):

    gamer  = models.ForeignKey(Gamer, verbose_name='Gamer', on_delete=models.CASCADE, null=True, blank=True)
    word   = models.CharField('Word', max_length=200)
    image  = models.ImageField('Image', upload_to='images/', max_length=500, null=True, blank=True)

    # Fields to backup control
    created = models.DateTimeField('Created', auto_now_add=True)
    modified = models.DateTimeField('Modified', auto_now=True)

    class Meta:
        verbose_name        = 'Word'
        verbose_name_plural = 'Words'

    def get_image_url(self):
        try:
            return self.image.url
        except ApiError as e:
            traceback.print_exc()
            return None


    def __str__(self):
        return self.word

class Right(models.Model):
    user   = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='User', on_delete=models.CASCADE)
    gamer  = models.ForeignKey(Gamer, verbose_name='Gamer', on_delete=models.CASCADE)
    word   = models.ForeignKey(Word, verbose_name='Word', on_delete=models.CASCADE)
    number = models.IntegerField('Rights', default=0)

    # Fields to backup control
    created = models.DateTimeField('Created', auto_now_add=True)
    modified = models.DateTimeField('Modified', auto_now=True)

    class Meta:
        verbose_name        = 'Right'
        verbose_name_plural = 'Rights'
        unique_together = [['user', 'gamer', 'word']]

    def __str__(self):
        return self.word.word + " " + str(self.number)
