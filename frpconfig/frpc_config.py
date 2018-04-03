# -*- coding:utf-8 -*-

import configparser


class FrpcConfig(object):
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config['common'] = {}
        self.common_config = self.config['common']

    def save_config(self):
        with open('frpc.ini', 'w') as config_write:
            self.config.write(config_write)

    def load_config(self):
        self.config.read('frpc.ini')

    def load_config_from_dict(self, config: dict):
        self.config = config
        return self
