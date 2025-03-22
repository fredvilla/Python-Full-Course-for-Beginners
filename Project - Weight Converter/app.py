weight = int(input("Weight: "))
lbs_or_kg = input("(L)bs or (K)g: ")

if lbs_or_kg.upper() == "L":
    kg = 0.45 * weight
    print(f"You are {kg} kilos")
elif lbs_or_kg.upper() == "K":
    lbs = weight  / 0.45
    print(f"You are {lbs} pounds")