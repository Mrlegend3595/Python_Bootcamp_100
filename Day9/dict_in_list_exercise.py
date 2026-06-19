travel_log = [
{
    "country": "France",
    "citties": ["Paris","Lille","Dijon"],
    "visits": 12,
},
{
    "country": "Germany",
    "citties": ["Berlin","Hamburg","Stuttgart"],
    "visits": 5,
},   
]

#dont change above

#write a function that will allow new country and entries
#to be added to travel_log
def add_new_country(name_country,num_visits,citties):
    new_country = {}
    
    new_country["country"] = name_country
    new_country["citties"] = citties
    new_country["visits"] = num_visits
    
    travel_log.append(new_country)

#dont change below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
