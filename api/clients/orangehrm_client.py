import requests

class OrangeHRMClient:
    def __init__(self,base_url):
        self.base_url = base_url

    def get(self,endpoint):
        response = requests.get(f"{self.base_url}{endpoint}")
        return response

    def post(self,endpoint,data):
        response = requests.post(f"{self.base_url}{endpoint}",json=data)
        return response