from django.db import models

# Create your models here.

class BlogPost(models.Model):
    """ Um assunto sobre o postagem """
    title = models.CharField(max_length=50)
    text = models.TextField()
    date_adedd = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'blogposts'

    def __str__(self):
        """ Retorna uma representação em string do modelo """
        # return self.text[:50] + '...'
        return self.title
