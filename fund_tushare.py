# -*- coding: utf-8 -*-
__author__ = 'DozingWolf'

# import sys
# import codecs
# sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
import sys
# sys.path.append('..')
# print(sys.path)
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.AL32UTF8'
import tushare as ts
import time
from sqlalchemy import *
#
from Database.getData import *
# FUND_TUSHARE/FUND_TUSHARE
print('================================================')
print('================================================')
print('================================================')
print('================================================')
print('================================================')
print('==========WELCOME==TO==DATA==SYSTEM=============')
print('================================================')
print('================================================')
print('================================================')
print('================================================')

token = input('input u r token: ')

print('token was :',token)

base_ts = ts.pro_api(token)

print('================================================')
print('=====================NEXT=======================')
print('================================================')

db_ip = input('input u r ip: ')

print('ip was :',db_ip)

print('================================================')
print('=====================NEXT=======================')
print('================================================')

db_sid = input('input u r db sid: ')

print('db sid was :',db_sid)

print('================================================')
print('====================START=======================')
print('================================================')

# base_ts = ts.pro_api('')
def countdownTimer(timer = 60,interval = 1):
    print('please wait a minutes...')
    for i in range(0,timer):
        print(timer-i)
        if timer-i == 1:
            print('ready...')
        time.sleep(1)
    print('Go! Next around!')

def getCCTVnews(ts_base,time):
    newslist = ts_base.cctv_news(date=time)
    return newslist

def getFundInformation(ts_base,market='E'):
    FundInformationList = ts_base.fund_basic(market=market,encoding='utf-8')
    return FundInformationList
#
def getFundPosition(ts_base,fundcode):
    FundPositionInfo = ts_base.fund_portfolio(ts_code=fundcode)
    return FundPositionInfo

# 从接口获取基金数据后再获取
# 因tushare接口存在超时的情况，这个函数仅可以在少量数据的情况下进行使用。若存在较大量数据，请使用DB获取方式
def getMultiFundPosition(ts_base,fund_df,conn):
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
        FundPositionInfo_set.to_sql(name='FUND_POSITION_LIST', con=conn, if_exists='append')
        print(FundPositionInfo_set)
    return FundPositionInfo_set

# 从DB获取基金数据后再获取
# 业务流程：
#   1. 先获取基金列表，条件为未处理数据
#   2. 取出基金列表后传参给函数
#   3. 确认取到接口数据后进行回写基金表
#   4. 考虑超时后自动重启数据获取
#   5. 若没有获取到任何未处理的基金数据，退出
def getMultiFundPositionFromDB(ts_base,fund_table,conn,dbsession):
    fundDataList = fund_table
    for key,value in enumerate(fundDataList):
        print('No.',key,'value ',value,'type of value', type(value),'value[1]',value[0],'value[2]',value[1])
        # test
        #=========================================================================================
        FundPositionInfo_set = ts_base.fund_portfolio(ts_code=value[1])
        if key>0 and key%59 == 0:
            countdownTimer(timer = 60)
        FundPositionInfo_set.to_sql(name='FUND_POSITION_LIST', con=conn, if_exists='append')
        # update fund data
        wbAction = dbsession.query(FUND_INFO_LIST_WORK).filter_by(ID = value[0]).first()
        wbAction.GETDATA_FLAG='10'
        dbsession.commit()
        # print(FundPositionInfo_set)
    # return FundPositionInfo_set

engine = createEngine('FUND_TUSHARE', 'FUND_TUSHARE', db_ip, 1521, db_sid)
CreateorReplaceTable(engine)
session = sessionmaker(bind=engine)
sess = session()
result_data = []
# 此处要根据业务需求添加一些查询条件，等待业务反馈数据再进行处理。
for row in sess.query(FUND_INFO_LIST_WORK).filter_by(GETDATA_FLAG='00').filter_by(INVEST_TYPE='???'):
    # print('Fund code =',row.TS_CODE,' id =',row.ID)
    row_data = []
    row_data.append(int(row.ID))
    row_data.append(row.TS_CODE)
    result_data.append(row_data)
# print(result_data)
# fundInfoList_o = getFundInformation(base_ts,market='O')
# fundInfoList_e = getFundInformation(base_ts)
####MultiFundPosition_set = getMultiFundPosition(base_ts, fundInfoList_o)
MultiFundPosition_set = getMultiFundPositionFromDB(base_ts,result_data,engine,sess)
# countdownTimer(time = 60)
# MultiFundPosition_set = getMultiFundPosition(base_ts, fundInfoList_e)

# fundInfoList.to_sql(name='FUND_INFO_LIST', con=orcl12c, if_exists='append')

# print(type(fundInfoList))
