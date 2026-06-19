#eazy dict
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    }

#best a list in dict
travel_log = {
    "France": ["Paris","Lille","Dijon"],
    "Germany": ["Berlin","Hamburg","Stuttgart"],
} #each key have only one value so we use a list or dict


#nest dict in dict
new_travel_log = {
    "France": {"citties_visited": ["Paris","Lille","Dijon"], "total_visited": 12,},
    "Germany": {"citties_visited": ["Berlin","Hamburg","Stuttgart"], "total_visited": 12,},   
}
#nesting dictionary in a list
new_travel_log1 = [
    {
        "country": "France",
        "citties_visited": ["Paris","Lille","Dijon"],
        "total_visited": 12,
    },
    {
        "country": "Germany",
        "citties_visited": ["Berlin","Hamburg","Stuttgart"],
        "total_visited": 5,
    },   
]
