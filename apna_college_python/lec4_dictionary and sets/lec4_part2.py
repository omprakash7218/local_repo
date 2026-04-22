# NESTED DICTIONARY

asian_paints = {
    "interior":
    {
        "economy":"tractor emulsion",
        "premium":"apcolite premium emulsion",
        "luxury":"royale shyne"
    },
    "exterior":
    {
        "economy":"ace exterior emulsion",
        "premium":"apex shyne",
        "luxury":"apex ultima"
    }
}
# print(asian_paints)
# print(asian_paints['exterior']['premium'])



#  METHODS IN DICTIONARY AS WE HAVE STUDIED FOR LIST , STRINGS , TUPLES 

print(list(asian_paints.keys()))   # It gives dict_keys, we can change this to list , tuples etc 
# print(asian_paints['exterior'].keys())  # this conversion is known as type cast
# print("\nend of the line ")
# print(tuple(asian_paints.keys()))

# print(str(asian_paints.keys()))

# print(list(asian_paints.keys()))

# # print(int(asian_paints.keys()))  it gives an error 
# # print(float(asian_paints.keys())) it will also give an error
# print(bool(asian_paints.keys()))

# # we can also know total number of keys

# print(len(asian_paints))
# print(len(list(asian_paints.keys())))


# print(asian_paints.values())
# #we can do the conversion herea also. list , bool etc

# print(asian_paints["interior"].items())
# #it gives tuple of items in the dictionary

# print(asian_paints.get("exterior"))
# # it gives values of key

# # print(asian_paints["abc"])            # it gives an error
# print(asian_paints.get("abc"))     # it gives a none but code runs without giving an error

# print("hello world")

# print("hello world")

# print("hello world")

# print("hello world")

# print("hello world")

# new_dict_primer = {"wall primer":("sparc", "trucare", "smartcare"),
#                     "wood primer":"trucare",
#                     "red oxide":("sparc","trucare")}

# asian_paints.update(new_dict_primer)
# print(asian_paints)