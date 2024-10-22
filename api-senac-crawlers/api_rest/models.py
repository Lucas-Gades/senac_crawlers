# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# This is an auto-generated Django model module.
from django.db import models
from django.core.validators import MinValueValidator, EmailValidator

date_dafault ="1900-01-01",

class Edital(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome_banca = models.CharField(max_length=100, blank=True, null=True)
    titulo = models.CharField(max_length=150, blank=True, null=True)
    valor = models.FloatField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(0),  # O valor não pode ser negativo
        ]
    )
    descricao = models.TextField(blank=True, null=True)
    link = models.URLField(max_length=255, blank=True, null=True)
    id_site = models.ForeignKey('Site', models.DO_NOTHING, db_column='id_site', blank=True, null=True)
    img_logo = models.CharField(max_length=255, blank=True, null=True)
    vencimento = models.DateField(blank=True, null=True)
    prazo_execucao = models.DateField(blank=True, null=True)
    valor_global = models.FloatField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(0),  # O valor não pode ser negativo
        ]
    )
    valor_estimado = models.FloatField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(0),  # O valor não pode ser negativo
        ]
    )
   
    valor_maximo = models.FloatField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(0),  # O valor não pode ser negativo
        ]
    )
    data_publicacao = models.DateField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Define valores padrão para campos em branco
        if self.valor is None:
            self.valor = 0.0
        if self.valor_global is None:
            self.valor_global = 0.0
        if self.valor_estimado is None:
            self.valor_estimado = 0.0
        if self.valor_maximo is None:
            self.valor_maximo = 0.0
        if not self.nome_banca:
            self.nome_banca = "Nome do campo vazio!"
        if not self.titulo:
            self.titulo = "Título do campo vazio!"
        if not self.descricao:
            self.descricao = "Descrição do campo vazio!"
        if not self.link:
            self.link = "Link do campo vazio!"
        if not self.img_logo:
            self.img_logo = "Logo do campo vazio!"
        super(Edital, self).save(*args, **kwargs)

    class Meta:
        managed = False
        db_table = 'edital'


class Site(models.Model):
    id = models.BigAutoField(primary_key=True)
    url = models.URLField(max_length=255, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.nome:
            self.nome = "Nome do campo vazio!"
        if not self.url:
            self.url = "URL do campo vazio!"
        super(Site, self).save(*args, **kwargs)

    class Meta:
        managed = False
        db_table = 'site'


class Usuario(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(
        max_length=150,
        blank=True,
        null=True,
        validators=[EmailValidator()]
    )

    def save(self, *args, **kwargs):
        if not self.nome:
            self.nome = "Nome do campo vazio!"
        if not self.email:
            self.email = "Email do campo vazio!"
        super(Usuario, self).save(*args, **kwargs)

    class Meta:
        managed = False
        db_table = 'usuario'
