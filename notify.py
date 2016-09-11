from urllib2 import *
import urllib
import json
import sys

API_KEY="AIzaSyAMz5i6fNLl0oqlgCHfn2qO90p9ss4oMHU"

messageTitle = sys.argv[1]
messageBody = sys.argv[2]

data={
    "to" : "/topics/global",
    "notification" : {
        "body" : messageBody,
        "title" : messageTitle,
        "icon" : "ic_cloud_white_48dp"
    }
}

dataAsJSON = json.dumps(data)

request = Request(
    "https://gcm-http.googleapis.com/gcm/send",
    dataAsJSON,
    { "Authorization" : "key="+API_KEY,
      "Content-type" : "application/json"
    }
)

print urlopen(request).read()
