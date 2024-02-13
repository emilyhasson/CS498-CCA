import requests
import json
import uuid

url = "https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp3-lexv2-autograder"

payload = {
	"graphApi": "https://n4dj3szxq5.execute-api.us-east-1.amazonaws.com/beta", #<post api for storing the graph>,
	"botId": "1PZB62G1IV",# <id of your Amazon Lex Bot>, 
	"botAliasId": "NLVQYF5NUV",# <Lex alias id>,
	"identityPoolId": "us-east-1:a94934af-f92d-48ba-9e6e-d81ecd6b0875",#<cognito identity pool id for lex>,
	"accountId": "211125736007",#<your aws account id used for accessing lex>,
	"submitterEmail": "ehasson2@illinois.edu",# <insert your coursera account email>,
	"secret": "6LuSVyyXkwoMo951", # <insert your secret token from coursera>,
	"region": "us-east-1" #<Region where your lex is deployed (Ex: us-east-1)>
    }

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)

# curl -X POST https://n4dj3szxq5.execute-api.us-east-1.amazonaws.com/beta \
# -H "Content-Type: application/json" \
# -d '{"graph": "Chicago->Urbana,Urbana->Springfield,Chicago->Lafayette"}'
