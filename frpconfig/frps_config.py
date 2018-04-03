# -*- coding:utf-8 -*-

import configparser


class FrpsConfig(object):
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config['common'] = {}
        self.server_config = self.config['common']
        self.load_config()

    def set_tcp_server_bind_port(self, bind_port='7600'):
        self.server_config['bind_port'] = bind_port
        return self

    def set_tcp_server_bind_address(self, bind_address='0.0.0.0'):
        self.server_config['bind_addr'] = bind_address
        return self

    def set_bind_udp_port(self, udp_port='7001'):
        self.server_config['bind_udp_port'] = udp_port
        return self

    def set_kcp_bind_port(self, kcp_bind_port='7000'):
        self.server_config['kcp_bind_port'] = kcp_bind_port
        return self

    def set_vhost_http_port(self, vhost_http_port='7001'):
        self.server_config['vhost_http_port'] = vhost_http_port
        return self

    def set_vhost_https_port(self, vhost_https_port='7001'):
        self.server_config['vhost_https_port'] = vhost_https_port
        return self

    def set_dashboard_addr(self, udp_port_number='7001'):
        self.server_config['bind_udp_port'] = udp_port_number
        return self

    def set_dashboard_port(self, udp_port_number='7001'):
        self.server_config['bind_udp_port'] = udp_port_number
        return self

    def set_dashboard_user(self, udp_port_number='7001'):
        self.server_config['bind_udp_port'] = udp_port_number
        return self

    def set_dashboard_pwd(self, udp_port_number='7001'):
        self.server_config['bind_udp_port'] = udp_port_number
        return self

    def set_log_file_path(self, log_file='./frps.log'):
        self.server_config['log_file'] = log_file
        return self

    def set_log_level(self, log_level='info'):
        self.server_config['log_level'] = log_level
        return self

    def set_log_max_days(self, log_max_days='3'):
        self.server_config['log_max_days'] = log_max_days
        return self

    def set_privilege_token(self, privilege_token='12345678'):
        self.server_config['privilege_token'] = privilege_token
        return self

    def set_privilege_allow_ports(self, privilege_allow_ports='2000-3000'):
        self.server_config['privilege_allow_ports'] = privilege_allow_ports
        return self

    def set_max_pool_count(self, max_pool_count='5'):
        self.server_config['max_pool_count'] = max_pool_count
        return self

    def set_max_ports_per_client(self, max_ports_per_client='0'):
        self.server_config['max_ports_per_client'] = max_ports_per_client
        return self

    def set_authentication_timeout(self, authentication_timeout='900'):
        self.server_config['authentication_timeout'] = authentication_timeout
        return self

    def set_subdomain_host(self, subdomain_host='frps.com'):
        self.server_config['subdomain_host'] = subdomain_host
        return self

    def set_tcp_mux(self, tcp_mux='true'):
        self.server_config['tcp_mux'] = tcp_mux
        return self

    def save_config(self, config_dir='frps.ini'):
        with open(config_dir, 'w') as config_write:
            self.config.write(config_write)

    def load_config(self, config_dir='frps.ini'):
        self.config.read(config_dir)

    def load_config_from_dict(self, config: dict):
        self.server_config = config
        return self

# if __name__ == '__main__':
#     frps_config = FrpsConfig()
#     frps_config.set_tcp_server_bind_address()\
#         .set_tcp_server_bind_port()
