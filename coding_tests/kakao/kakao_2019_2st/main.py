import time
import requests
import api.request

if __name__ == "__main__":
    url = 'http://192.168.99.100:8888'
    a = api.request.Request(url)
    a.start('tester', 2, 4)
    time.sleep(0.1)
    while True: 
        time.sleep(0.005)
        elevs, calls, res = a.oncalls()
        
        if res: break

        cmds = [elev.action(calls) for elev in elevs]

        time.sleep(0.005)
        res = a.action(cmds)
        
        if res: break