from services.banking_service import BankingService

def main() -> None:
    """
    메인 함수를 실행하여 온라인 뱅킹 시스템을 시작합니다.

    - 사용자를 추가하거나 찾을 수 있습니다.
    - 각 사용자별로 입금, 출금, 잔고 확인, 거래 내역 기능을 제공합니다.
    """
    banking_service = BankingService()

    while True:
        print("\n=== 온라인 뱅킹 시스템 ===")
        print("1. 사용자 추가")
        print("2. 사용자 찾기")
        print("3. 종료")
        choice = input("옵션을 선택하세요: ")

        if choice == "1":
            username = input("추가할 사용자 이름을 입력하세요: ")
            banking_service.add_user(username)
            print(f"사용자 '{username}'이(가) 추가되었습니다.")
        elif choice == "2":
            username = input("찾을 사용자 이름을 입력하세요: ")
            try:
                banking_service.user_menu(username)
            except Exception as e:
                print(f"오류: {e}")
        elif choice == "3":
            print("온라인 뱅킹 시스템을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")

# 메인 함수 실행
if __name__ == "__main__":
    main()
