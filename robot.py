from enum import Enum

MASS_LIMIT_KG = 20
DIMENSION_LIMIT_CM = 150
VOLUME_LIMIT_CM3 = 1000000

class Stacks(Enum):
    STANDARD = "STANDARD"
    SPECIAL = "SPECIAL"
    REJECTED = "REJECTED"

def is_heavy(mass_in_kg: float) -> bool:
    return mass_in_kg >= MASS_LIMIT_KG

def is_bulky(width_cm: float, height_cm: float, length_cm: float) -> bool:
    if width_cm >= DIMENSION_LIMIT_CM or height_cm >= DIMENSION_LIMIT_CM or length_cm >= DIMENSION_LIMIT_CM:
        return True

    return (width_cm * height_cm * length_cm) >= VOLUME_LIMIT_CM3

def sort(width_cm: float, height_cm: float, length_cm: float, mass_in_kg: float) -> Stacks:
    is_package_heavy = is_heavy(mass_in_kg)
    is_package_bulky = is_bulky(width_cm, height_cm, length_cm)

    if is_package_heavy and is_package_bulky:
        return Stacks.REJECTED

    if is_package_heavy or is_package_bulky:
        return Stacks.SPECIAL
    
    return Stacks.STANDARD