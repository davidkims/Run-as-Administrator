\set ACC :ACC
with s as (select generate_series(1, :ACC) as i)
insert into accounts(account_no, holder_name)
select 'V' || to_char(i,'FM000000'), 'User ' || i from s
on conflict (account_no) do nothing;

with s as (select generate_series(1, :ACC) as i)
insert into balances(account_no, balance)
select 'V' || to_char(i,'FM000000'), 0 from s
on conflict (account_no) do nothing;
