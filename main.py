from uuid import uuid4


class Account:
    def __init__(self, name):
        self.name = name
        self.account_number = str(uuid4())
        self.balance = 0


if __name__ == '__main__':
    print("Pair Bank")

    current_account = None

    while True:
        print("--- 메뉴 ---")
        print("1. 계좌 계설")
        print("2. 입금")
        print("3. 출금")
        print("4. 잔액 조회")
        print("5. 이체")
        print("6. 종료")
        choice = input("입력 : ")

        if choice == "1":
            print("=== 계좌 계설 ===")
            name = input("이름 : ")
            current_account = Account(name)

            print(f"계좌번호: {current_account.account_number}")
            print(f"잔액: {current_account.balance}")

        elif choice == "2":
            print("=== 입금 ===")
            try:
                amount = int(input("입금액 : "))
            except ValueError:
                print("숫자를 입력해주세요.")
                continue

            if amount <= 0:
                print("0보다 큰 금액을 입력해주세요.")
                continue

            current_account.balance += amount
            print(f"잔액: {current_account.balance}")

        elif choice == "6":
            print("종료합니다.")
            break
