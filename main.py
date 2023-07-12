# we have some more requests
# TODO
#  1.Get = we ask an external system for data
#  2.Post = we give data to system
#  3.Put = update data in external system
#  4.Delete = delete data in external system
#  we just use requests.name()

import requests
from datetime import datetime as dt

USERNAME = 'gaigo'
TOKEN = 'jew7ffuyyf7didf8'
GRAPH_ID = 'graph1'

# Creating user account
pixela_endpoint = 'https://pixe.la/v1/users'
user_param = {
	'token': TOKEN,
	'username': USERNAME,
	'agreeTermsOfService': 'yes',
	'notMinor': 'yes'
}

user_response = requests.post(url=pixela_endpoint, json=user_param)
# print(user_response.text)


# Creating a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_param = {
	'id': GRAPH_ID,
	'name': 'Weight Graph',
	'unit': 'Kg',
	'type': 'float',
	'color': 'ajisai'
}

# in this API, we need to provide the token using a header
header = {
	'X-USER-TOKEN': TOKEN
}

graph_response = requests.post(url=graph_endpoint, json=graph_param, headers=header)
# print(graph_response.text)


# Adding a pixel to the pixela
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = dt.now()
pixel_param = {
	# using strftime() method
	'date': today.strftime('%Y%m%d'),
	'quantity': '93.4'
}
another_param = {
	'date': '20230612',
	'quantity': '100'
}
pixel_response = requests.post(url=pixel_endpoint, json=pixel_param, headers=header)
another_response = requests.post(url=pixel_endpoint, json=another_param, headers=header)
# print(pixel_response.text)


# updating data
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
update_param = {
	'quantity': '93.3'
}
update_response = requests.put(url=update_endpoint, json=update_param, headers=header)
# print(update_response.text)


# deleting a pixel
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20230612"
delete_response = requests.delete(url=delete_endpoint, headers=header)
print(delete_response.text)
