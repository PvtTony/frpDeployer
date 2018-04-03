# -*- coding:utf-8 -*-

import requests


class FrpRelease(object):
    def __init__(self):
        self.__link_dict = dict()
        self.__pack_dict = dict()
        self.__release_requests = requests.get("https://api.github.com/repos/fatedier/frp/releases/latest")
        self.release_json_raw = self.__release_requests.json()
        index: int = 0
        for item in self.release_json_raw['assets']:
            release_name = item['name']
            if 'windows' in release_name:
                continue
            release_download_url = item['browser_download_url']
            index += 1
            self.__pack_dict[str(index)] = release_name
            self.__link_dict[release_name] = release_download_url

    def print_raw(self):
        print(self.release_json_raw)

    def get_release_name(self):
        return self.release_json_raw['name']

    def get_release_download_dict(self):
        return self.__link_dict

    def get_pack_dict(self):
        return self.__pack_dict


if __name__ == '__main__':
    frp = FrpRelease()
    # frp.print_raw()
    # print(frp.get_release_name())
    release_dict = frp.get_pack_dict()
    for k in release_dict:
        print(k + ': ' + release_dict.get(k))
