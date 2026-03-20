from pydantic import BaseModel, Field, ConfigDict
from robot import Stacks

class Package(BaseModel):
    width_cm: float = Field(gt=0)
    height_cm: float = Field(gt=0)
    length_cm: float = Field(gt=0)
    mass_kg: float = Field(gt=0)

class SortResponse(BaseModel):
    model_config = ConfigDict(use_enum_values=True)
    stack: Stacks