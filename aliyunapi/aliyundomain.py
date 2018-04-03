# -*- coding:utf-8 -*-
from aliyunsdkcore.client import AcsClient
from aliyunsdkalidns.request.v20150109 import AddDomainRecordRequest
from aliyunsdkalidns.request.v20150109 import DescribeDomainRecordsRequest
from aliyunsdkalidns.request.v20150109 import UpdateDomainRecordRequest
import json


class AliyunDomain(object):
    def __init__(self, client: AcsClient):
        self.client = client

    def add_domain_record(self, domain_name, value, record_type='A', rr='frp', priority=1):
        request = AddDomainRecordRequest.AddDomainRecordRequest()
        request.set_DomainName(domain_name)
        request.set_RR(rr)
        request.set_Type(record_type)
        request.set_Value(value)
        request.set_Priority(priority)
        response = self.client.do_action_with_exception(request)
        return json.loads(response.decode('utf-8'))['RecordId']

    def search_domain_record_list_by_rr(self, domain_name, rr_keyword='frp', page_size=10, index=1):
        request = DescribeDomainRecordsRequest.DescribeDomainRecordsRequest()
        request.set_PageSize(page_size)
        request.set_PageNumber(index)
        request.set_DomainName(domain_name)
        request.set_RRKeyWord(rr_keyword)
        response = self.client.do_action_with_exception(request)
        return json.loads(response.decode('utf-8'))['DomainRecords']['Record']

    def modify_domain_record(self, record_id, value, record_type='A', rr='frp', priority=1):
        request = UpdateDomainRecordRequest.UpdateDomainRecordRequest()
        request.set_RecordId(record_id)
        request.set_Value(value)
        request.set_Type(record_type)
        request.set_RR(rr)
        request.set_Priority(priority)
        response = self.client.do_action_with_exception(request)
        return json.loads(response.decode('utf-8'))['RecordId']

    def get_domain_record_list(self, domain_name, page_size=10, index=1):
        request = DescribeDomainRecordsRequest.DescribeDomainRecordsRequest()
        request.set_PageSize(page_size)
        request.set_PageNumber(index)
        request.set_DomainName(domain_name)
        response = self.client.do_action_with_exception(request)
        return json.loads(response.decode('utf-8'))['DomainRecords']['Record']
