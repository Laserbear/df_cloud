import requests
import pandas as pd

URL = "localhost"
def to_cloud(df):
    requests.post(URL+"hash", data=df.to_json)

def from_cloud(json_url):
    json = dict(request.get(json_url))
    df = pd.DataFrame.from_dict(json, orient='index')
    df.reset_index(level=0, inplace=True)
    return df

pd.core.base.PandasObject.to_cloud = to_cloud
pd.DataFrame.from_cloud = from_cloud
