# DICTIONARY: KEY VALUE PAITING.
# Unorderd ,  Mutable, and donot allow duplicate keys
dict1 = {
    "name" : "Omprakash Chaudhary",
    "age" : 23,
    "adress":"Bihar",
    "adult": True,
    "fav_movies":["krissh", "Indian"],
    "fav_food":["chicken boneless", "dal bhat chokha"],
    "marks": 67.4545,
    12.324:234.532,
    (23,324,25): "rajaoihg",
    "key": "Value"
}
print(dict1)

print(dict1["name"])

print(dict1["key"])

print(dict1[(23,324,25)])


#print(dict1["namesd"])           #keyerror


# what if we want to change the value of a key
dict1["adress"] = ["Patna, Bihar"]
print(dict1)

# what if we want to add a new key and its value

dict1["fav_book"] = ["psycopath"]
print(dict1)


null_dict = {}
print(null_dict)
null_dict["Company to invest in"] = ["asian paints", "mrf tyre", "ceat tyre", "britania"]
print(null_dict)
