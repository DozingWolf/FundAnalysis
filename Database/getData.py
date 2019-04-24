__author__ = 'DozingWolf'
import json
from datetime import datetime
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table,Column,MetaData
from sqlalchemy.orm import sessionmaker,query
from sqlalchemy.dialects.oracle import DATE,VARCHAR2,NUMBER

def createEngine(user, password, ip, port, sid):
    db_engine = create_engine('oracle://%s:%s@%s:%d/%s'%(user, password, ip, port, sid ), echo=False)
    return db_engine

Base = declarative_base()
#table model
class FUND_INFO_LIST_WORK(Base):
    __tablename__ = 'FUND_INFO_LIST_WORK'
    ID = Column(NUMBER,primary_key=True)
    TS_CODE	= Column(VARCHAR2(27))
    NAME = Column(VARCHAR2(63))
    MANAGEMENT = Column(VARCHAR2(27))
    CUSTODIAN = Column(VARCHAR2(18))
    FUND_TYPE = Column(VARCHAR2(15))
    FOUND_DATE = Column(VARCHAR2(24))
    DUE_DATE = Column(VARCHAR2(24))
    LIST_DATE = Column(VARCHAR2(24))
    ISSUE_DATE = Column(VARCHAR2(24))
    DELIST_DATE = Column(VARCHAR2(24))
    ISSUE_AMOUNT = Column(NUMBER)
    M_FEE = Column(NUMBER)
    C_FEE = Column(NUMBER)
    DURATION_YEAR = Column(NUMBER)
    P_VALUE = Column(NUMBER)
    MIN_AMOUNT = Column(NUMBER)
    EXP_RETURN = Column(VARCHAR2(30))
    BENCHMARK = Column(VARCHAR2(1200))
    STATUS = Column(VARCHAR2(3))
    INVEST_TYPE = Column(VARCHAR2(21))
    TYPE = Column(VARCHAR2(18))
    TRUSTEE = Column(VARCHAR2(50))
    PURC_STARTDATE = Column(VARCHAR2(24))
    REDM_STARTDATE = Column(VARCHAR2(24))
    MARKET = Column(VARCHAR2(3))
    GETDATA_FLAG = Column(VARCHAR2(2)

    def __repr__(self):
        return '<ALM_WECHAT_LIST(ID=%d,TS_CODE=%s,NAME=%s)>'%(self.ID,self.TS_CODE,self.NAME)


# engine = createEngine(db_ip,db_password,db_sid,db_user,db_password)

def CreateorReplaceTable(db_engine):
    Base.metadata.create_all(db_engine)

def CreateSession(db_engine):
    session = sessionmaker(bind=db_engine)
    return session()
