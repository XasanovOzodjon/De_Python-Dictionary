users = [
  {"id": 1, "active": True},
  {"id": 2, "active": True},
  {"id": 3, "active": True},
  {"id": 4, "active": True},
  {"id": 5, "active": True},
]

for user in users:
    user["active"] = True


for user in users:
    print(user)