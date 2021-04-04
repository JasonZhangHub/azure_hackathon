import urllib
import urllib.request
import streamlit
# If you are using Python 3+, import urllib instead of urllib2

import json

def app():
    date = streamlit.number_input('Insert a date later than 01042021')

    data = {

        "Inputs": {

            "input1":
                {
                    "ColumnNames": ["date", "new_cases", "group"],
                    "Values": [[date, "0", "1"]]
                }, },
        "GlobalParameters": {
        }
    }

    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/0f25f93b6ae74b47bd509b5c4cd3da44/services/4f73110eafae46d78b675de0c1528965/execute?api-version=2.0&details=true'
    api_key = ''  # Replace this with the API key for the Azure ML web service
    headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
        # req = urllib.request.Request(url, body, headers)
        # response = urllib.request.urlopen(req)

        result = response.read()
        print(result)

    except urllib.error.HTTPError:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())

        print(json.loads(error.read()))

    streamlit.write("Following is the predicted number of cases on the entered date:")
    streamlit.write(result[3])
