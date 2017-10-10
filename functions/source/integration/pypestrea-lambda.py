import base64
import json
import os
import urllib
from urllib import request, parse

populated_url = "https://prod-webserviceext-v3r3.pype.tech/v3/broadcast"

def lambda_handler(event, context):

    customerPhoneNumber = event.get('Details').get('ContactData').get('CustomerEndpoint').get('Address');
    resultMap = {"lambdaResult": customerPhoneNumber, "lambdaResult": "Success"};
    client_Key = "please request from Pypestream"
    client_Secret = "please request from Pypestream"



    post_params = {"sms_user_msg": " sms ", "pypestream_user_msg": "hello app user!", "array_of_mobile_numbers": [ customerPhoneNumber ]}

    data = parse.urlencode(post_params).encode()

    req = request.Request(populated_url)
    req.add_header("Authorization", "{} {}".format(str(client_Key),str(client_Secret)))
    req.add_header("Content-Type", "application/json")
    req.add_header("Accept", "application/json")

    try:
        with request.urlopen(req, data) as f:
            print("Result is {}".format(str(f.read().decode('utf-8'))))
    except Exception as e:
        # something went wrong!
        return e

    return resultMap
