#from ejemplo.models import Familiar
#Familiar(nombre="Rosario", direccion="Rio Parana 745", numero_pasaporte=123123).save()
#Familiar(nombre="Alberto", direccion="Rio Parana 745", numero_pasaporte=890890).save()
#Familiar(nombre="Samuel", direccion="Rio Parana 745", numero_pasaporte=345345).save()
#Familiar(nombre="Florencia", direccion="Rio Parana 745", numero_pasaporte=567567).save()
#print("Se cargo con éxito los usuarios de pruebas")

from ejemplo.models import MVPFamiliares
MVPFamiliares(nombre="Pedro", edad=25 , ultimo_trabajo="Mi último trabajo fue de comerciante" , fecha_de_nacimiento= "20/03/1997").save()
MVPFamiliares(nombre="Laura", edad=32 , ultimo_trabajo="Mi último trabajo fue de productora" , fecha_de_nacimiento= "30/01/1990").save()
MVPFamiliares(nombre="Leo", edad=20 , ultimo_trabajo="Mi último trabajo fue de cantante" , fecha_de_nacimiento= "10/05/2000").save()
print("Se cargo con éxito los usuarios de pruebas")