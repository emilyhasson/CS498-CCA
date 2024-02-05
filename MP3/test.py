import requests
import json
import uuid

url = "https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp3-lexv2-autograder"

payload = {
	"graphApi": #<post api for storing the graph>,
	"botId": # <id of your Amazon Lex Bot>, 
	"botAliasId": # <Lex alias id>,
	"identityPoolId": #<cognito identity pool id for lex>,
	"accountId": #<your aws account id used for accessing lex>,
	"submitterEmail": # <insert your coursera account email>,
	"secret": # <insert your secret token from coursera>,
	"region": "us-east-1" #<Region where your lex is deployed (Ex: us-east-1)>
    }

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)