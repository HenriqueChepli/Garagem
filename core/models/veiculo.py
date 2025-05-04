from django.db import models

class Veiculo(models.Model):
    preco = models.DecimalField(max_digits=10, decimal_places=2, null= True, default=0)
    modelo = models.ForeignKey('Modelo', on_delete=models.CASCADE, related_name='veiculos')
    cor = models.ForeignKey('Cor', on_delete=models.CASCADE, related_name='veiculos')
    ano = models.IntegerField()
    acessorios = models.ManyToManyField('Acessorio', blank=True, related_name='veiculos')

    def __str__(self):
        return f'({self.id}) - {self.modelo.nome.upper()}, {self.cor.nome.upper()}, {self.ano}'