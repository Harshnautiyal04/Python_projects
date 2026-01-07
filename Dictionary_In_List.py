travel_log = [
    {
    "country":"India",
    "visits":18,
    "cities":["New Delhi","Uttarakhand","Sikkim","Mizoram"]
},
    {
        "country":"Switzerland",
        "visits":22,
        "cities":["Zurich","Geneva","Basel","Bern"]
    }
]
def add_new_country(name,time_visits,list_of_cities):
    new_country={}
    new_country["country"] = name
    new_country["visits"] =  time_visits
    new_country["cities"] = list_of_cities
    travel_log.append(new_country)

add_new_country("Brazil",12,["Sao Paulo","Rio De Janeiro"])
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")


