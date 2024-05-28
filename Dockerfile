# Используем образ с Python
FROM python:3

# Устанавливаем рабочую директорию 
WORKDIR /app

# Копируем исходный код в контейнер
COPY calorie_intake.py /app/calorie_intake.py

# Запускаем приложение при старте контейнера
CMD ["python", "/app/calorie_intake.py"]
