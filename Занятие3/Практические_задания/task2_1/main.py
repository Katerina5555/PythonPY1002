def pow_func(base, pow_=2):
    # base ** pow_ -> реализовать через цикл while
    result = 1
    while int(pow_) != 0:
        if pow_ < 0:
            result /= base
            pow_ += 1
        elif pow_ > 0:
            result *= base
            pow_ -= 1
    return result
if __name__ == "__main__":
    a = 5
    n = 2

    print(pow_func(a, n))
