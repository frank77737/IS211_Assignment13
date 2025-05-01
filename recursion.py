# Part 1: Recursive Fibonacci Function
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
# Part 2: Recursive GCD Function
def gcd(a, b):

    if b == 0:
        return a
    else:
        return gcd(b, a % b)
# Part 3: Recursive String Comparison Function
def stringCompare(s1, s2):
    if not s1 and not s2:
        return 0
    if not s1:
        return -1
    if not s2:
        return 1
    if s1[0] < s2[0]:
        return -1
    if s1[0] > s2[0]:
        return 1
    return stringCompare(s1[1:], s2[1:])


def main():
    print("Part One Fibinnaci :")
    print(f"fib of 13 = {fib(13)}")
    print(f"fib of 20  = {fib(20)}")

    print("\nPart Two Greatest Common Divisor:")
    print(f"gcd(48, 18) = {gcd(100, 42)}")
    print(f"gcd(20, 8) = {gcd(200, 24)}")

    print("\nPart 3 String Comparison:")
    print(f"stringCompare('Franklyn', 'Franklyn Collaguazo') = {stringCompare('Franklyn', 'Franklyn Collaguazo')}")
    print(f"stringCompare('franklyn', 'nylknarf') = {stringCompare('franklyn', 'franklyn')}")  

if __name__ == "__main__":
    main()
