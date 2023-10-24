"""Practice with dictionaries"""

# Create a new dictionary
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}

# add elements using subscription notation
ice_cream["mint"] = 3

# remove element using pop()
ice_cream.pop("mint")

# modify/update element using subscription notation
ice_cream["vanilla"] = 10

# access a value
print(f"There are {ice_cream['chocolate']} orders of chocolate")

# len(dict)
print(f"There are {len(ice_cream)} flavors available ({len(ice_cream)} key-value pairs).")

# check if key in dictionary!
if "chocolate" and "vanilla" in ice_cream:
    print("Both flavors available")

if "mint" in ice_cream:
    print(f"{ice_cream['mint']} orders of mint.")
else:
    print("No orders of mint")

print("Mint in dictionary?")
print("mint" in ice_cream) # prints True or False

# loop through dictionary
for flavor in ice_cream:
    print(f"{flavor.title()} has {ice_cream[flavor]} orders.")