
car1 = {
    "brand": "Chevrolet",
    "model": "Cobalt",
    "color": "white"}

car2 = {
    "brand": "BMW",
    "model": "BMW M5",
    "color": "black",
    "year": 2024    
}

print(car1.get("year", car1))
print(car2.get("year", car2))