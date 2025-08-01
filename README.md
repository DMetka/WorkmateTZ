# Обработка лог файла

1. Склонируйте репозиторий:

   ```bash
   git clone https://github.com/username/WorkmateTZ.git
   ```

2. Установите зависимости (рекомендуется использовать виртуальное окружение):

   ```bash
   pip install -r requirements.txt
   ```
3. Запустить скрипт (Пример без даты):
    ```bash
    python main.py --file logs/example1.log logs/example2.log --report average
    ```
4. Запустить скрипт (Пример с датой):
    ```bash
    python main.py --file logs/example1.log logs/example2.log --report average --date 2025-06-22
    ```


# Примеры:
1. Использование без даты:
   <img width="881" height="261" alt="image" src="https://github.com/user-attachments/assets/d5f85639-7705-475f-9d4c-6a48a25bdcc5" />

2. Использование с датой:
   <img width="987" height="203" alt="image" src="https://github.com/user-attachments/assets/b09206e6-4a17-4832-a7be-b07344f4a9a4" />

