# Case

Нужно разработать рекомендательную систему с 3 моделями:

* которые учитывают видео, просмотренные пользователем за последние 10мин,
* активная выбирается по метрике NDCG каждую неделю по результатам A / B теста

# Solution

[readme.md](./docs/readme.md)

# Generate

1. Установите Java https://www.java.com/ru/
2. Установите https://plantuml.com/ru/starting
3. Сделайте файл `.env` с переменной JAVA_PUML_PATH – путь до `plantuml.jar`
4. Запустите скрипт
```bash
python generate.py
```
    