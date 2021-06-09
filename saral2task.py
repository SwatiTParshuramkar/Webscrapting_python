
from saral1task import scrape_top_list
import json
import requests
from bs4 import BeautifulSoup
from pprint import pprint

# 1.code - error is that, create the json file but not sequencewise year.
# we want year wise movie list.  

# movies_list = scrape_top_list()   

# def group_by_year(movies):
# 	years={}
# 	for i in movies:
# 		year=i["year"]
# 		years[year]=[]
# 		print(years)	
# 	for j in years:
# 		for key in movies:
# 			movies_year=key["year"]
# 			if j==movies_year:
# 				years[j].append(key)
# 	with open("year_list_movie.json","w") as saral :
# 		data2 =json.dump(years,saral,indent=4)

# 	return(years)

# group_by_year(movies_list)


# 2.code. but here not create json file.

# top_movies_list = scrape_top_list()   

# def group_by_year(movies):
# 	years={}
# 	for i in movies:
# 		year=i["year"]
# 		years[year]=[]	
# 	for j in years:
# 		for key in movies:
# 			movies_year=key["year"]
# 			if j==movies_year:
# 				years[j].append(key)
# 	return(years)

# pprint(group_by_year(top_movies_list))

from saral1task import scrape_top_list
import requests
import json
from bs4 import BeautifulSoup 
from pprint import pprint

data2=scrape_top_list()

realsing_year = []
unique_year = []
def group_by_year ():
    index = 0
    while index < len(data2):
        year = data2[index]["year"]
        realsing_year.append(year)
        index = index +1
    index2 = 0
    while index2 <len(realsing_year):
        if realsing_year[index2] not in unique_year:
            unique_year.append(realsing_year[index2])
        index2 = index2+1
    index3 = 0
    while index3 < len(unique_year):
        i = 0
        while i < len(unique_year):
          if unique_year[index3] < unique_year[i]:
            a = unique_year[index3]
            b = unique_year[i]
            unique_year[index3] = b
            unique_year[i] = a
          i = i + 1
        index3 = index3 + 1 
    my_dict = {}
    a = 0
    while a < len(unique_year):
        list2 = []
        b = 0
        while b < len(data2):
            if unique_year[a] == data2[b]["year"]:
                if data2[b] not in list2:
                    list2.append(data2[b])
            b = b + 1
        my_dict[unique_year[a]] = list2 
        a = a + 1
    with open ("year_vise_movies.json","w") as sara_data2:
        json.dump(my_dict,sara_data2,indent = 4)
    return(my_dict)
group_by_year()

    

    


    
    

