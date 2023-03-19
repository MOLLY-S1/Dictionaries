hero0 = {"Name": "Materdon", "Power": "Flight", "Strength": 5}

print(hero0)

hero0["Speed"] = 12
print(hero0)

hero0["Strength"] = 6
print(hero0)

popped_item = hero0.pop("Power")
print(hero0)
print(popped_item)

print("\nSuperhero 1 Stats\n")
for i in hero0:
    print(f"{i}: {hero0[i]}")
