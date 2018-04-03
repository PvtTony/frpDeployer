# -*- coding:utf-8 -*-

import datetime
import json

from aliyunsdkcore.client import AcsClient
from aliyunsdkecs.request.v20140526 import AllocatePublicIpAddressRequest
from aliyunsdkecs.request.v20140526 import CreateInstanceRequest
from aliyunsdkecs.request.v20140526 import DescribeImagesRequest
from aliyunsdkecs.request.v20140526 import DescribeInstanceTypeFamiliesRequest
from aliyunsdkecs.request.v20140526 import DescribeInstanceTypesRequest
from aliyunsdkecs.request.v20140526 import DescribeSpotPriceHistoryRequest
from aliyunsdkecs.request.v20140526 import DescribeZonesRequest
from aliyunsdkecs.request.v20140526 import ModifyInstanceAutoReleaseTimeRequest
from aliyunsdkecs.request.v20140526 import StartInstanceRequest


class AliyunEcs(object):
    def __init__(self, acs_client: AcsClient):
        if acs_client is not None:
            self.client = acs_client

    @staticmethod
    def create_instance_request(zone_id, instance_type, instance_name , password,
                                security_group_id, image_id, price_limit=0.02, sys_disk_size=20):
        create_request = CreateInstanceRequest.CreateInstanceRequest()
        create_request.set_ZoneId(zone_id)
        create_request.set_SecurityGroupId(security_group_id)
        create_request.set_InstanceType(instance_type)
        create_request.set_ImageId(image_id)
        create_request.set_SecurityEnhancementStrategy("Active")
        create_request.set_SpotStrategy("SpotWithPriceLimit")
        create_request.set_SpotPriceLimit(price_limit)
        create_request.set_IoOptimized('optimized')
        create_request.set_InternetMaxBandwidthOut(100)
        create_request.set_InstanceName(instance_name)
        create_request.set_SystemDiskCategory('cloud_efficiency')
        create_request.set_SystemDiskSize(sys_disk_size)
        create_request.set_Password(password)
        return create_request

    def create_instance(self, request):
        response = self.client.do_action_with_exception(request)
        instance_id = json.loads(response.decode('utf-8'))['InstanceId']
        return instance_id

    def set_instance_auto_release(self, instance_id, time_release):
        request = ModifyInstanceAutoReleaseTimeRequest.ModifyInstanceAutoReleaseTimeRequest()
        request.set_InstanceId(instance_id)
        request.set_AutoReleaseTime(time_release)
        response = self.client.do_action_with_exception(request)
        return response.decode('utf-8')

    def allocate_public_ip(self, instance_id):
        request = AllocatePublicIpAddressRequest.AllocatePublicIpAddressRequest()
        request.set_InstanceId(instance_id)
        response = self.client.do_action_with_exception(request)
        return json.loads(response.decode('utf-8'))['IpAddress']

    def start_instance(self, instance_id):
        request = StartInstanceRequest.StartInstanceRequest()
        request.set_InstanceId(instance_id)
        response = self.client.do_action_with_exception(request)
        return response.decode('utf-8')

    def get_zone_id(self):
        request = DescribeZonesRequest.DescribeZonesRequest()
        request.set_SpotStrategy('SpotWithPriceLimit')
        response = self.client.do_action_with_exception(request)
        return json.loads(response.decode('utf-8'))

    def get_spot_price_history(self, zone_id='cn-hangzhou-b', network_type='classic', instance_type='ecs.xn4.small'):
        request = DescribeSpotPriceHistoryRequest.DescribeSpotPriceHistoryRequest()
        request.set_ZoneId(zone_id)
        request.set_NetworkType(network_type)
        request.set_InstanceType(instance_type)
        response = self.client.do_action_with_exception(request)
        return json.loads(response.decode('utf-8'))

    # 查询云服务器 ECS 提供的实例规格族资源
    def get_ecs_type_families(self):
        request = DescribeInstanceTypeFamiliesRequest.DescribeInstanceTypeFamiliesRequest()
        response = self.client.do_action_with_exception(request)
        families = json.loads(response.decode('utf-8'))['InstanceTypeFamilies']['InstanceTypeFamily']
        for family in families:
            family_id = family['InstanceTypeFamilyId']
            family['InstanceTypes'] = self.get_ecs_type(family_id)
        return families

    # 查询云服务器 ECS 提供的实例规格资源
    def get_ecs_type(self, family_id):
        request = DescribeInstanceTypesRequest.DescribeInstanceTypesRequest()
        request.set_InstanceTypeFamily(family_id)
        response = self.client.do_action_with_exception(request)
        return json.loads(response.decode('utf-8'))['InstanceTypes']['InstanceType']

    # 查询可以使用的镜像资源
    def get_ecs_images_list(self):
        request = DescribeImagesRequest.DescribeImagesRequest()
        request.set_PageSize(30)
        response = self.client.do_action_with_exception(request)
        json_response = json.loads(response.decode('utf-8'))
        return json_response['Images']['Image']

    @staticmethod
    def get_default_time_release(release_minutes=15):
        time_release = datetime.datetime.combine(datetime.date.today(), datetime.time.min) + datetime.timedelta(
            days=1) + datetime.timedelta(minutes=release_minutes) - datetime.timedelta(hours=8)
        return time_release.isoformat() + 'Z'


# if __name__ == '__main__':
#     aliyun = AliyunEcs(client)
    # print(aliyun.get_zone_id())
    # print(aliyun.get_spot_price_history())
    # print(aliyun.get_spot_price_history('cn-hangzhou-f'))
    # print(aliyun.get_spot_price_history('cn-hangzhou-e'))
    # print(aliyun.get_ecs_type_families())
    # print(aliyun.get_ecs_type('ecs.xn4'))
