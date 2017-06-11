#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import * 
from rest_framework import viewsets
from rest_framework import status 
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework.permissions import AllowAny

from rest_framework import generics, filters

from django.contrib.auth.models import User
from django.db.models import Q
from django.core import serializers
import json



# Create your views here.


@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})


@api_view()
def getUserInfo(request):
	print 'Profile user Api'

	id_user = (request.GET['id_user'])

	try:
		profile = User_info.objects.get(Q(id=id_user))
	except Exception, e:
		profile = ""

	if profile != "":

		try:
			data = []
			data.append({'user': str(profile.user),'email': profile.email,'username': profile.userName,'real_name': profile.name,'phone': profile.phone,'profile_picture': str(profile.profile_picture),'reputacion':str(profile.reputacion),'last_connection':str(profile.last_connection),})

		
		except Exception, e:
			print e


		print data
		try:
			return Response(json.dumps(data))
		except Exception, e:
			print e
		
	else:
		return Response({"message": "User no"})




@api_view()
def getUserPayment(request):

	try:
		id_user = (request.GET['id_user'])
	except Exception, e:
		print e
		return Response({"message": "id_user is required"})

	try:
		profile = User_info.objects.get(Q(id=id_user))
	except Exception, e:
		profile = ""

	if profile != "":

		try:
			payment_user_info = Payment_user_info.objects.get(Q(id_user_info = profile))
		except Exception, e:
			print e
			payment_user_info = ""
		
		if payment_user_info:
			print payment_user_info
			try:
				data = []
				data.append({'current_payment':str(payment_user_info.current_payment),'saldo':str(payment_user_info.saldo),})

			except Exception, e:
				raise e

			print data
			try:
				return Response(json.dumps(data))
			except Exception, e:
				print e
		else:
			return Response({"message": "no payment user"})

	else:
		return Response({"message": "User no"})



@api_view()
def getUserGustos(request):
	try:
		id_user = (request.GET['id_user'])
	except Exception, e:
		print e
		return Response({"message": "id_user is required"})

	try:
		profile = User_info.objects.get(Q(id=id_user))
	except Exception, e:
		profile = ""

	if profile != "":

		lista_gustos = Lista_gustos.objects.filter(Q(id_userInfo=profile))

		gustos=[]

		for gusto in lista_gustos:
			gustos.append({'categoria':str(gusto.id_gustos.categoria),'descripcion':str(gusto.id_gustos.descripcion),})

		print gustos
		try:
			return Response(json.dumps(gustos))
		except Exception, e:
			print e
	else:


		return Response({"message": "User no"})


@api_view()
def getUserCustomers(request):
	try:
		id_user = (request.GET['id_user'])
	except Exception, e:
		print e
		return Response({"message": "id_user is required"})

	try:
		profile = User_info.objects.get(Q(id=id_user))
	except Exception, e:
		profile = ""

	if profile != "":

		vendedor_favorito = Vendedor_favorito.objects.filter(Q(id_user_info=profile))

		vendedores=[]

		for vendedor in vendedor_favorito:
			vendedores.append({'calificacion':str(vendedor.calificacion),'fecha_agregado':str(vendedor.fecha_agregado),'id_vendedor':str(vendedor.id_vendedor),})

		print vendedores
		try:
			return Response(json.dumps(vendedores))
		except Exception, e:
			print e
	else:


		return Response({"message": "User no"})


@api_view()
def getUserCurrentOrder(request):
	try:
		id_user = (request.GET['id_user'])
	except Exception, e:
		print e
		return Response({"message": "id_user is required"})

	try:
		profile = User_info.objects.get(Q(id=id_user))
	except Exception, e:
		profile = ""

	if profile != "":

		pedido = Pedido.objects.get(Q(id_userInfo=id_user))
		lista = Listapedido.objects.filter(Q(id_pedido=pedido))
		lista_pedidos=[]

		if pedido:
			date = pedido.Date
			hour = pedido.hour
			precio_total = pedido.Precio_total
			status_orden = pedido.id_statusOrden.descripcion
			direccion_entrega = pedido.id_direccion.direccion
			direccion_entrega = direccion_entrega.encode('utf8')
			print direccion_entrega


			pedidos = []
			for pedido1 in lista:
				sucursal_id = pedido1.id_menu.id_sucursal
				pedidos.append({'cantidad':str(pedido1.cantidad),'descripcion':str(pedido1.id_menu.descripcion),'tipo_comida':str(pedido1.id_menu.tipo_comida),'photo_menu':str(pedido1.id_menu.photo_menu),})


			lista_pedidos.append({'date':str(date),'hour':str(hour),'precio_total':str(precio_total),'status_orden':str(status_orden),'pedidos':pedidos,'sucursal_id':str(sucursal_id),'direccion_entrega':str(direccion_entrega),})

			print lista_pedidos
			try:
				return Response(json.dumps(lista_pedidos))
			except Exception, e:
				print e
		else:
			print('no data in pedido')
			return Response({"message": "no data in pedido"})
	else:


		return Response({"message": "User no"})
		



