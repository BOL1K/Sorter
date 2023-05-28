import os
import shutil


def sort_files_in_folder(folder_path):
    # Папка, в которую будут перемещаться отсортированные файлы
    destination_folder = folder_path
  
    # Создаем словарь с расширениями файлов и соответствующими папками
    file_formats = {
        'Изображения': ['.jpg', '.jpeg', '.png', '.gif'],
        'Документы': ['.doc', '.docx', '.txt', '.pdf'],
        'Видео': ['.mp4', '.avi', '.mov'],
        'Музыка': ['.mp3', '.wav', '.flac'],
        'Архивы': ['.zip', '.rar'],
        'Программирование': ['.py'],
        'Прочие': []  # Здесь можно указать расширения, которые не входят в основные категории
    }

    # Перебираем все файлы в исходной папке
    for file_name in os.listdir(destination_folder):
        file_path = os.path.join(destination_folder, file_name)

        # Пропускаем папки и специальные файлы (например, .DS_Store для macOS)
        if os.path.isdir(file_path) or file_name.startswith('.'):
            continue

        # Получаем расширение файла
        file_extension = os.path.splitext(file_name)[1].lower()

        # Ищем соответствующую папку для данного расширения
        for folder, extensions in file_formats.items():
            if file_extension in extensions:
                destination_path = os.path.join(destination_folder, folder)
                break
        else:
            # Если расширение не найдено в основных категориях, перемещаем файл в папку "Прочие"
            destination_path = os.path.join(destination_folder, 'Прочие')

        # Создаем папку назначения, если она не существует
        os.makedirs(destination_path, exist_ok=True)

        # Перемещаем файл в папку назначения
        shutil.move(file_path, os.path.join(destination_path, file_name))

    print('Сортировка завершена.')


# Получаем путь к папке от пользователя
folder_path = input('Введите путь к папке, которую нужно отсортировать и очистить: ')

# Вызываем функцию для сортировки и очистки файлов
sort_files_in_folder(folder_path)
