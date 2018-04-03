# -*- coding:utf-8 -*-

from aliyunsdkcore.client import AcsClient
from aliyunapi import AliyunEcs
from aliyunapi import AliyunDomain
import yamlconf

if __name__ == '__main__':
    aliyun_config = yamlconf.get_config()['aliyun']

    access_key_id = aliyun_config['access_key']['id']
    access_key_secret = aliyun_config['access_key']['secret']
    default_region_id = aliyun_config['region_id']
    domain_name = aliyun_config['domain_name']
    default_instance_config = aliyun_config['default_instance']

    client = AcsClient(access_key_id, access_key_secret, default_region_id)
    ali_ecs = AliyunEcs(client)
    ali_dom = AliyunDomain(client)
    print('正在创建实例...')
    new_instance_request = ali_ecs.create_instance_request(default_instance_config['zone_id'],
                                                           default_instance_config['instance_type'],
                                                           default_instance_config['instance_name'],
                                                           default_instance_config['server_password'],
                                                           default_instance_config['security_group_id'],
                                                           default_instance_config['image_id'])
    instance_id = ali_ecs.create_instance(new_instance_request)
    print("实例ID：" + instance_id)
    ali_ecs.set_instance_auto_release(instance_id, ali_ecs.get_default_time_release())
    public_ip = ali_ecs.allocate_public_ip(instance_id)
    print("外网IP：" + public_ip)
    ali_ecs.start_instance(instance_id)
    domain_record = ali_dom.search_domain_record_list_by_rr(domain_name)
    if not domain_record:
        ali_dom.add_domain_record(domain_name, public_ip)
    else:
        record_id = domain_record[0]['RecordId']
        ali_dom.modify_domain_record(record_id, public_ip)
    print('访问地址：frp.{0}'.format(aliyun_config['domain_name']))
