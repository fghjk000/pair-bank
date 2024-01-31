from uuid import uuid4
# uuid에 uuid4를 꺼내온다.


class Account:
    # Account 라는 객체 생성

    def __init__(self, name):
        # 함수
        self.name = name
        # 이름
        self.account_number = str(uuid4())
        # 계좌 번호
        self.balance = 0
        # 잔액


if __name__ == '__main__':
    # void main() 이랑 같은 의미 시작점
    print("Pair Bank")
    #출력

    current_account = None
    #현재 잔액

    while True:
    #반복문
        print("--- 메뉴 ---")
        print("1. 계좌 계설")
        print("2. 입금")
        print("3. 출금")
        print("4. 잔액 조회")
        print("5. 이체")
        print("6. 종료")
        choice = input("입력 : ")
        # if문 선택
        if choice == "1":
            print("=== 계좌 계설 ===")
            name = input("이름 : ")
            current_account = Account(name)
            #Account 함수에 이름저장
            print(f"계좌번호: {current_account.account_number}")
            #uuid4 로 계좌 번호 출력
            print(f"잔액: {current_account.balance}")
            #잔액조회
        elif choice == "2":
            print("=== 입금 ===")
            try:
            #시도해서 맞으면 실행
                amount = int(input("입금액 : "))
            except ValueError:
            # 다른 벨류이면 >> 숫자가아닌 문자 입력시
                print("숫자를 입력해주세요.")
                continue

            if amount <= 0:
                #음수 입력시
                print("0보다 큰 금액을 입력해주세요.")
                continue

            current_account.balance += amount
            # amount 금액 입력값을 balance 더하라
            print(f"잔액: {current_account.balance}")
            # 저장된 잔액 조회

        elif choice == "6":
            print("종료합니다.")
            break
        #종료