import requests
from bs4 import BeautifulSoup
import json

# imbd = "https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in"
# imbd_url= requests.get(imbd)
# data = imbd_url.json
# soup = BeautifulSoup(imbd_url.text,"html.parser")
# soup1 = soup.find("div",class_= "lister")
# body = soup1.find("tbody",class_ = "lister-list")
# name = body.find_all("tr")
# list1 = []
# for tr in name :
#     title = tr.find("td",class_="titleColumn").a.get_text()
#     year = tr.find("td",class_="titleColumn").span.get_text()
#     # list1.append(title)
#     print(title,year)
# print(soup1)
# print(imbd_url)



#   Webscrapping - Task 1 - Create scrape_top_list func. & from Imbd website we have to take the movie list.
#   using requests,beatifulsoup and json.



def scrape_top_list():
    imbd = "https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in"
    imbd_url= requests.get(imbd)
    data = imbd_url.json
    soup = BeautifulSoup(imbd_url.text,"html.parser")
    soup1 = soup.find("div",class_= "lister")
    body = soup1.find("tbody",class_ = "lister-list")
    name = body.find_all("tr")
    list1 = []
    scrape_dict = {}
    serial_no = 0
    for tr in name :
        serial_no = serial_no + 1
        title = tr.find("td",class_="titleColumn").a.get_text()
        year = tr.find("td",class_="titleColumn").span.get_text()
        link = tr.find("td",class_="titleColumn").a['href']
        movie_link = 'https://www.imbd/com' + str(link)
        movie_rating = float(tr.find("td",class_="ratingColumn imdbRating").strong.get_text())
        scrape_dict['naame'] = title
        scrape_dict["year"] = int(year[1:5])
        scrape_dict["position"] = int(serial_no)
        scrape_dict["movie_rating"] = movie_rating 
        scrape_dict["movie_link"] = movie_link
        list1.append(scrape_dict.copy())
    with open ("movie_list.json","w") as imbd_data:
        data1 = json.dump(list1,imbd_data,indent = 4)
    return list1
scrape_top_list()

