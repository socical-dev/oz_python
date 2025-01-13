class UserNotFoundError(Exception):
    def __init__(self, username: str) -> None:
        """
        사용자 검색 실패 예외.

        Args:
            username (str): 찾으려는 사용자 이름.
        """
        super().__init__(f"사용자 '{username}'를 찾을 수 없습니다.")

class InsufficientFundsError(Exception):
    def __init__(self, balance: int) -> None:
        """
        잔고 부족 예외.

        Args:
            balance (int): 현재 잔고.
        """
        super().__init__(f"잔고가 부족합니다. 현재 잔고: {balance}원.")

class NegativeAmountError(Exception):
    def __init__(self) -> None:
        """
        음수 금액 예외.
        """
        super().__init__("거래 금액은 음수가 될 수 없습니다.")
