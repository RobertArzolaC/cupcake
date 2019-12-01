import os
import requests
from elasticsearch import Elasticsearch


class Service():
    es_port = os.getenv('ELASTICSEARCH_PORT', 9200)
    es_host = os.getenv('ELASTICSEARCH_HOST', 'elasticsearch')

    def connect(self):
        return Elasticsearch(['elasticsearch:9200'])

    def sanitizer_query(self, query):
        resp = [item["_source"] for item in query["data"]["hits"]["hits"]]
        return resp

    def send_request(self, path, json=None, params=None):
        result = dict()
        endpoint = 'http://{host}:{port}/{path}'.format(
            host=self.es_host, port=self.es_port, path=path)

        if json:
            resp = requests.post(endpoint, json=json)
        else:
            resp = requests.get(endpoint, params=params)
        
        try:
            resp.raise_for_status()
            result.update(dict(
                status_code=resp.status_code, message="successful",
                data=resp.json()))
        except:
            result.update(dict(status_code=resp.status_code, error=resp.text))
        finally:
            return result
