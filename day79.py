class nilai:
  def __init__(self, angka):
    self.angka = angka

  def __add__(self, objek):
    return nilai(
      self.angka + objek.angka
    )

  def __sub__(self, objek):
    return nilai(
      self.angka - objek.angka
    )

  def __mul__(self, objek):
    return nilai(
      self.angka * objek.angka
    )

  def __truediv__(self, objek):
    return nilai(
      self.angka / objek.angka
    )

x1 = nilai(70)
x2 = nilai(45)
x3 = x1 + x2

print(x3.angka)
print((x1 - x2).angka)
print((x1 * x2).angka)
print((x1 / x2).angka)