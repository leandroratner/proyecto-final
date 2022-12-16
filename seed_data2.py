from ejemplo.models import Vehiculo, Mascota, Vacaciones

Vehiculo(tipo="Auto", color="Rojo", año_modelo=2015).save()
Vehiculo(tipo="Moto", color="Blanca", año_modelo=2022).save()
Vehiculo(tipo="Camioneta", color="Negra", año_modelo=1999).save()

Mascota(tipo_animal="Perro", edad="7").save()
Mascota(tipo_animal="Gato", edad="10").save()
Mascota(tipo_animal="Loro", edad="2").save()

Vacaciones(destino= "Mar del Plata", dias_de_estadia = 15).save()
Vacaciones(destino= "Bariloche", dias_de_estadia = 30).save()
Vacaciones(destino= "Misiones", dias_de_estadia = 7).save()

print("Se cargaron con éxito los datos")
