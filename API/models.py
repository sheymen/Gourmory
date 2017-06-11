# -*- coding: utf-8 -*-
from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class User_info(models.Model): 
    user = models.OneToOneField(User) 
    name = models.CharField(max_length=255)
    userName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='profile_User')
    last_connection = models.DateTimeField()
    reputacion = models.IntegerField()

    def __unicode__(self):
        return unicode(self.user)
 
class Menu(models.Model): 
    id_menu = models.AutoField(primary_key=True)
    id_sucursal = models.ForeignKey('Sucursal', related_name='sucursal_menu')
    descripcion = models.CharField(max_length=255)
    tipo_comida = models.CharField(max_length=255)
    precio = models.IntegerField()
    photo_menu = models.ImageField(upload_to='photo_menu')

    def __unicode__(self):
        return unicode(self.id_menu)

  
class Pedido(models.Model): 
    id_pedido = models.AutoField(primary_key=True)
    id_userInfo = models.ForeignKey('User_info', related_name='user_infoPedido')
    id_direccion = models.ForeignKey('Direccion', related_name='direccion_pedido')
    Precio_total = models.IntegerField()
    Date = models.DateTimeField()
    hour = models.DateTimeField()
    id_statusOrden = models.ForeignKey('Status_orden', related_name='status_ordenPedido')

    def __unicode__(self):
        return unicode(self.id_pedido)

  
class Vendedor(models.Model): 
    id_vendedor = models.AutoField(primary_key=True)
    id_user_info = models.ForeignKey('User_info', related_name='user_infoVendedor')
    status = models.IntegerField()

    def __unicode__(self):
        return unicode(self.id_vendedor)

  
class Direccion(models.Model): 
    id_direccion = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=255)

    def __unicode__(self):
        return unicode(self.id_direccion)

  
class Listapedido(models.Model): 
    id_listapedido = models.AutoField(primary_key=True)
    id_menu = models.ForeignKey('Menu', related_name='menuListaPedido')
    id_pedido = models.ForeignKey('Pedido', related_name='menuPedido')
    cantidad = models.IntegerField()

    def __unicode__(self):
        return unicode(self.id_listapedido)

  
class Sucursal(models.Model): 
    id_sucursal = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    addres = models.CharField(max_length=255)

    def __unicode__(self):
        return unicode(self.id_sucursal)

  
class Status_orden(models.Model): 
    id_statusOrden = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)

    def __unicode__(self):
        return unicode(self.id_statusOrden)

  
class Lista_direcciones_ip(models.Model): 
    id_lista_direcciones_ip = models.AutoField(primary_key=True)
    id_ip_records = models.ForeignKey('Ip_records', related_name='ip_recordsLista_direcciones_ip')
    direccion_ip = models.CharField(max_length=255)
    fecha_usro = models.DateTimeField()

    def __unicode__(self):
        return unicode(self.id_lista_direcciones_ip)

  
class Payment_user_info(models.Model): 
    id_payment_user_info = models.AutoField(primary_key=True)
    id_user_info = models.ForeignKey('User_info', related_name='user_infoPayment')
    current_payment = models.CharField(max_length=255)
    saldo = models.IntegerField()

    def __unicode__(self):
        return unicode(self.id_payment_user_info)

  
class Gustos(models.Model): 
    id_gustos = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)

    def __unicode__(self):
        return unicode(self.id_gustos)

  
class Ip_records(models.Model): 
    id_ip_records = models.AutoField(primary_key=True)
    id_user_info = models.ForeignKey('User_info', related_name='user_infoIp_records')
    ip_actual = models.CharField(max_length=255)

    def __unicode__(self):
        return unicode(self.id_ip_records)

  
class Lista_gustos(models.Model): 
    id_lista_gustos = models.AutoField(primary_key=True)
    id_userInfo = models.ForeignKey('User_info', related_name='user_infoLista_gustos')
    id_gustos = models.ForeignKey('Gustos', related_name='gustos_lista')

    def __unicode__(self):
        return unicode(self.id_lista_gustos)

  
class Payment_Available(models.Model): 
    id_payment_Available = models.AutoField(primary_key=True)
    id_payment_userinfo = models.ForeignKey('Payment_user_info', related_name='payment_user_info_available')
    type = models.CharField(max_length=255)

    def __unicode__(self):
        return unicode(self.id_payment_Available)

  
class Vendedor_favorito(models.Model): 
    id_vendedor_favorito = models.AutoField(primary_key=True)
    id_user_info = models.ForeignKey('User_info', related_name='user_infoVendedor_favorito')
    fecha_agregado = models.DateTimeField()
    id_vendedor = models.ForeignKey('Vendedor', related_name='vendedor_favorito')
    calificacion = models.IntegerField()

    def __unicode__(self):
        return unicode(self.id_vendedor_favorito)


# Senal es un elemento que se dispara en django cuando ocurre un cambio, el cual permite liberar el cache para reflejar los cambios

from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.sessions.models import Session

@receiver(post_save)
def clear_cache(sender, **kwargs):
    if sender != Session:
        cache.clear()

