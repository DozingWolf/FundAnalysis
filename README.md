# FundAnalysis
利用公开数据接口进行基金数据的获取和分析

## 项目起源

2018年某同学联系告知其论文希望通过技术手段获取基金数据，遂建立本项目。

前期经过讨论，接口使用wind。但通过调查与相关业内前辈的讨论，发现wind在基金持仓数据方面没有公开的接口。

现时考虑使用tushare接口来进行基金持仓数据的获取。

未来若有其他变化，会在本文件进行说明。

## 项目分期

1. 一期希望先行获取各基金的季度持仓数据
2. 一期行业热点数据通过新闻报道的历史回溯进行
3. 二期进行分析数据分析
4. 二期分析结果考虑图形化展示

考虑到整个项目的时间围绕某同学的毕业论文时间节点，以上项目分期可能不一定准确。

具体请参见开发日志。

## 目录说明

*字体* 表示不一定存在该目录

/FundAnalysis
    -root

    ./Test
        -接口使用测试

    ./FundPosition_tushare/
        -基金持仓获取，使用tushare

    *./FundPosition_wind/*
        *-基金持仓获取，使用wind*

    ./Database/
        -ORM调用

    *./MQ/*
        *-MQ调用*

    ./SQL/
        -分析中使用的SQL语句整理

    ./Parameter/
        -配置文件

    ./Log/
        -日志文件

    ./DevelopmentLog.md
        -开发日志

    ./main.py
        -程序主调

## 程序思路

1. 调用接口
2. 格式化或剔除垃圾数据
3. 通过ORM写入DB
4. 在DB内进行数据分析
5. 有必要的话(如果数据量已经大到SQL处理不过来的话)考虑使用其他数据处理方式

## 使用组件

*字体* 表示不一定使用该组件

1. Python 3.6.5
2. ORM sqlalchemy　1.2.15
3. *pika 0.12.0*
