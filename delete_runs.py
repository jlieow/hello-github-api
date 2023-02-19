import http.client
import json

conn = http.client.HTTPSConnection("api.github.com")
payload = ''
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer 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',
  'User-Agent': 'PostmanRuntime/7.29.2'
}
conn.request("GET", "/repos/jlieow/slack-bot-github-api/actions/runs", payload, headers)
res = conn.getresponse()
data = res.read()

jsonData = json.loads(data)
print(jsonData["total_count"])
print(len(jsonData["workflow_runs"]))
print(jsonData["workflow_runs"][0]["id"])

for i in range(len(jsonData["workflow_runs"])):
#     print(i)
    conn = http.client.HTTPSConnection("api.github.com")
    payload = ''
    headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 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',
    'User-Agent': 'PostmanRuntime/7.29.2'
    }
    conn.request("DELETE", "/repos/jlieow/slack-bot-github-api/actions/runs/%s" % jsonData["workflow_runs"][i]["id"], payload, headers)
