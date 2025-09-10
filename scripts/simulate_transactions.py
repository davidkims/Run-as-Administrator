import json
import random
from typing import List, Dict


def simulate_transactions(accounts: List[str], num: int = 10) -> List[Dict[str, float]]:
    transactions = []
    for _ in range(num):
        account = random.choice(accounts)
        amount = round(random.uniform(10, 1000), 2)
        t_type = random.choice(["DEPOSIT", "WITHDRAWAL"])
        transactions.append({"account": account, "type": t_type, "amount": amount})
    return transactions


def main() -> None:
    accounts = ["1001", "1002", "1003"]
    txns = simulate_transactions(accounts, 20)
    with open("transactions.json", "w", encoding="utf-8") as f:
        json.dump(txns, f, indent=2)


if __name__ == "__main__":
    main()
