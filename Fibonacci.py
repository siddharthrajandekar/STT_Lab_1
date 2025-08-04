#This function calculates the nth fibonacci number
# The nth fibonacci number Fn = Fn-1 + Fn-2
# F1 = 1 and F2 = 1
def fibonacci(n):
    if n <= 0:
        return -1
    if n == 1 or n == 2:
        return 1
    
    first = 1
    second = 1
    ans = 0
    for _ in range(n-2):
        ans = first + second
        first, second = ans, first

    return ans

def main():
    n = int(input("Enter an integer: "))
    fibo = fibonacci(n)
    if fibo == -1:
        print("The integer should be greater than 0")
    else:
        print(fibo)

if __name__ == "__main__":
    main()