import requests
from pandas.core.base import PandasObject
URL = "https://df-cloud.org"
def to_cloud(df):
    requests.post(URL, data=df.to_json)
PandasObject.to_cloud = to_cloud
