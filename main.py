import pickle
# pickle 사용
from account import Account
# account 에 Account를 불러들임

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
    #함수를 시작하는부분
    try:
        #시도하기
        with open("account", "rb") as f:
            # 서비스가 종료되었어다가 다시켯을떄 전에 파일을 불러오는 역할
            account_table = pickle.load(f)
            #pickle을 사용하여 account를 account_table에 불러오기

    except FileNotFoundError:
        #시도하고 실패시
        account_table = {}
        #account_table 딕셔너리생성

    # void main() 이랑 같은 의미 시작점
    print("Pair Bank")
    # pair bank출력
    current_account = None
    # current_account를 None으로 설정
    flag = True
    # while문 실행을 위해 true설정
    while flag:
    # 반복문 실행
        # 로그인 서비스
        while current_account is None:
            # current_account를 None일때 실행
            print("==== 메뉴 ====")
            # 메뉴 출력
            print("1. 로그인")
            # 로그인 출력
            print("2. 회원가입")
            # 회원가입 출력
            print("3. 종료")
            # 종료 출력
            choice = input("입력 : ")
            # if문을 받기위해 input으로 choice값 설정
            if choice == "1":
                #choice 1번 입력설정시 실행
                print("=== 로그인 ===")
                # 로그인 출력
                username = input("ID : ")
                # username 을 input 으로 설정
                if username not in account_table:
                    # 입력한 username이 account_table에 없을시 실행
                    print("존재하지 않는 아이디입니다.")
                    # 문구 출력
                    continue
                    # 가까운 반복문으로 돌아가기

                current_account = account_table[username]
                # account_table 안에 username 라는 (붕어빵)을 current_account로 설정

            if choice == "2":
                # choice를 2번으로 설정시 실행
                print("=== 회원가입 ===")
                # 회원가입 출력
                username = input("ID : ")
                # 회원가입할 username 입력
                username = username.replace(" ", "")
                # username 에서 공백 발생시 replace를 사용하여 바꿔준다
                if len(username) <= 0:
                    # 입력한 username에 길이가 0보다 짧으면 (공백이면)실행
                    print("아이디를 입력해주세요.")
                    # 문구 출력
                    continue
                    # 가까운 반복문으로 복귀

                current_account = Account(username)
                # Account에 입력한 username을 current_account로 설정
                account_table[username] = current_account
                # 위에서 설정한 current_account를 account_table 딕셔너리[username]에 저장

                print(f"ID : {current_account.user_name}")
                # current_account 클래스 안에있는 username ID 출력
                print(f"계좌번호 : {current_account.account_number}")
                # current_account 클래스 안에있는  (uuid4를 이용한 계좌) 출력
                print(f"잔액 : {current_account.balance}")
                # 잔액조회
            if choice == "3":
                # choice 3번 출력시 실행
                print("종료합니다.")
                # 종료 출력
                flag = False
                # 반복문 종료를 위해 flag를 False 설정
                break

        # 뱅킹 서비스
        while current_account is not None:
            # current_account 값이 None이 아닌경우 실행
            print("--- 메뉴 ---")
            # 메뉴 출력
            print("1. 입금")
            # 입금 출력
            print("2. 출금")
            # 출금 출력
            print("3. 잔액 조회")
            # 잔액 조회 출력
            print("4. 이체")
            # 이체 출력
            print("5. 로그아웃")
            # 로그아웃 출력
            choice = input("입력 : ")
            # 다음 if 문을 실행하기위해 choice 값 설정
            if choice == "1":
                # choice 값을 1번 설정시 실행
                current_account.deposit()
                # current_account를 deposit(설정해둿던 입금함수사용)

            elif choice == "2":
                # choice 값을 2번으로 설정시 실행
                current_account.withdraw()
                # current_account를 withdraw(설정해둿던 출금함수사용)
            elif choice == "3":
                # choice 값을 3번으로 설정시 실행
                print(f"현재 잔액: {current_account.balance}")
                # 설정한 current_account에 잔액조회
            elif choice == "4":
                # choice 값을 4번으로 설정시 실행

                # 이체 시 필요한 데이터
                # 1. 보낼 상대의 정보 (계좌번호 or 아이디)
                # 1-1. 존재하는 아이디 or 계좌번호인지 확인
                # 2. 이체할 금액
                # 2-1. 단 이체할 금액은 내 잔액보다 작아야함
                print("이체할 아이디를 적으시오.")
                # 문구 출력
                username = input("ID : ")
                # 이체할 username 설정
                if username not in account_table:
                    # if문을 사용하여 account_table에 username이 없을시 실행
                    print("존재하지 않는 아이디 입니다.")
                    # 문구 출력
                    continue
                    # 가까운 반복문으로 복귀
                other_user = account_table[username]
                # 위에서 설정한 accout_table에있는 username이라는 (붕어빵)하나를 other_user라는 변수에 저장
                amount = current_account.withdraw()
                # 기존에 설정되있던 current_account를 withdraw로 출금시킨값을 amount에 저장
                other_user.balance += amount
                # amount에 저장되있는 출금시킨 값을 other_user 라는 input으로 설정한 변수에 balnce값에 축적시킴

            elif choice == "5":
                # choice 5번을 설정시 실행
                print("로그아웃 합니다.")
                # 로그아웃 출력
                current_account = None
                # current_account를 None 으로 설정함으로써 반복문을 초기화 시킴
                break
                # 종료

    with open("account", "wb") as f:
        # 서비스를 종료 하여도 저장할수있게 만들어줌
        pickle.dump(account_table, f)
        # pickle을 사용하여 accoout에 저장시킴
