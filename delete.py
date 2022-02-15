import requests

x = requests.delete("http://saral.navgurukul.org/api/courses")
# /delete",data ={"key":"value"})
# y=requests.delete(x)

print(x)
# print(x.json())


# import requests
  
# # Making a DELETE request
# r = requests.delete('https://httpbin.org / delete', data ={'key':'value'})
  
# # check status code for response received
# # success code - 200
# print(r)
  
# # print content of request
# print(r.json())