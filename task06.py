car = {
    "brand": "BMW",
    "model": "BMW M5",
    "color": "black",
    "year": 2024    
}
key = input("Kalit nomini kiritng: ").lower()

print(car.get(key, "Topilmadi"))