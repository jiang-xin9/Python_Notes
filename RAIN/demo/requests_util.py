import json

import requests


class RequestsUtil:
    session=requests.session()

    def send_request(self,method,url,data,**kwargs):

        method=str(method).lower()
        rep=None
        if method=="get":
            rep = self.session.request(method, url=url, params=data, **kwargs)
        else:
            data=json.dumps(data)
            rep = self.session.request(method, url=url, data=data, **kwargs)
        return rep.text