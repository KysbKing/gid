import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Проверяем и устанавливаем библиотеку gdown
try:
    import gdown
except ImportError:
    install('gdown')
    import gdown

# Идентификатор файла на Google Диске
file_id = '11RQp0S8SPa_9KtMOtXFrUvFKmre_mTb-'
# Создаем ссылку для скачивания
url = f'https://drive.google.com/uc?id={file_id}'

# Имя файла, под которым вы хотите сохранить скачанный файл
output = 'downloaded_file.ext'  # Замените расширение на нужное, если известно

# Скачиваем файл
gdown.download(url, output, quiet=False)

print(f"Файл сохранен как {output}")