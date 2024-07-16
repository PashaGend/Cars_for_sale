import json



with open("TODO.json") as json_file:
     cars = json.load(json_file)

def all_cars():
     return cars

def specific_car(car_id):
#     get_one_car = [car for car in cars if car["id"] == id]
     get_one_car = []
     for car in cars:
          if car["car_id"] == car_id:
             get_one_car.append(car)
     if len(get_one_car) == 0:
          return "Car not found"
     return get_one_car

def delete_car(car_id):
    del_car = None
    for car in cars:
        if car['car_id'] == car_id:
            del_car = car
            break
    if del_car is None:
        return "Car not found"
    cars.remove(del_car)
    with open("TODO.json", "w") as json_file:
        json.dump(cars, json_file)
    return f"Car number: {car_id} deleted successfully"

def add_car(data):
    new_car_id = 1
    ids = []
    for car in cars:
        ids.append(car["car_id"]) # List of existing IDss
    while new_car_id in ids:  # Find a unique ID
        new_car_id += 1
    new_car = {"car_id": new_car_id, "car_make": data['car_make'], "car_model": data['car_model'], "make_year": data['make_year'], "color": data['color'], "car_price": data['car_price']}
    cars.append(new_car)
    with open("TODO.json", "w") as json_file:
        json.dump(cars, json_file)
    return f"New car number: {new_car_id} was added successfully"
