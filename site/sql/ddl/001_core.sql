create table if not exists accounts (
  account_id bigserial primary key,
  account_no varchar(32) unique not null,
  holder_name varchar(128) not null,
  opened_at timestamptz not null default now(),
  status varchar(16) not null default 'ACTIVE'
);
create table if not exists journal_entries (
  je_id bigserial primary key,
  ts timestamptz not null default now(),
  account_no varchar(32) not null,
  type varchar(8) not null check (type in ('DEBIT','CREDIT')),
  amount numeric(18,2) not null check (amount>=0),
  currency varchar(8) not null default 'KRW',
  memo text
);
create index if not exists ix_journal_account_ts on journal_entries(account_no, ts);

create table if not exists transactions (
  txn_id bigserial primary key,
  ts timestamptz not null default now(),
  account_no varchar(32) not null,
  direction varchar(8) not null check (direction in ('IN','OUT')),
  amount numeric(18,2) not null check (amount>=0),
  balance_after numeric(18,2) not null,
  ref varchar(64),
  note text
);
create index if not exists ix_txn_account_ts on transactions(account_no, ts);

create table if not exists balances (
  account_no varchar(32) primary key,
  balance numeric(18,2) not null default 0
);
