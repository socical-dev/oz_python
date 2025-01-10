# 삼각형 넓이 구해주는 함수
def triangle_area(width, height):
    return (width * height) / 2

# 원의 넓이 구해주는 함수
def circle_area(radius):
    return radius * radius * 3.14

# 직윤면체 겉넓이 구하는 함수
def cubiod_suface_area(width, length, height):
    return 2 * (width * length + width * height + length * height)