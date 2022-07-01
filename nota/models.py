from django.db import models

PAGAMENTO = [('dinheiro', 'Dinheiro'), ('cartao', 'Cartão'), ('pix', 'Pix')]


class Pai(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    pagamento = models.CharField(max_length=100, choices=PAGAMENTO)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome


class Filho(models.Model):
    pai = models.ForeignKey(Pai, related_name='pai', on_delete=models.CASCADE)
    produto = models.CharField(max_length=100)
    quantidade = models.PositiveBigIntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.produto


