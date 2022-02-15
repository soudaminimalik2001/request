# import requests
  
# # api-endpoint
# URL = "http://maps.googleapis.com/maps/api/geocode/json"
  
# # location given here
# location = "delhi technological university"
  
# # defining a params dict for the parameters to be sent to the API
# PARAMS = {'address':location}
  
# # sending get request and saving the response as response 
import requests
import json
URL="http://saral.navgurukul.org/api/courses"
r=requests.get(url=URL)
data=r.json()
# print(data)
# n=0
with open("saral.json","w") as f:
    json.dump(data,f,indent=4)
    # print(y)n=0
    # for i in range(len(data)):
    #     if "id" in data:
    #         print(n,"id")
    #     n+=1 
    # n=0
    # for i in "saral.json":
    #    print(i)
x=open("saral.json")
y=json.load(x)
v=(y["availableCourses"])
# print(v)
n=1
d=[]
for j in v:
    print(n,j["name"],":-",j["id"])
    d.append(j["id"])
    # print(d)
    n=n+1
print(d)
number=int(input("enter number"))
course=requests.get("http://saral.navgurukul.org/api/courses/"+str(d[number-1])+"/exercises")
print(course)
course1=course.json()
count=1
for name in course1["data"]:
    print(count,":-",name["name"])
    count+=1


        
    
    