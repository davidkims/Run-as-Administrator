import json, psycopg2
from kafka import KafkaConsumer
consumer=KafkaConsumer("transactions", bootstrap_servers="localhost:9092", value_deserializer=lambda m: json.loads(m.decode()))
conn=psycopg2.connect(host="127.0.0.1", user="finops", password="finops", dbname="finops")
cur=conn.cursor()
for msg in consumer:
  r=msg.value
  acc=r["account_no"]; direction=r["direction"]; amount=float(r["amount"]); ts=r["ts"]
  cur.execute("select balance from balances where account_no=%s",(acc,))
  row=cur.fetchone(); bal=float(row[0]) if row else 0.0
  new_bal=bal+amount if direction=="IN" else max(0.0, bal-amount)
  cur.execute("""insert into transactions(account_no,direction,amount,balance_after,ref,note,ts)
                 values(%s,%s,%s,%s,%s,%s,%s)""",(acc,direction,amount,new_bal,r.get("ref","kafka"),"kafka",ts))
  jtype="DEBIT" if direction=="IN" else "CREDIT"
  cur.execute("""insert into journal_entries(account_no,type,amount,ts,memo)
                 values(%s,%s,%s,%s,%s)""",(acc,jtype,amount,ts,"kafka"))
  cur.execute("""insert into balances(account_no,balance)
                 values(%s,%s)
                 on conflict (account_no) do update set balance=excluded.balance""",(acc,new_bal))
  conn.commit()
