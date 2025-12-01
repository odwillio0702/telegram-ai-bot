# Берём образ Python 3.11
FROM python:3.11-slim

# Создаём рабочую директорию
WORKDIR /app

# Копируем файл зависимостей и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта
COPY . .

# Команда запуска бота
CMD ["python3", "main.py"]