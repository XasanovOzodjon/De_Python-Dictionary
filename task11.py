config = {}

for i in range(3):
    key = input(f"{i+1} key= ")
    va1ue = input(f"{i+1} value= ")
    config.update({key:va1ue})
    print()

print(config)