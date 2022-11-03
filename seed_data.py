from ejemplo.models import Familiar
from ejemplo.models import Configuracion

#Familiar(nombre="Rosario", direccion="Rio Parana 745", numero_pasaporte=123123).save()
#Familiar(nombre="Alberto", direccion="Rio Parana 745", numero_pasaporte=890890).save()
#Familiar(nombre="Samuel", direccion="Rio Parana 745", numero_pasaporte=345345).save()
#Familiar(nombre="Florencia", direccion="Rio Parana 745", numero_pasaporte=567567).save()

#print("Se cargo con éxito los usuarios de pruebas")

#Configuracion(nombre_blog="Mi blog", construido_por="", titulo_principal="Familiares", subtitulo_principal="ABM en Django").save()

#Configuracion(nombre_blog="Mi blog de Familiares")

Conf = Configuracion.objects.get(nombre_blog="Mi blog")

print(f"{Conf.nombre_blog, Conf.titulo_principal}")

#configuracion = Configuracion.objects.first()
#print(f"{configuracion.id, configuracion.nombre_blog}") 