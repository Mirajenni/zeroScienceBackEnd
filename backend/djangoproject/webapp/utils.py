from enum import IntEnum

class AvatarTypes(IntEnum):
  MENINA_NEGRA = 1
  MENINA_PARDA = 2
  MENINA_ASIATICA = 3
  MENINA_CADEIRANTE = 4
  MENINO_NEGRO = 5
  
  @classmethod
  def choices(cls):
    return [(key.value, key.name) for key in cls]