# To Make the POST, PUT, PATCH, DELETE, GET
import json

import requests

# HTTP Methods - Generic Functions

#Get request
def get_request(url,auth,in_json):
    response = requests.get(url=url, auth=auth)
    if in_json is True:
        return response.json()
    else:
        return response

# Post Request
def post_request(url, auth, headers, payload, in_json):
    post_response = requests.post(url=url,auth=auth,headers=headers,data=json.dumps(payload))
    if in_json is True:
        return post_response.json()
    else:
        return post_response

# Patch Request
def patch_request(url, auth, headers, payload, in_json):
    patch_response = requests.patch(url=url,auth=auth,headers=headers,data=json.dumps(payload))
    if in_json is True:
        return patch_response.json()
    else:
        return patch_response

# Put Request
def put_request(url, auth, headers, payload, in_json):
    put_response = requests.put(url=url,auth=auth,headers=headers,data=json.dumps(payload))
    if in_json is True:
        return put_response.json()
    else:
        return put_response

# Delete Request
def delete_request(url, auth, headers, payload, in_json):
    delete_response = requests.put(url=url,auth=auth,headers=headers)
    if in_json is True:
        return delete_response.json()
    else:
        return delete_response