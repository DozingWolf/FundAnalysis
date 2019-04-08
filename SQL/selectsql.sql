select * from fund_info_list where management like '%东方%';

select count(*) from fund_info_list;

select count(*) from stock_info_list;

select market from stock_info_list group by market;
