from django.db import models


class Biblia(models.Model):
    livro = models.CharField(max_length=255)
    capitulo = models.IntegerField()
    versiculo = models.CharField(max_length=255)
    mensagem = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Biblia'
        unique_together = ['livro', 'capitulo', 'versiculo']
        ordering = ['-id']

    def __str__(self):
        return self.livro
