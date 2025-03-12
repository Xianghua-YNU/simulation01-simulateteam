def is_prime(n):
    """
    检验一个数是否是质数
    :param n: 要检验的数
    :return: 如果是质数返回True，否则返回False
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
