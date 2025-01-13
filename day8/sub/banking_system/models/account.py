"""
1) Account 클래스 생성
2) __balance(계좌 잔고) 와 transactions(거래 내역) 리스트를 초기화하는 생성자
3) 출금 withdraw 메서드 구현
4) 잔고 get_balance 메서드 구현
5) 거래 내역 get_transactions 메서드 구현
6) 전역 변수 bank_name(문자열)), 메소드 get_bank_name, set_bank_name 구현
"""

from transaction import Transaction

class Account:
    bank_name = ""
    
    def __init__(self) -> None:
        self.__balance = 0
        self.transactions = list()
        
    # 입금을 위한 메서드
    # 입금 금액이 0 이하인 경우 예외 발생.
    def deposit(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("입금 금액은 0보다 커야 합니다.")
        self.__balance += amount
        self.transactions.append(Transaction("입금", amount, self.__balance))
    
    # 출금을 위한 메서드
    # 출금 금액이 0 이하이거나 잔고보다 높게 출금할 경우
    def withdraw(self, amount:int):
        if amount <= 0:
            raise ValueError("출금 금액은 0보다 커야 합니다.")
        if amount > self.__balance:
            raise ValueError("잔고가 부족합니다.")
        self.__balance -= amount
        self.transactions.append(Transaction("출금", amount, self.__balance))
    
    # 잔고를 반환하는 메서드
    def get_balance(self) -> int:
        return self.__balance

    # 거래 내역 반환하는 메서드
    def get_transactions(self) -> list:
        return self.transactions
    
    # 은행 이름 가져오기
    def get_bank_name(cls) -> str:
        return cls.bank_name
    
    # 은행 이름 저장하기
    def set_bank_name(cls, name:str) -> None:
        cls.bank_name = name