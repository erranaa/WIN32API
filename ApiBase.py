import urllib.request
import urllib.parse
import urllib.error
import json
from abc import ABCMeta
from abc import abstractmethod


class ApiBase:
    @abstractmethod
    def request(self, serviceurl):
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 ' \
                '(KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
        req = urllib.request.Request(serviceurl, headers=headers)
        resp = urllib.request.urlopen(req)
        respData = resp.read()
        return respData


class UserApi(ApiBase):
    def __init__(self, real_subject):
        self._real_subject = real_subject
    
    def request(self):
        try:
            serviceurl = 'https://randomuser.me/api/'
            
            respData = ApiBase.request(self, serviceurl)

            saveFile = open('user.json', 'w')
            resp = {"test1": "1", "test2": "2", "test3": "3"}
            
            json_str = json.dumps(resp)
            
            data = json.loads(json_str)
            
            with open('user.json', 'r') as f:
                objects = data.items()
                columns = list(objects)
            data = json.loads(respData)

            self.name = data['results'][0]['name']['first']
            self.surname = data['results'][0]['name']['last']


            saveFile.write(str(respData))
            saveFile.close()
            self._real_subject.request()

        except Exception as e:
            print ("A")


class BoredApi(ApiBase):
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        try:
            serviceurl = 'https://www.boredapi.com/api/activity'
            
            respData = ApiBase.request(self, serviceurl)


            saveFile = open('bored.json', 'w')
            resp = {"test1": "1", "test2": "2", "test3": "3"}
            
            json_str = json.dumps(resp)
            
            data = json.loads(json_str)
            

            with open('bored.json', 'r') as f:
                objects = data.items()
                columns = list(objects)
            data = json.loads(respData)

            ids = data['activity']
            ids2 = data['participants']

            print(ids)
            saveFile.write(str(respData))
            saveFile.close()
            self._real_subject.request()
            return ids2


        except Exception as e:
            print ("B")

class JokeApi(ApiBase):
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        try:
            serviceurl = "http://api.icndb.com/jokes/random?"

            respData = ApiBase.request(self, serviceurl)


            saveFile = open('joker.json', 'w')
            resp = {"type": "success", "value": { "id": 81, "joke": "John Norris invented his own type of karate. "
                "It\'s called John-Will-Kill.", "categories": []} }
            
            json_str = json.dumps(resp)
            
            data = json.loads(json_str)
            
            with open('joker.json', 'r') as f:
                objects = data.items()
                columns = list(objects)
            data = json.loads(respData)

            ids = data["value"]['joke']

            print(ids)

            saveFile.write(str(respData))
            saveFile.close()
            self._real_subject.request()


        except Exception as e:
            print ("C")




