# plarin_testtask
Тестовое задание компании plarin

## Задача
Реализовать веб-приложение которое предоставляет один API метод для получения
списка определенных сотрудников. Приложение должно быть реализовано с
использованием FastAPI и MongoDB.
Список данных прикреплен в json файле.
Плюсом будет использование Docker, покрытие тестами.

## Запуск
0. Переменные окружение  
CONTRIB_MONGODB_DSN - Путь к mongodb, пример  
`mongodb://mongoadmin:secret@db:27017`
MONGO_INITDB_ROOT_USERNAME - Имя пользователя mongodb указывается так же в CONTRIB_MONGODB_DSN
MONGO_INITDB_ROOT_PASSWORD - Пароль пользователя mongodb указывается так же в CONTRIB_MONGODB_DSN
0. Запуск docker compose  
`docker-compose up`

## Путь к документации
`http://localhost/docs`
