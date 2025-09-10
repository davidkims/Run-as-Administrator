import json
from typing import List


def create_accounts(count: int = 5) -> List[str]:
    return [f"{1000 + i}" for i in range(count)]


def main() -> None:
    accounts = create_accounts(5)
    with open("accounts.json", "w", encoding="utf-8") as f:
        json.dump(accounts, f, indent=2)


if __name__ == "__main__":
    main()
