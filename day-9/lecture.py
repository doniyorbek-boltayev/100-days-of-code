# dictionaries

fruits = {
    "apple": "red",
    "banana": "yellow",
    "pear": "green",
}
print(fruits["apple"])

# add new element
fruits["peeler"] = "orange"
print(fruits)

# create empty dictionary
empty_dictionary = {}

# edit an item in dictionary
fruits["apple"] = "blue"
print(fruits)

# loop through dictionary
for key in fruits:
    print(key) # this outputs key
    print(fruits[key]) # this outputs value

# wipe existing dictionary
fruits = {} # this wipes of all data inside fruits as python runs the code line by line
print(fruits)


capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",
}

# nested list in dictionary
travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Uzbekistan" : ["Tashkent", "Khorezm"],
}
# print Lille
print(travel_log["France"][1])


# nested list
nested_list = ["A", "B", ["C", "D"]]
# printing letter D
print(nested_list[2][1])

#nested dictionary inside dictionary
travel_logv2 ={
    "Uzbekistan" : {
        "num_times_visited" : 2,
        "cities_visited" : ["Tashkent", "Khorezm"],
    },
    "France" : {
        "num_times_visited" : 0,
        "cities_visited" : ["Paris", "Lille", "Dijon"],
    },
}
# print Khorezm
print(travel_logv2["Uzbekistan"]["cities_visited"][1])
