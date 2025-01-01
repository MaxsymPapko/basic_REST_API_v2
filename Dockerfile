# Вибір образу Python
FROM python:3.9

# Встановлення робочої директорії
WORKDIR /app

# Копіювання файлів проекту в контейнер
COPY requirements.txt .

# Встановлення залежностей
RUN pip install -r requirements.txt

# Копіювання всіх файлів проекту в контейнер
COPY . .

# Вказуємо порт, на якому працює Flask
EXPOSE 5000

# Команда для запуску Flask
CMD ["flask", "run", "--host=0.0.0.0"]
