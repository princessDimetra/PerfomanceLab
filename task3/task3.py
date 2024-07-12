import sys
import json

def find_key_path(data, target_value, current_path=[]):
    if isinstance(data, dict):
        for key, value in data.items():
            new_path = current_path + [key]
            if key == 'id' and value == target_value:
                return new_path
            if isinstance(value, dict):
                result = find_key_path(value, target_value, new_path)
                if result:
                    return result
            elif isinstance(value, list):
                for index, item in enumerate(value):
                    result = find_key_path(item, target_value, new_path + [index])
                    if result:
                        return result
    elif isinstance(data, list):
        for index, item in enumerate(data):
            result = find_key_path(item, target_value, current_path + [index])
            if result:
                return result
    return None


def insert_value_by_path(data, path, value):
    current = data
    for key in path[:-1]:
        if isinstance(key, int) and isinstance(current, list):

            while len(current) <= key:
                current.append({})
            current = current[key]
        else:
            if key not in current:
                current[key] = {}
            current = current[key]
    final_key = path[-1]
    if isinstance(final_key, int) and isinstance(current, list):

        while len(current) <= final_key:
            current.append({})
        current[final_key] = value
    else:
        current[final_key] = value



def read_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Ошибка декодирования JSON в файле {file_path}.")
        sys.exit(1)
    sys.exit(1)


def save_dict_to_json_file(data, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        #print(f"Словарь успешно сохранен в файл: {file_path}")
    except Exception as e:
        print(f"Произошла ошибка при сохранении файла: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Использование: python script.py <путь_к_файлу> <путь_к_файлу> <путь_к_файлу>")
        sys.exit(1)

    file_path_value = sys.argv[1]
    file_path_test = sys.argv[2]
    file_path_report = sys.argv[3]
    data_value = read_json_file(file_path_value)
    data_test = read_json_file(file_path_test)

    data_report = data_test


    for item in data_value['values']:

        id = item['id']
        value = item['value']

        path = find_key_path(data_test, id, [])
        #print(path)
        path[-1] = 'value'
        insert_value_by_path(data_report, path, value)



    save_dict_to_json_file(data_report, file_path_report)
