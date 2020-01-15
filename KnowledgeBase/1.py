import csv
from geopy.geocoders import Nominatim
import wikipedia
from subprocess import call
geolocator = Nominatim(user_agent="damn")
import subprocess

def getNames():
    f = open("names.txt" , "r");
    x = list(map(str , f.read().split('\n')))
    f.close()
    return x

def exportData(x,y,z,a):
    with open('data.csv', mode='w') as data:
        dopple = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for i in range(len(x)):
            dopple.writerow([x[i] , y[i] , z[i] , a[i]])

x = getNames()
y = []
z = []
# print(x)
for i in x:
    location = geolocator.geocode(i)
    if location is not None:
        y.append(location.longitude)
        z.append(location.latitude)
    else:
        y.append("-1")
        z.append("-1")

# for i in range(len(x)):
#     print(x[i] , "\t" , y[i] , "\t" , z[i])

a = []

for i in x:
    temp = (wikipedia.search(i))
    a.append(temp[0])

for i in range(len(a)):
    articleName = "_".join(list(a[i].split()))
    wiki = "www.wikipedia.com/wiki/"+articleName
    a[i] = wikipedia.summary(articleName)

exportData(x,y,z,a)
