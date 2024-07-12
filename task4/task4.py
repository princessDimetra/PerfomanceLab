import sys

def read_numbers_from_file(filename):
    """Читает массив целых чисел из файла."""
    try:
        with open(filename, 'r') as file:
            numbers = list(map(int, file.read().split()))
        return numbers
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден.")
        sys.exit(1)
    except ValueError:
        print(f"Ошибка: файл '{filename}' содержит некорректные данные.")
        sys.exit(1)

def ps_median(numbers):
    temp = len(numbers)//2
    return numbers[temp]

def calculate_muvs(numbers, median):
    count = 0
    for number in numbers:
        count = count + abs(number-median)
    return count

def main():
    if len(sys.argv) != 2:
        print("python script.py <путь_к_файлу>")
        sys.exit(1)
    filename = sys.argv[1]
    numbers = read_numbers_from_file(filename)
    #print("Считанный массив чисел:", numbers)
    numbers.sort()
    #print("New", numbers)
    median = ps_median(numbers)
    #print("Median:", median)
    count = calculate_muvs(numbers, median)
    print(count)


if __name__ == "__main__":
    main()
