import http.client

conn = http.client.HTTPConnection("demand.team22.softwareengineeringii.com:4001")

headers = {
    'cache-control': "no-cache"
    }

conn.request("GET", "/loginHandler", headers=headers)

res = conn.getresponse()
data = res.status
if (data != 200):
	print("Success")
else:
	print("Failure")


