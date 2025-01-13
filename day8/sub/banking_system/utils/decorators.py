from typing import Callable

def validate_transaction(func: Callable) -> Callable:
    """
    거래 금액이 유효한지 확인하는 데코레이터.

    Args:
        func (Callable): 데코레이터로 감쌀 함수.

    Returns:
        Callable: 거래 금액을 검증한 후 실행되는 함수.
    """
    def wrapper(*args, **kwargs):
        amount = args[1]  # 첫 번째 인자는 self, 두 번째 인자가 금액.
        if amount <= 0:
            raise ValueError("거래 금액은 0보다 커야 합니다.")
        return func(*args, **kwargs)
    return wrapper
