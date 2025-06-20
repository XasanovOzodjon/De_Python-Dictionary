def cheak_email(dic: dict)-> None:
    cheak = True
    email = dic["email"]
    ind = email.find("@")
    if ind == -1 and email.count("@") == 1:
        cheak = False
    if not email[:ind].isalnum():
        cheak = False
    if "." not in email[ind:]:
        cheak = False

    if not cheak:
        dic["email"] = "correct@email.com"
    

user = {
    "name": "Ali",
    "age": 25,
    "city": "Tashkent",
    "email":  "Ozodja$ds@fa.com"
}


cheak_email(user)

print(user)