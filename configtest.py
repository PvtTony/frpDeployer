# -*- coding:utf-8 -*-
import yamlconf

if __name__ == '__main__':
    config = yamlconf.get_config()
    print(config['aliyun'])
    for k in config['aliyun']:
        print("Key: {0}, Value: {1}".format(k, config['aliyun'][k]))
