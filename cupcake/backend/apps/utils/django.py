import os
import requests
from urllib.parse import urlparse


class Service():
    django_port = os.getenv('DJANGO_PORT', 8000)
    django_host = os.getenv('DJANGO_HOST', 'django')
    django_token = os.getenv('DJANGO_TOKEN', 'django')

    def _get_basename(self, url):
        parsed = urlparse(url)
        return os.path.basename(parsed.path)

    def send_request(self, path, json=None, params=None):
        result = dict()
        headers = dict(Authorization='Token {0}'.format(self.django_token))
        endpoint = 'http://{host}:{port}/{path}'.format(
            host=self.django_host, port=self.django_port, path=path)

        if json:
            resp = requests.post(endpoint, headers=headers, json=json)
        else:
            resp = requests.get(endpoint, headers=headers, params=params)
        
        try:
            resp.raise_for_status()
            result.update(dict(
                status_code=resp.status_code, message="successful",
                data=resp.json()))
        except:
            result.update(dict(status_code=resp.status_code, error=resp.text))
        finally:
            return result

    def save_file_url(self, image_url):
        img = requests.get(image_url)
        filename = self._get_basename(image_url)
        files = {'file': (filename, img.content)}
        endpoint = 'http://{host}:{port}/files/'.format(
            host=self.django_host, port=self.django_port)
        resp = requests.post(endpoint, files=files)
        return resp.json()['filename']
