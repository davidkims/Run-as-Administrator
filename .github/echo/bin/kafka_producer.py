import os, json, random
from datetime import datetime, timedelta
from kafka import KafkaProducer
ROWS=int(os.getenv("ROWS","2000"))
producer=KafkaProducer(bootstrap_servers="localhost:9092", value_serializer=lambda v: json.dumps(v, default=str).encode())
accts=[f"V{str(i).zfill(6)}" for i in range(1, 50+int(os.getenv("EXTRA","150"))+1)]
base=datetime.utcnow()-timedelta(days=3)
for i in range(ROWS):
  msg={
    "ts": (base+timedelta(seconds=i*(3*24*3600/ROWS))).isoformat(),
    "account_no": random.choice(accts),
    "direction": random.choice(["IN","OUT"]),
    "amount": round(random.uniform(10, 500000),2),
    "ref": f"KAFKA{i}"
  }
  producer.send("transactions", msg)
  if i%500==0: producer.flush()
producer.flush()
