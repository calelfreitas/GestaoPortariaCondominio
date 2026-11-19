from django.db import models

class Morador(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF")
    telefone = models.CharField(max_length=20)
    bloco = models.CharField(max_length=10)
    apartamento = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nome} - Bloco {self.bloco}, Ap {self.apartamento}"


class Funcionario(models.Model):
    TURNO_CHOICES = [
        ('Manhã', 'Manhã'),
        ('Tarde', 'Tarde'),
        ('Noite', 'Noite'),
    ]
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    turno = models.CharField(max_length=10, choices=TURNO_CHOICES)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nome} ({self.cargo})"


class Entrega(models.Model):
    morador = models.ForeignKey(Morador, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    data_recebimento = models.DateTimeField(auto_now_add=True)
    retirado = models.BooleanField(default=False)
    data_retirada = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.descricao} - {self.morador.nome}"


class Entrada(models.Model):
    nome_visitante = models.CharField(max_length=100)
    documento = models.CharField(max_length=20)
    morador_destino = models.ForeignKey(Morador, on_delete=models.CASCADE)
    data_hora_entrada = models.DateTimeField(auto_now_add=True)
    data_hora_saida = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome_visitante} -> {self.morador_destino}"


class Ocorrencia(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    data_registro = models.DateTimeField(auto_now_add=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo