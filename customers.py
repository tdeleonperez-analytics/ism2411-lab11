#---REFLECTION---
#1) In the real world, you'd use bracket notation [] when either they key must exist or when writing to the dictionary. You'd use the .get() method when you want to avoid a KeyError if the key doesn't exist, this saves the program from crashing and not running.
#2) It reminds me of excel pivot tables and the forumlas that you'd use such as SUMIFS and COUNTIFS. Python would be better because you can do loops for much larger tables that deals with millions of rows rather than just a couple.


#Excercise 1: One Customer
firstCustomer = {
    "Name" : "Jake",
    "Email" : "jdawg@email.com",
    "Tier" : "gold",
    "ytd_spend" : 14500.00
}
print(firstCustomer)

print()
#Excercise 2: Update and Add
firstCustomer["Phone"] = "561-118-2026"
print(firstCustomer)
firstCustomer["Tier"] = "platinum"
print(firstCustomer)
del firstCustomer["Email"]
print(firstCustomer)

print()
#Excercise 3: Safe Lookup
firstCustomer.get("Email", "no email on file") 
try:
    print(firstCustomer["Email"])
except KeyError:
    print("no email on file")

print()
#Excercise 4: Iterate
for key, val in firstCustomer.items():
    print(f"{key}: {val}")
print()
for key in firstCustomer: 
    print(key, firstCustomer[key])
    #Using .items() is more efficient than using the key to access the value in the dictionary.

print()
#Excercise 5: Lookup Table
tier_discounts = {"bronze": 0, "silver": .05, "gold": .10, "platinum": .15}
firstCustomer.get("Tier", "bronze")
discPrice = 200 - (200 * tier_discounts[firstCustomer["Tier"]])
print(f"Tier: {firstCustomer['Tier']}, Discount Amount: {tier_discounts[firstCustomer['Tier']]*100}%, Discounted Price: ${discPrice:.2f}")

print()
#Excercise 6: List of Dicts
dict1 = {
    "Name" : "Paul",
    "Email" : "Ptrail@email.com",
    "Tier" : "silver",
    "ytd_spend" : 8650.00
    }
dict2 = {
    "Name" : "Eve",
    "Email" : "AscEve@email.com",
    "Tier" : "platinum",
    "ytd_spend" : 14500.00
}
dict3 = {
    "Name" : "Becky",
    "Email" : "becksline@email.com",
    "Tier" : "bronze",
    "ytd_spend" : 2450.00
}
customers = [dict1, dict2, dict3]
for dict in customers:
    for key,val in dict.items():
        print(f"{key}: {val}")
    print("Discount on $300: ",300 - (300 * tier_discounts[dict["Tier"]]))
    print()

print()
#Excercise 7: Nested Catalog
catalog = {"Widget A": {"price": 9.99, "stock": 150}, "Gadget C": {"price": 49.99, "stock": 8}}
for key, val in catalog.items():
    if val["stock"] < 20:
        print(f"{key} is LOW ON STOCK. Only {val['stock']} left.")

print()
#Exercise 8: Sales by Region
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]
totalSouth = 0
totalNorth = 0
for value in transactions:
    if value.get("region" , 0) == "South":
        totalSouth += value.get("amount", 0)
    else: 
        totalNorth += value.get("amount", 0)
print(f"Total South: ${totalSouth}, Total North: ${totalNorth}")