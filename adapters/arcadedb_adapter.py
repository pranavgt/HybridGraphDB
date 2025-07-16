import requests

class ArcadeDBAdapter:
    def __init__(self, host='http://localhost:2480', user='root', password='root'):
        self.base_url = host
        self.auth = (user, password)

    def run_query(self, sql):
        resp = requests.post(
            f'{self.base_url}/command',
            auth=self.auth,
            json={"command": sql}
        )
        return resp.json()