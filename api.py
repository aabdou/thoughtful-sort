from fastapi import FastAPI
from schema import Package, SortResponse
from robot import sort

app = FastAPI()

@app.post("/api/sort", response_model=SortResponse)
def sort_package(package: Package):
    res = sort(package.width_cm, package.height_cm, package.length_cm, package.mass_kg)

    return SortResponse(stack=res)