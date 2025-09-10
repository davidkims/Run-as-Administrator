import os, random, csv
from datetime import datetime, timedelta
import psycopg2
import matplotlib.pyplot as plt

ROWS=int(os.getenv("ROWS","2000"))
PGHOST=os.getenv("PGHOST","127.0.0.1")
PGUSER=os.getenv("PGUSER","finops")
PGPASSWORD=os.getenv("PGPASSWORD","finops")
PGDB=os.getenv("PGDB","finops")

accts=[]
conn=psycopg2.connect(host=PGHOST,user=PGUSER,password=PGPASSWORD,dbname=PGDB)
cur=conn.cursor()
cur.execute("select account_no from accounts order by account_no;")
for r in cur.fetchall(): accts.append(r[0])

base=datetime.utcnow()-timedelta(days=10)
rows=[]
for i in range(ROWS):
  acc=random.choice(accts)
  ts=base+timedelta(seconds=i*(10*24*3600/ROWS))
  direction=random.choice(["IN","OUT"])
  amount=round(random.uniform(10, 800000),2)

  cur.execute("select balance from balances where account_no=%s",(acc,))
  bal=cur.fetchone()
  bal=float(bal[0]) if bal else 0.0
  new_bal=bal+amount if direction=="IN" else max(0.0, bal-amount)

  cur.execute("""insert into transactions(account_no,direction,amount,balance_after,ref,note,ts)
                 values(%s,%s,%s,%s,%s,%s,%s)""",
              (acc,direction,amount,new_bal,f"REF{i}","sim",ts))
  jtype="DEBIT" if direction=="IN" else "CREDIT"
  cur.execute("""insert into journal_entries(account_no,type,amount,ts,memo)
                 values(%s,%s,%s,%s,%s)""",(acc,jtype,amount,ts,"sim"))
  cur.execute("""insert into balances(account_no,balance)
                 values(%s,%s)
                 on conflict (account_no) do update set balance=excluded.balance""",(acc,new_bal))

  rows.append((ts,acc,direction,amount,new_bal))
  if i%500==0: conn.commit()
conn.commit()

os.makedirs("site/reports",exist_ok=True)
with open("site/reports/transactions.csv","w",newline="",encoding="utf-8") as f:
  w=csv.writer(f); w.writerow(["ts","account_no","direction","amount","balance_after"]); w.writerows(rows)

# Charts
cur.execute("select d,revenue,expense,profit from v_income_statement order by d;")
data=cur.fetchall()
d=[r[0] for r in data]; rev=[float(r[1]) for r in data]; exp=[float(r[2]) for r in data]; prof=[float(r[3]) for r in data]
plt.figure(); plt.plot(d,rev,label="Revenue"); plt.plot(d,exp,label="Expense"); plt.plot(d,prof,label="Profit")
plt.legend(); plt.title("Income Statement (Daily)"); plt.xlabel("Date"); plt.ylabel("Amount"); plt.tight_layout()
os.makedirs("site/imgs",exist_ok=True); plt.savefig("site/imgs/income_statement.png")

cur.execute("select total_assets from v_balance_sheet;")
assets=float(cur.fetchone()[0] or 0)
plt.figure(); plt.bar(["Assets"],[assets]); plt.title("Balance Sheet (Assets)"); plt.tight_layout()
plt.savefig("site/imgs/balance_sheet.png")

# TD-Sim Daily Count
cur.execute("select d, txn_cnt from td_sim_daily order by d;")
dd=cur.fetchall()
if dd:
  days=[r[0] for r in dd]; cnt=[int(r[1]) for r in dd]
  plt.figure(); plt.bar(days,cnt); plt.title("TD-Sim Daily Txn Count"); plt.tight_layout()
  plt.savefig("site/imgs/td_sim_daily_txn.png")

cur.close(); conn.close()
