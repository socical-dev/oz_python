"""
1) Transaction(거래) 클래스 생성
2) transaction_type(거래 유형 문자열 ex: "입금", "출금) 생성자 구현
3) amount(거래 금액) 생성자 구현
4) balance (잔고) 생성자 구현
3) to_tuple 메서드 구현 : 거래 정보를 튜플로 반환하는 메서드
"""

class Transaction:
    def __init__(self, transaction_type: str, amount:int, balance: int) -> None:
        """
        거래 정보를 초기화 합니다.
        
        - transaction_type:str => 거래 유형 (예: "입금", "출금")
        - amount:int => 거래 금액
        - balance:int => 거래 후 잔고
        """
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance = balance
        
    def __str__(self) -> str:
        return f"{self.transaction_type}: {self.amount} | Balance: {self.balance}"

    def to_tuple(self) -> tuple:
        return (self.transaction_type, self.amount, self.balance)