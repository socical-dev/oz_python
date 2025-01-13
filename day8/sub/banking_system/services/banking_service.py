from banking_system.models.user import User
from banking_system.utils.exceptions import UserNotFoundError

class BankingService:
    def __init__(self) -> None:
        """
        BankingService를 초기화합니다.
        사용자 목록을 관리합니다.
        """
        self.users = []

    def add_user(self, username: str) -> None:
        """
        새로운 사용자를 추가합니다.

        Args:
            username (str): 추가할 사용자의 이름.
        """
        user = User(username)
        self.users.append(user)

    def find_user(self, username: str) -> User:
        """
        사용자를 검색합니다.

        Args:
            username (str): 찾고자 하는 사용자의 이름.

        Returns:
            User: 해당 이름을 가진 User 객체.

        Raises:
            UserNotFoundError: 사용자가 존재하지 않을 경우 예외 발생.
        """
        for user in self.users:
            if user.username == username:
                return user
        raise UserNotFoundError(f"사용자 '{username}'를 찾을 수 없습니다.")

    def user_menu(self, username: str) -> None:
        """
        사용자 메뉴를 표시하고 사용자의 선택을 처리합니다.

        Args:
            username (str): 메뉴를 사용할 사용자의 이름.
        """
        user = self.find_user(username)
        while True:
            print(f"\n{user.username}님, 환영합니다!")
            print("1. 입금\n2. 출금\n3. 잔고 확인\n4. 거래 내역\n5. 종료")
            choice = input("옵션을 선택하세요: ")
            if choice == "1":
                amount = int(input("입금할 금액을 입력하세요: "))
                user.account.deposit(amount)
                print("입금이 완료되었습니다.")
            elif choice == "2":
                amount = int(input("출금할 금액을 입력하세요: "))
                try:
                    user.account.withdraw(amount)
                    print("출금이 완료되었습니다.")
                except ValueError as e:
                    print(f"오류: {e}")
            elif choice == "3":
                print(f"현재 잔고: {user.account.get_balance()}원")
            elif choice == "4":
                print("거래 내역:")
                for transaction in user.account.get_transactions():
                    print(transaction)
            elif choice == "5":
                print("메뉴를 종료합니다.")
                break
            else:
                print("잘못된 선택입니다. 다시 시도하세요.")