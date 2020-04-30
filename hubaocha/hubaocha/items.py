# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HubaochaItem(scrapy.Item):
    RegistCapi = scrapy.Field()  # 注册资本
    StartDate = scrapy.Field()  # 注册时间
    No = scrapy.Field()  # 工商注册号
    OrgNo = scrapy.Field()  # 组织机构代码
    CreditCode = scrapy.Field()  # 统一社会信用代码
    EconKind = scrapy.Field()  # 公司类型
    # 字段值与统一社会信用代码字段值相同
    # nsrsbh = scrapy.Field()  # 纳税人识别号
    OperName = scrapy.Field()  # 法人
    BelongOrg = scrapy.Field()  # 登记机关
    UpdatedDate = scrapy.Field()  # 核准日期
    Scope = scrapy.Field()  # 经营范围
    Name = scrapy.Field()  # 公司名称
    Address = scrapy.Field()   # 公司地址

