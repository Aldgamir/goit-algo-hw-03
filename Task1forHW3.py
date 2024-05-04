import os
import shutil
import argparse

def copy_file(source_path, dest_dir):
    filename = os.path.basename(source_path)
    ext = os.path.splitext(filename)[1]

    # Створення піддиректорії для файлів з певним розширенням, якщо такої не існує
    ext_dir = os.path.join(dest_dir, ext[1:])
    if not os.path.exists(ext_dir):
        os.makedirs(ext_dir)

    # Копіювання файлу
    dest_path = os.path.join(ext_dir, filename)
    try:
        shutil.copyfile(source_path, dest_path)
    except Exception as e:
        print(f'Помилка при копіюванні файлу: {e}')

def copy_dir(source_dir, dest_dir):
    for entry in os.scandir(source_dir):
        source_path = os.path.join(source_dir, entry.name)
        if entry.is_dir():
            # Рекурсивно копіюємо підпапки
            copy_dir(source_path, dest_dir)
        elif entry.is_file():
            # Отримуємо розширення файлу
            ext = os.path.splitext(entry.name)[1]
            # Створюємо папку для розширення, якщо вона ще не існує
            ext_dir = os.path.join(dest_dir, ext[1:])
            if not os.path.exists(ext_dir):
                os.makedirs(ext_dir)
            # Копіюємо файл у відповідну папку
            dest_path = os.path.join(ext_dir, entry.name)
            try:
                shutil.copyfile(source_path, dest_path)
            except Exception as e:
                print(f'Помилка при копіюванні файлу: {e}')

def main():
    parser = argparse.ArgumentParser(description='Копіювання файлів з вихідної директорії до директорії призначення за їх розширенням.')
    parser.add_argument('source_dir', metavar='source_directory', type=str, help='Шлях до вихідної директорії.')
    parser.add_argument('dest_dir', metavar='destination_directory', type=str, nargs='?', default='dist', help='Шлях до директорії призначення (за замовчуванням: dist).')
    args = parser.parse_args()

    source_dir = args.source_dir
    dest_dir = args.dest_dir

    # Перевірка існування вихідної директорії
    if not os.path.exists(source_dir):
        print(f'Помилка: директорія "{source_dir}" не існує.')
        exit(1)

    # Створення директорії призначення, якщо вона не існує
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Рекурсивне копіювання файлів
    copy_dir(source_dir, dest_dir)

    print('Файли успішно скопійовано!')

if __name__ == '__main__':
    main()

