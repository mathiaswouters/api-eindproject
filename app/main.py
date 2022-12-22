from fastapi import FastAPI, Query
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    #"*",
    #"http://127.0.0.1:5500",
    #"https://mathiaswouters.github.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=[""],
    allow_headers=[""],
)


# Class
class Car(BaseModel):
    id: int
    brand: str | None = None
    model: str | None = None
    year: str | None = Query(default=None)
    body_type: str | None = None
    power_hp: int | None = None
    cylinders: int | None = None
    liters: float | None = None


# List
car_list = []


# Database
car_list.append(Car(id=1, brand="Toyota", model="Land Cruiser", year="2007", body_type="SUV", power_hp=381,
                    cylinders=8, liters=5.7))
car_list.append(Car(id=2, brand="Chevrolet", model="Colorado ZR2", year="2022", body_type="Truck", power_hp=308,
                    cylinders=6, liters=3.6))
car_list.append(Car(id=3, brand="Land Rover", model="Defender 110", year="2007", body_type="SUV", power_hp=122,
                    cylinders=4, liters=2.4))
car_list.append(Car(id=4, brand="Toyota", model="Tacoma", year="2015", body_type="Truck", power_hp=278,
                    cylinders=6, liters=3.5))
car_list.append(Car(id=5, brand="Ford", model="Raptor", year="2019", body_type="Truck", power_hp=213,
                    cylinders=4, liters=2.0))
car_list.append(Car(id=6, brand="Jeep", model="Wrangler Rubicon", year="2017", body_type="SUV", power_hp=285,
                    cylinders=6, liters=3.6))
car_list.append(Car(id=7, brand="RAM", model="2500", year="2019", body_type="Truck", power_hp=410, cylinders=8,
                    liters=6.4))


# GET 1 - return all cars
@app.get("/cars")
async def get_cars():
    return car_list


# GET 2 - return all cars by body type
@app.get("/body_type/{body_type}")
async def get_cars_by_body_type(body_type: str):
    body = []
    for i in car_list:
        if i.body_type == body_type:
            body.append(i)
    return body


# GET 3 - return car by brand
@app.get("/brands")
async def get_cars_brand():
    main = []
    brands = []
    for i in car_list:
        if i.brand not in main:
            main.append(i.brand)
    for k in range(len(main)):
        cars_brand = []
        for m in car_list:
            if m.brand == main[k]:
                cars_brand.append(m)
        brands.append({"brand": main[k], "cars": cars_brand})
    return brands


# POST 1 - post new car
# EXAMPLE: http://127.0.0.1:8000/newcar/?id=8&brand=Ford&model=Mustang&year=1971&body_type=muscle&power_hp=266&cylinders
# =8&liters=5.8
@app.post("/newcar/")
async def post_newcar(id: int, brand: str | None = None, model: str | None = None, year: str | None = Query(
    default=None, min_length=4, max_length=4), body_type: str | None = None, power_hp: int | None =
                     None, cylinders: int | None = None, liters: float | None = None):
    for i in car_list:
        if i.brand == brand and i.model == model and i.year == year:
            return  {"Error": "Car already exists"}
    new_car = Car(id=id, brand=brand, model=model, year=year, body_type=body_type, power_hp=power_hp,
                  cylinders=cylinders, liters=liters)
    car_list.append(new_car)
    return new_car


# PUT 1 -
@app.put("/update/}")
async def update_cars(id: int, brand: str | None = None, model: str | None = None, year: str | None = None,
                      body_type: str | None = None, power_hp: int | None = None, cylinders: int | None = None,
                      liters: float | None = None):
    for i in car_list:
        if i.id == id:
            i.brand = brand
            i.model = model
            i.year = year
            i.body_type = body_type
            i.power_hp = power_hp
            i.cylinders = cylinders
            i.liters = liters
            return i
    return {"Error": "Car doesn't exists"}


# DELETE 1 -
@app.delete("/delete/")
async def delete_cars (brand: str | None = None, model: str | None = None):
    for i in car_list:
        if i.brand == brand and i.model == model:
            car_list.remove(i)
            return i
    return {"Error": "Car doesn't exists"}