@api_view()
def getUserOrders(request):
	try:
		id_user = (request.GET['id_user'])
	except Exception, e:
		print e
		return Response({"message": "id_user is required"})

	try:
		profile = User_info.objects.get(Q(id=id_user))
	except Exception, e:
		profile = ""

	if profile != "":

		pedido = Pedido.objects.get(Q(id_userInfo=id_user))
		lista = Listapedido.objects.filter(Q(id_pedido=pedido))
		lista_pedidos=[]

		if pedido:
			date = pedido.Date
			hour = pedido.hour
			precio_total = pedido.Precio_total
			status_orden = pedido.id_statusOrden.descripcion
			direccion_entrega = pedido.id_direccion.direccion
			direccion_entrega = direccion_entrega.encode('utf8')
			print direccion_entrega


			pedidos = []
			for pedido1 in lista:
				sucursal_id = pedido1.id_menu.id_sucursal
				pedidos.append({'cantidad':str(pedido1.cantidad),'descripcion':str(pedido1.id_menu.descripcion),'tipo_comida':str(pedido1.id_menu.tipo_comida),'photo_menu':str(pedido1.id_menu.photo_menu),})


			lista_pedidos.append({'date':str(date),'hour':str(hour),'precio_total':str(precio_total),'status_orden':str(status_orden),'pedidos':pedidos,'sucursal_id':str(sucursal_id),'direccion_entrega':str(direccion_entrega),})

			print lista_pedidos
			try:
				return Response(json.dumps(lista_pedidos))
			except Exception, e:
				print e
		else:
			print('no data in pedido')
			return Response({"message": "no data in pedido"})
	else:


		return Response({"message": "User no"})

@api_view()
def getUserRecommendations(request):
	return Response({"message": "User no"})


@api_view()
def getTopCustomer(request):
	return Response({"message": "User no"})


@api_view()
def getSucursales(request):

	sucursales = Sucursal.objects.filter(Q())

	if sucursales:

		lista_sucursales = []

		for sucursal in sucursales:
			lista_sucursales.append({'name':sucursal.name,'phone':sucursal.phone,'addres':sucursal.addres,})

		try:
			return Response(json.dumps(lista_sucursales))
		except Exception, e:
			print e

	else:


		return Response({"message": "sin sucursales"})




@api_view()
def getMenu(request):
	try:
		sucursal_id = (request.GET['id_sucursal'])
	except Exception, e:
		print e
		return Response({"message": "id_sucursal is required"})

	try:
		sucursal = Sucursal.objects.get(Q(id_sucursal=sucursal_id))
	except Exception, e:
		sucursal = ""

	if sucursal != "":

		menus = Menu.objects.filter(Q(id_sucursal=sucursal))

		if menu:

			lista_menu = []

			for menu in menus:
				lista_menu.append({'id_sucursal':menu.id_sucursal,'descripcion':menu.descripcion,'tipo_comida':menu.tipo_comida,'precio':menu.precio,'photo_menu':menu.photo_menu,})


			try:
				return Response(json.dumps(lista_menu))
			except Exception, e:
				print e
		else:
			print('sin menu')
			return Response({"message": "no data in Menu"})
	else:
		print('sin menu')
		return Response({"message": "sin sucursal"})





@api_view()
def getSucursalInfo(request):

	try:
		sucursal_id = (request.GET['id_sucursal'])
	except Exception, e:
		print e
		return Response({"message": "id_sucursal is required"})

	try:
		sucursal = Sucursal.objects.get(Q(id_sucursal=sucursal_id))
	except Exception, e:
		sucursal = ""

	if sucursal:

		lista_sucursal = []

		
		lista_sucursal.append({'name':str(sucursal.name),'phone':str(sucursal.phone),'addres':str(sucursal.addres),})

		try:
			return Response(json.dumps(lista_sucursal))
		except Exception, e:
			print e

	else:


		return Response({"message": "sin sucursal"})














