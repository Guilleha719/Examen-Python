def curvi(letra_mayuscula):
  letra_mayuscula = int(input("Introduce una letra"))
  curvas = ['B', 'C', 'D', 'G', 'J', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'U']
  if letra_mayuscula.islower():
      return 0
  elif letra_mayuscula in curvas:
      return 1
  else:
      return 0
