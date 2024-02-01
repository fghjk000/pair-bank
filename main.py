from uuid import uuid4
# uuid에 uuid4를 꺼내온다.


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
        current_account.balance += amount

        print(f"잔액: {current_account.balance}")

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

        elif current_account.balance < amount:
            print("잔액보다 큰 금액은 출금하실수 없습니다.")
            return

        current_account.balance -= amount
        print(f"잔액: {current_account.balance}")

if __name__ == '__main__':
    # void main() 이랑 같은 의미 시작점
    print("Pair Bank")
    # 출력
    # 로그인 회원가입 종료..
    current_account = None

    # 로그인 서비스
    while current_account is None:
        print("==== 메뉴 ====")
        print("1. 로그인")
        print("2. 회원가입")
        print("3. 종료")
        choice = input("입력 : ")
        if choice == "1":
            ...
        if choice == "2":
            print("=== 회원가입 ===")
            username = input("ID : ")
            username = username.replace(" ", "")
            if len(username) <= 0:
                print("아이디를 입력해주세요.")
                continue

            current_account = Account(username)

            print(f"ID : {current_account.user_name}")
            # Account 함수에 이름저장
            print(f"계좌번호 : {current_account.account_number}")
            # uuid4 로 계좌 번호 출력
            print(f"잔액 : {current_account.balance}")
            # 잔액조회
        if choice == "3":
            print("종료합니다.")
            break

    # 뱅킹 서비스
    while current_account is not None:
        # 반복문
        print("--- 메뉴 ---")
        print("1. 입금")
        print("2. 출금")
        print("3. 잔액 조회")
        print("4. 이체")
        print("5. 종료")
        choice = input("입력 : ")
        if choice == "1":
            current_account.deposit()

        elif choice == "2":
            current_account.withdraw()

        elif choice == "3":
            print(f"현재 잔액: {current_account.balance}")

        elif choice == "4":
            ...

        elif choice == "5":
            print("종료합니다.")
            break
            # 종료
