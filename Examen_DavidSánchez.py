import random

class Usuario():
  def __init__(self, nombre = "Usuario"):
    self.cuenta = 50
    self.nombre = nombre
    self.historial = []
    self.tipo = "Normal"

  def recargar(self, dinero):
    self.cuenta += dinero
    print (f"Se han recargado ${dinero:.2f}")

  def viajar(self):
    distancia = random.randint(1, 1000)
    precio = distancia*0.5
    viajes = (distancia, precio)
    self.historial.append(viajes)
    print(f"Distancia: {distancia}\nValor a pagar: ${precio:.2f}")
    self.cuenta -= precio
    if self.cuenta >= 0:
      print("Pago realizado")
      pass
    else:
      print("Dinero insuficiente")
      self.historial.pop()
      self.cuenta += precio

  def revisar(self):
    k = 0
    if len(self.historial) == 0:
      print("No tiene viajes")
    else:
      for x, y in self.historial:
        k += 1
        print(f"{k}: {x}km")

  def perfil(self, detallado):
    if detallado:
      print(f"Nombre:{self.nombre}\nTipo:{self.tipo}\nSaldo:{self.cuenta:.2f}\nCantidad de Viajes: {len(self.historial)}")
    else:
      print(f"Nombre:{self.nombre}\nSaldo:{self.cuenta:.2f}")
  
  def sumatoria(self):
    suma = 0
    for x, y in self.historial:
      suma += y
    return suma
  
class Premium(Usuario):
  def __init__(self,nombre = "Usuario"):
    super().__init__(nombre)
    self.tipo = "Premium"

  def viajar(self):
    distancia = random.randint(1, 1000)
    precio = distancia*0.5*0.8
    viajes = (distancia, precio)
    self.historial.append(viajes)
    print(f"Distancia: {distancia}km\nValor a pagar: ${precio:.2f}")
    self.cuenta -= precio
    if self.cuenta >=0:
      print("Pago realizado")
      pass
    else:
      print("Dinero insuficiente")
      self.historial.pop()
      self.cuenta += precio

n = 0

ini = input("¿Desea iniciar secion? (si/no): ").lower()
if ini == "si":
  n = str(input("Digite su nombre: "))
  print(f"Bienvenido {n}")
elif ini == "no":
  pass
else:
  print("Valor no valido, no se ha iniciado sesion")
opc = [1,2]
if n != 0:
  while True:
    try:
      t = int(input("Digite su tipo [1 (Normal)/2(Premium)]: "))
    except:
      pass
    if t in opc:
      break
    else:
      pass
  else:
    t = 1
  if t == 1:
    usuario = Usuario(n)
  else:
    usuario = Premium(n)
if n == 0:
  usuario = Usuario()
print()

while True:
      ac = input(f"Viajar\nRecargar\nRevisar\nPerfil\nSumatoria\nSalir\nDigite su accion: ").lower()
      print()
      if ac == "recargar":
        while True:
          try:
            din = float(input("Cuanto desea recargar: "))
            if din > 0:
              break
            else:
              pass
          except:
            pass
        usuario.recargar(din)
        print()
      elif ac == "viajar":
        usuario.viajar()
        print()
      elif ac == "revisar":
        usuario.revisar()
        print()
      elif ac == "perfil":
        while True:
          d = input("Desea revisar el perfil detallado? (si/no): ").lower()
          if d == "si":
            m = True
            break
          elif d == "no":
            m = False
            break
          else:
            print("Opcion no valida")
        usuario.perfil(m)
        print()
      elif ac == "sumatoria":
        print(f"Gasto total: ${usuario.sumatoria():.2f}")
        print()
      elif ac == "salir":
        break
      else:
        print("Opcion no valida")
        print()
