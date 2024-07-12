import sys
import math

def read_circle(file_path):
    try:
        with open(file_path, 'r') as file:
            # Читаем первую строку для координат x и y
            line1 = file.readline().strip()
            x, y = map(float, line1.split())

            # Читаем вторую строку для радиуса R
            line2 = file.readline().strip()
            R = float(line2)

            return x, y, R
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        sys.exit(1)
    except ValueError:
        print("Ошибка формата данных в файле.")
        sys.exit(1)
    return None

def read_coordinates(file_path):
    coordinates = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                x, y = map(float, line.split())
                coordinates.append((x, y))
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        sys.exit(1)
    except ValueError:
        print("Ошибка формата данных в файле.")
        sys.exit(1)
    return coordinates

def cheak_dot(x,y,R, x_dot, y_dot):
    epsilon = 1e-9
    destination = (x-x_dot)**2 + (y-y_dot)**2
    R_sq = R**2
    if math.isclose(R_sq, destination, rel_tol=epsilon):
        return 0
    elif destination < R_sq:
        return 1
    else:
        return 2


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("python script.py <путь_к_файлу> <путь_к_файлу>")
        sys.exit(1)

    file_path_circle = sys.argv[1]
    file_path_dot = sys.argv[2]
    x, y, R = read_circle(file_path_circle)
    coords = read_coordinates(file_path_dot)
    #print(x,y, R)
    for dot in coords:
        print(cheak_dot(x, y, R, dot[0], dot[1]))