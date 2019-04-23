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

orcl12c = createEngine(user='FUND_TUSHARE', password='FUND_TUSHARE', ip='', port=1521, sid='')

def getCCTVnews(ts_base,time):
    newslist = ts_base.cctv_news(date=time)
    return newslist

def getFundInformation(ts_base,market='E'):
    FundInformationList = ts_base.fund_basic(market=market,encoding='utf-8')
    return FundInformationList

def getFundPosition(ts_base,fundcode):
    FundPositionInfo = ts_base.fund_portfolio(ts_code=fundcode)
    return FundPositionInfo

def getMultiFundPosition(ts_base,fund_df):
    fundDataList = list(fund_df.itertuples(index=False))
    for key,value in enumerate(fundDataList):
        print('No.',key)
        FundPositionInfo_set = ts_base.fund_portfolio(ts_code=value.ts_code)
        if key>0 and key%59 == 0:
            # time.sleep(60)
            print('please wait a minutes...')
            for i in range(0,60):
                print(60-i)
                if 60-i == 1:
                    print('ready...')
                time.sleep(1)
            print('Go! Next part of data!')
        FundPositionInfo_set.to_sql(name='FUND_POSITION_LIST', con=orcl12c, if_exists='append')
        print(FundPositionInfo_set)
    return FundPositionInfo_set

fundInfoList_o = getFundInformation(base_ts,market='O')
fundInfoList_e = getFundInformation(base_ts)
MultiFundPosition_set = getMultiFundPosition(base_ts, fundInfoList_o)
print('please wait a minutes...')
for i in range(0,60):
    print(60-i)
    if 60-i == 1:
        print('ready...')
    time.sleep(1)
print('Go! Next around!')
MultiFundPosition_set = getMultiFundPosition(base_ts, fundInfoList_e)

# fundInfoList.to_sql(name='FUND_INFO_LIST', con=orcl12c, if_exists='append')

# print(type(fundInfoList))
