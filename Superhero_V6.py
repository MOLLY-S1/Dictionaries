hero0 = {"Name": "Materdon", "Power": "Flight", "Strength": 5, "Speed": 12}
hero1 ={"Name": "Orsay", "Power": "x-ray vision", "Strength": 2, "Speed": 8}
hero_list = [hero0,hero1]
print(hero_list)

for i in hero_list:
    print(f"{i['Name']}'s superpower is {i['Power']} and their strength value "
          f"is {i['Strength']}")
