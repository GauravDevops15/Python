#get commit messages info on repo using python script
##steps
###python module to access github is requests
###requests
###API
###Json to dictionaries
###print output

import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetese/pulls")

complete_detail = response.json()

for i in range (len(complete_detail)):
    print(complete_detail[i]["user"]["login"])