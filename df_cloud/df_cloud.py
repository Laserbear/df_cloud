import requests
from pandas.core.base import PandasObject
URL = "https://dfcloud.com"
def to(df):
    requests.post(URL, json = myobj)
PandasObject.to = to
