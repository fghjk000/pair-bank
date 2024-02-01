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

    def deposit(self):
        print("=== 입금 ===")  # deposit
        try:
            # 시도해서 맞으면 실행
            amount = int(input("금액 : "))
        except ValueError:
            # 다른 벨류이면 >> 숫자가아닌 문자 입력시
            print("숫자를 입력해주세요.")
            return
        if amount <= 0:
            # 음수 입력시
            print("0보다 큰 금액을 입력해주세요.")
            return
        self.balance += amount

        print(f"잔액: {self.balance}")

    def withdraw(self):
        print("=== 출금 ===")  # withdraw
        try:
            amount = int(input("출금액 : "))
        except ValueError:
            print("숫자를 입력해주세요.")
            return

        if amount <= 0:
            print("0보다 큰 금액을 입력해주세요.")
            return

        elif self.balance < amount:
            print("잔액보다 큰 금액은 출금하실수 없습니다.")
            return

        self.balance -= amount
        print(f"잔액: {self.balance}")
