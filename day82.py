class Hewan:
  def __init__(self):
    self.__list_hewan = []

  def tambah_hewan(self, hewan):
    self.__list_hewan.append(hewan)

  def __len__(self):
    return len(self.__list_hewan)

grupA= Hewan()
grupA.tambah_hewan('harimau')

print(len(grupA))