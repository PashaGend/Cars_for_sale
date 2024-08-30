import unittest
from cars_db import all_cars, specific_car, delete_car
import json

class TestCarsDB(unittest.TestCase):
    def setUp(self):
        # Define a JSON file containing the list of cars
        with open('cars_list.json', 'r') as f:
            self.cars = json.load(f)

    def test_all_cars_from_json(self):
        # Test that the all_cars() function returns the correct list of cars from the JSON file
        result = all_cars()
        self.assertEqual(result, self.cars)

    def test_delete_car(self):
        # Test that the delete_car() function removes the correct car from the list and updates the JSON file
        car_id = 1
        delete_car(car_id)
        result = all_cars()
        self.assertNotIn({"car_id": 1}, result)

if __name__ == '__main__':
    unittest.main()
