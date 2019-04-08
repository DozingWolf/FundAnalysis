# -*- coding: utf-8 -*-
__author__ = 'DozingWolf'

# import sys
# import codecs
# sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.AL32UTF8'
import tushare as ts
import time
from sqlalchemy import *
# token = input('input u r token: ')
#
# print('token was :',token)
#
# base_ts = ts.pro_api(token)

base_ts = ts.pro_api('')

def createEngine(user, password, ip, port, sid):
    db_engine = create_engine('oracle://%s:%s@%s:%d/%s'%(user, password, ip, port, sid ), echo=True,encoding = 'utf-8') #,encoding=''
    return db_engine
# FUND_TUSHARE/FUND_TUSHARE

orcl12c = createEngine(user='', password='', ip='', port=1521, sid='')

def getCCTVnews(ts_base,time):
    newslist = ts_base.cctv_news(date=time)
    return newslist

def getFundInformation(ts_base,market='E'):
    FundInformationList = ts_base.fund_basic(market=market,encoding='utf-8')
    return FundInformationList

def getStockInformation(ts_base,exc='',l_status='L'):
    StockInformationList = ts_base.stock_basic(exchange=exc, list_status=l_status, fields='ts_code,symbol,name,area,industry,market,exchange,list_status,delist_date,list_date')
    return StockInformationList

stockInfoList = getStockInformation(ts_base=base_ts)

print(stockInfoList)

stockInfoList.to_sql(name='STOCK_INFO_LIST', con=orcl12c, if_exists='append')
