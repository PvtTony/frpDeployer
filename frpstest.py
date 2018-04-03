# -*- coding:utf-8 -*-

from frpconfig import FrpsConfig

if __name__ == '__main__':
    frps_config = FrpsConfig()
    frps_config.load_config()
    print('Keys in [common]')
    for key in frps_config.server_config:
        print("Key: {0}, Value: {1}".format(key, frps_config.server_config[key]))
    frps_config.set_tcp_server_bind_port('7001').save_config()
