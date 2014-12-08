import urllib2
from bs4 import BeautifulSoup
import csv
 
url = urllib2.urlopen("http://freekaamaal.com/")
 
soup = BeautifulSoup(url)
var = soup.find('title')
#print var4.text
#print " "
 
var1 = soup.find_all('h2', {"class" : "top-offers fltLeft width-100 margin-top-spacing-20"})

#for items in var1:
        #print items.text
        #print " "
var4 = soup.find_all('span', {"class" : "text-12 black-txt prefix-5 suffix-5"})
var2 = soup.find_all('div', {"class" : "old-rs light-txt text-12 fltLeft prefix-42 suffix-5 top-spacing-4"})
var3 = soup.find_all('div', {"class" : "offer-rs orange-text text-16 fltLeft prefix-5 suffix-5 font-bold"})
        #print var2
        #print " "
        #print var3
        #print " "
        #print var4

f = csv.writer(open("Data.csv", "w"))
f.writerow(["Product Name","Deal Price", "MRP"])

print "product name"
    #f.writerow(["Product Name"])
for items2 in var4:
        
    i = items2.text
    print i
    print " "
        
        #f.writerow(["i"])


print "Deal Price"
    #f.writerow(["Deal Price"])
for items1 in var3:
    j = items1.text
    print j
    print " "
        
        #f.writerow([items1.text])

print "MRP"
    #f.writerow(["MRP"])
for items in var2:
    k = items.text
    print k
    print " "
        
f.writerow([var, var2, var2])

    


print "Done writing file"   

soup.prettify()