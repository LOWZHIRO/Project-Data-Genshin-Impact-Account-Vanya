import os
import random
import string
data=dict()
while True:
    os.system("cls")
    print(f"{'DATA GENSHIN ACCOUNT':_^35}" )
    keyfinal="".join(random.choice(string.ascii_uppercase) for i in range(3))
    uid=input("Enter User ID\t\t: ")
    ar=input("Enter Adventure Rank\t\t: ")
    main=input("Enter your Main\t: ")
    data[keyfinal]={'uidkey':uid, 'arkey':ar, 'mainkey':main}
    option=input("Would you like to add another input?(y/t): ").lower()
    if option == 't':
        break

print("-"*50)
print(f"KEY\t UID \t AR \t MAIN")
print("-"*50)
for key, value in data.items():
    print(f"{key}\t {data[key]['uidkey']}\t {data[key]['arkey']}\t {data[key]['mainkey']}")