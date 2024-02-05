class AccountService:

    @classmethod
    def find_by_username(cls, account_table, username):
        if username in account_table:
            return account_table[username]
        return None

    @classmethod
    def input_deposit(cls):
        try:
            # 시도해서 맞으면 실행
            money = int(input("금액 : "))
        except ValueError:
            # 다른 벨류이면 >> 숫자가아닌 문자 입력시
            print("숫자를 입력해주세요.")
            return
        if money <= 0:
            # 음수 입력시
            print("0보다 큰 금액을 입력해주세요.")
            return

        return money

    @classmethod
    def input_withdraw(cls, balance):
        try:
            # 시도해서 맞으면 실행
            money = int(input("금액 : "))
        except ValueError:
            # 다른 벨류이면 >> 숫자가아닌 문자 입력시
            print("숫자를 입력해주세요.")
            return
        if money <= 0:
            # 음수 입력시
            print("0보다 큰 금액을 입력해주세요.")
            return
        elif balance < money:
            # 잔액보다 큰 금액 입력시
            print("잔액보다 큰 금액은 출금하실수 없습니다.")
            return

        return money
