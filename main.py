import pickle

from account import Account

# map = {
#     "key": "value"
# }
# map['아이디'] = Account("아이디")
# value = map['key']
#
# if '아이디' in map:
#     print("키가 있습니다.")
#
# a = []
# b = {}

if __name__ == '__main__':
    try:
        with open("account", "rb") as f:
            account_table = pickle.load(f)

    except FileNotFoundError:
        account_table = {}

    # void main() 이랑 같은 의미 시작점
    print("Pair Bank")
    # 출력
    # 로그인 회원가입 종료..
    current_account = None
    flag = True

    while flag:
        # 로그인 서비스
        while current_account is None:
            print("==== 메뉴 ====")
            print("1. 로그인")
            print("2. 회원가입")
            print("3. 종료")
            choice = input("입력 : ")
            if choice == "1":
                print("=== 로그인 ===")
                username = input("ID : ")
                if username not in account_table:
                    print("존재하지 않는 아이디입니다.")
                    continue

                current_account = account_table[username]

            if choice == "2":
                print("=== 회원가입 ===")
                username = input("ID : ")
                username = username.replace(" ", "")
                if len(username) <= 0:
                    print("아이디를 입력해주세요.")
                    continue

                current_account = Account(username)
                account_table[username] = current_account

                print(f"ID : {current_account.user_name}")
                # Account 함수에 이름저장
                print(f"계좌번호 : {current_account.account_number}")
                # uuid4 로 계좌 번호 출력
                print(f"잔액 : {current_account.balance}")
                # 잔액조회
            if choice == "3":
                print("종료합니다.")
                flag = False
                break

        # 뱅킹 서비스
        while current_account is not None:
            # 반복문
            print("--- 메뉴 ---")
            print("1. 입금")
            print("2. 출금")
            print("3. 잔액 조회")
            print("4. 이체")
            print("5. 로그아웃")
            choice = input("입력 : ")
            if choice == "1":
                current_account.deposit()

            elif choice == "2":
                current_account.withdraw()

            elif choice == "3":
                print(f"현재 잔액: {current_account.balance}")

            elif choice == "4":
                # 이체 시 필요한 데이터
                # 1. 보낼 상대의 정보 (계좌번호 or 아이디)
                # 1-1. 존재하는 아이디 or 계좌번호인지 확인
                # 2. 이체할 금액
                # 2-1. 단 이체할 금액은 내 잔액보다 작아야함
                print("이체할 아이디를 적으시오.")
                username = input("ID : ")
                if username not in account_table:
                    print("존재하지 않는 아이디 입니다.")
                    continue

                other_user = account_table[username]
                amount = current_account.withdraw()
                other_user.deposit(amount)

            elif choice == "5":
                print("로그아웃 합니다.")
                current_account = None
                break
                # 종료

    with open("account", "wb") as f:
        pickle.dump(account_table, f)
