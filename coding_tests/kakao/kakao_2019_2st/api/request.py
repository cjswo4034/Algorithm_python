from model import call
from model import elevator

import requests

class Request:
    def __init__(self, url):
        self.url = url
        self.action_uri = f'{url}/action'
        self.oncalls_uri = f'{url}/oncalls'

    def start(self, user_key, prob_id, elv_cnt):
        start_uri = f'{self.url}/start/{user_key}/{prob_id}/{elv_cnt}'
        res = requests.post(start_uri)
        status = res.status_code
        msg = ""
        if status == 200:
            self.token = res.json()['token']
            self.headers = {'X-Auth-Token': self.token}
            return self.to_elevators(res.json()["elevators"])
        elif status == 400: msg, error = "Bad Request", ValueError
        elif status == 401: msg, error = "Unauthrized", TypeError
        elif status == 403: msg, error = "Forbidden", KeyError
        else: msg, error = "Internal Server Error", ConnectionError
        print(msg)
        raise error

    def action(self, cmds, calls=None):
        res = requests.post(self.action_uri, headers=self.headers, json={'commands': cmds})
        status = res.status_code
        if status == 400: print(cmds)
        json = res.json()
        return json["is_end"]

    def oncalls(self):
        res = requests.get(self.oncalls_uri, headers=self.headers)
        status = res.status_code
        if status == 400: print(res)
        json = res.json()
        elev = self.to_elevators(json["elevators"])
        call = self.to_calls(json["calls"])
        return [elev, call, json["is_end"]]

    def to_calls(self, res_calls):
        return call.Call(res_calls)

    def to_elevators(self, res_elevators):
        return [elevator.Elevator(res_elevator) for res_elevator in res_elevators]