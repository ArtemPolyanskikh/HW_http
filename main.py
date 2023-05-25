# Задача №1

import requests
from pprint import pprint
import json

responce = requests.get('https://akabab.github.io/superhero-api/api/all.json')

j_list = responce.json()
res = {}
for line in j_list:
    if line['name'] in ['Hulk', 'Captain America', 'Thanos']:
        res[line['name']] = line['powerstats']['intelligence']
    else:
        continue
smart = sorted(res.items(), key=lambda x: x[1], reverse=True)
print(smart[0][0])


#Задача №2

class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")
#
#
TOKEN =''
ya = YandexDisk(token=TOKEN)
pprint(ya.get_files_list())



import yadisk
y = yadisk.YaDisk(token=TOKEN)
print(y.check_token())
y.upload("text.txt", "/Netology/file1.txt")