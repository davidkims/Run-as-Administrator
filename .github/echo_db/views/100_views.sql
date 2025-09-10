create or replace view v_income_statement as
select date_trunc('day', ts) as d,
       sum(case when direction='IN'  then amount else 0 end) as revenue,
       sum(case when direction='OUT' then amount else 0 end) as expense,
       sum(case when direction='IN'  then amount else -amount end) as profit
from transactions
group by 1
order by 1;

create or replace view v_balance_sheet as
select sum(balance) as total_assets
from balances;

-- TD-Sim: Teradata 스타일 요약 뷰(간단)
create or replace view td_sim_daily as
select date_trunc('day', ts) as d,
       count(*) as txn_cnt,
       sum(amount) filter (where direction='IN') as sum_in,
       sum(amount) filter (where direction='OUT') as sum_out
from transactions
group by 1
order by 1;
