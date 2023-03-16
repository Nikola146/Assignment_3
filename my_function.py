def triangle_type(a, b, c):
    if a <=0 or b <=0 or c <=0 or a >= 200 or b >= 200 or c >=200:
        return "Invalid input."
    if a <= 0 or b <= 0 or c <= 0 or a+b <= c or a+c <= b or b+c <= a:
        return "NotATriangle"
    elif a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"
