# -*- coding:utf-8 -*-

# import sys
import yaml


def get_config():
    file = open('config.yaml')
    content = yaml.load(file)
    return content
