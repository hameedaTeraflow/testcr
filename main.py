import os
from google.cloud import storage
import pip._vendor.requests
import json
import pandas as pd

from flask import Flask
app = Flask(__name__)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'teraflow-tarvis-lake-dev-6c6c4514197d.json'
storage_client = storage.Client()

dir(storage_client)

bucket_name = 'timeadmin_data_bucket'
bucket = storage_client.bucket(bucket_name)
bucket.location = 'US'
#bucket = storage_client.create_bucket(bucket)

apiKey = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjI1MDM1MjYxOSwidWlkIjoyNjgwNjY3OCwiaWFkIjoiMjAyMy0wNC0xMlQxNDo0NjowOS4wNDVaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6NDUyMDU1OSwicmduIjoidXNlMSJ9.ddVaxj8XcxuXK7ZQIQi438aX-8k5HZn36ymgz9GS-Jc"
apiUrl = "https://api.monday.com/v2"
headers = {"Authorization" : apiKey}

query2 = '{boards(ids:1980874898) { name id description items { name column_values{title id type text } } } }'
data = {'query' : query2}

@app.route('/')
def upload_to_bucket(self, project_name, df, destination_blob_name):
    try:

        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_string(df.to_csv(), 'text/csv')
        
        return True
    except Exception as e:
        print(e)
        return False
r = pip._vendor.requests.post(url=apiUrl, json=data, headers=headers) # make request
df = pd.read_json(r.text)
upload_to_bucket('time admin','timeadmin_data_bucket',df,'timeadmin_data_bucket010')
