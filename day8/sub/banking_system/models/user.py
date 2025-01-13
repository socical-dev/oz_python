"""
1) User 클래스 구현
2) username 과 account 를 추기화 하는 생성자 구현
3) username은 문자열 / account : 는 Account 객체
"""

from account import Account

class User:    
    def __init__(self, username: str) -> None:
        self.username = username
        self.account = Account()
    