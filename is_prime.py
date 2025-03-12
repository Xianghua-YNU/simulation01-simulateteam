
def is_prime(n):
    """
    检验一个数是否是质数
    
    参数:
    n (int): 需要检验的整数
    
    返回:
    bool: 如果n是质数返回True，否则返回False
    """
    # 处理特殊情况
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # 使用6k±1优化的试除法
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True

