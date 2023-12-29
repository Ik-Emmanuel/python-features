from dataclasses import dataclass, field
from decimal import Decimal
import random
import string
from typing import Iterator

@dataclass
class Account:
    name: str
    number: str
    balance: Decimal = Decimal("0")

    def deposit(self, amount: Decimal) -> None:
        self.balance += amount

    def withdraw(self, amount: Decimal) -> None:
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

@dataclass
class Bank:
    accounts: dict[str, Account] = field(default_factory=dict)

    def __len__(self) -> int:
        return len(self.accounts)

    def __getitem__(self, account_number: str) -> Account:
        return self.accounts[account_number]

    def __iter__(self) -> Iterator[Account]:
        return iter(self.accounts.values())

    def create_account(self, name: str) -> Account:
        number = "".join(random.choices(string.digits, k=12))
        account = Account(name, number)
        self.accounts[number] = account
        return account

    def get_account(self, account_number: str) -> Account:
        return self.accounts[account_number]