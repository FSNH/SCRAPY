#coding:utf-8
import scrapy
import re
from hubaocha.items import HubaochaItem


class HubaoSpider(scrapy.Spider):
    name = 'hubao'
    allowed_domains = ['hubocha.com']

    def start_requests(self):
        name = '南京云帐房网络科技有限公司'
        url = 'https://www.hubocha.com/searchCompany/{}'.format(name)
        yield scrapy.Request(url=url, meta={'name': name}, callback=self.parse_page)

    def parse_page(self, response):
        # print(response.text)
        # 公司名称
        name = response.meta['name']
        # print(name)
        companys = response.xpath('//div[@class="search-list bg-white"]/ul//li//a').extract()
        # a标签列表转换成str
        companys= ''.join(companys)
        # 正则匹配a标签的href和公司名称
        patter = re.compile(r'<a.*?href="(.*?)".*?>(.*?)</a>')
        company_infos = patter.findall(companys)
        # print(company_infos)
        # 提取出查询公司url
        for company_info in company_infos:
            # print(company_info)
            # 判断公司是否存在，存在则取出url并发送请求company_info[0]公司名,company_info[1]公司url
            if name in company_info:
                # print(company_info[0])
                yield scrapy.Request(url=company_info[0], callback=self.parse_detail)

    def parse_detail(self, response):
        # print(response.text)
        items = HubaochaItem()
        # infos列表保存所有工商信息
        infos = []
        infos_dict = dict()
        divs = response.xpath('//div[contains(@class,"col")]')
        for div in divs:
            info = div.xpath('.//p/text()').extract_first()
            # print(info)
            infos.append(info)
        # print(infos)
        # 将列表转化为k,v格式的字典中
        for k in range(0, len(infos)-1, 2):
            infos_dict[infos[k]] = infos[k + 1]
        # print(infos_dict)
        items['RegistCapi'] = infos_dict['注册资本']
        items['StartDate'] = infos_dict['注册时间']
        items['No'] = infos_dict['工商注册号']
        items['OrgNo'] = infos_dict['组织机构代码']
        items['CreditCode'] = infos_dict['统一社会信用代码']
        items['EconKind'] = infos_dict['公司类型']
        # items['nsrsbh'] = infos_dict['纳税人识别号']
        items['OperName'] = infos_dict['法人']
        items['BelongOrg'] = infos_dict['登记机关']
        items['UpdatedDate'] = infos_dict['核准日期']
        items['Scope'] = infos_dict['经营范围']
        items['Name'] = response.xpath('//div[@class="title"]/h5/text()').extract_first()
        items['Address'] = response.xpath('//div[@class="title"]/span[@class="address"]/text()').extract_first()
        yield items


