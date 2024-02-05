from uuid import uuid4


class Account:
    # Account 라는 객체 생성

    def __init__(self, user_name):
        # 함수
        self.user_name = user_name
        # 이름
        self.account_number = str(uuid4())
        # 계좌 번호
        self.balance = 0
        # 잔액

    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        self.balance -= money
