from django.shortcuts import render
from django.http import HttpResponse
from CoderApp.models import mascotas
 
 
 
def mascotas(request):
  mascota1= mascotas(nombre="Chiquita", parentesco="Perrita de mi novio Rodri", edad="7 años", cumpleanios="20/03/2015")
  mascota1.save()
  mascota2= mascotas(nombre="Juana", parentesco="Mi hija", edad="4 años", cumpleanios="23/12/2018")
  mascota2.save()
  mascota3= mascotas(nombre="Cleto", parentesco="Sobrino", edad="10 años", cumpleanios="26/02/2012")
  mascota3.save()
  lista=[mascota1, mascota2, mascota3]
 
  return render(request, "CoderApp\mascotas.html", {"listita" : lista})

