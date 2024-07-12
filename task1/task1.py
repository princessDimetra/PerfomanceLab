import sys

def find_next(n, m, k):
    return (m + k - 2) % n + 1

def find_array(n, m):
    array = []
    k =1
    while True:
        array.append(k)
        k = find_next(n, m , k)
        if k == 1:
            break
    return array

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <number1> <number2>")
        return
    try:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
    except ValueError:
        print("Both arguments must be numbers.")
        return
    array = find_array(n, m)
    result = ''.join(str(num) for num in array)
    print(result)



if __name__ == "__main__":
    main()