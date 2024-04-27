# Используем официальный образ Python
FROM python:3.8

# Устанавливаем рабочую директорию в /app
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Копируем все файлы в рабочую директорию
COPY . .

# Команда для запуска приложения
CMD ["python", "main.py"]
