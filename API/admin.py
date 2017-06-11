# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.

from models import *

class User_infoAdmin(admin.ModelAdmin):
	list_display = ('user','name','userName','email','phone','profile_picture','last_connection','reputacion',)
	#list_filter = ('user','username')
	search_fields = ('userName',)


class Menu_Admin(admin.ModelAdmin):
	list_display = ('id_menu','id_sucursal','descripcion','tipo_comida','precio','photo_menu',)
	search_fields = ('precio',)


class Pedido_Admin(admin.ModelAdmin):
	list_display = ('id_pedido','id_userInfo','id_direccion','Precio_total','Date','hour','id_statusOrden',)
	search_fields = ('Precio_total',)


class Vendedor_Admin(admin.ModelAdmin):
	list_display = ('id_vendedor','id_user_info','status',)
	search_fields = ('status',)


class Direccion_Admin(admin.ModelAdmin):
	list_display = ('id_direccion','direccion',)
	search_fields = ('direccion',)


class Listapedido_Admin(admin.ModelAdmin):
	list_display = ('id_listapedido','id_menu','id_pedido','cantidad',)
	search_fields = ('cantidad',)



class Sucursal_Admin(admin.ModelAdmin):
	list_display = ('id_sucursal','name','phone','addres',)
	search_fields = ('name',)



class Status_orden_Admin(admin.ModelAdmin):
	list_display = ('id_statusOrden','descripcion',)
	search_fields = ('descripcion',)



class Lista_direcciones_ip_Admin(admin.ModelAdmin):
	list_display = ('id_lista_direcciones_ip','id_ip_records','direccion_ip','fecha_usro',)
	search_fields = ('fecha_usro',)


class Payment_user_info_Admin(admin.ModelAdmin):
	list_display = ('id_payment_user_info','id_user_info','current_payment','saldo',)
	search_fields = ('saldo',)



class Gustos_Admin(admin.ModelAdmin):
	list_display = ('id_gustos','descripcion','categoria',)
	search_fields = ('categoria',)


class Ip_records_Admin(admin.ModelAdmin):
	list_display = ('id_ip_records','id_user_info','ip_actual',)
	search_fields = ('ip_actual',)


class Lista_gustos_Admin(admin.ModelAdmin):
	list_display = ('id_lista_gustos','id_userInfo','id_gustos',)
	

class Payment_Available_Admin(admin.ModelAdmin):
	list_display = ('id_payment_Available','id_payment_userinfo','type',)
	search_fields = ('type',)



class Vendedor_favorito_Admin(admin.ModelAdmin):
	list_display = ('id_vendedor_favorito','id_user_info','fecha_agregado','id_vendedor','calificacion',)
	search_fields = ('calificacion',)








admin.site.register(User_info,User_infoAdmin)
admin.site.register(Menu,Menu_Admin)
admin.site.register(Pedido,Pedido_Admin)
admin.site.register(Vendedor,Vendedor_Admin)
admin.site.register(Direccion,Direccion_Admin)
admin.site.register(Listapedido,Listapedido_Admin)
admin.site.register(Sucursal,Sucursal_Admin)
admin.site.register(Status_orden,Status_orden_Admin)
admin.site.register(Lista_direcciones_ip,Lista_direcciones_ip_Admin)
admin.site.register(Payment_user_info,Payment_user_info_Admin)
admin.site.register(Gustos,Gustos_Admin)
admin.site.register(Ip_records,Ip_records_Admin)
admin.site.register(Lista_gustos,Lista_gustos_Admin)
admin.site.register(Payment_Available,Payment_Available_Admin)
admin.site.register(Vendedor_favorito,Vendedor_favorito_Admin)








