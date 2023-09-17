# QRkot_spreadseets

# QRKot

### Описание

Проект QRKot — приложение для Благотворительного фонда поддержки котиков.

Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.

### Проекты

В Фонде QRKot может быть открыто несколько целевых проектов. У каждого проекта есть название, описание и сумма, которую планируется собрать. После того, как нужная сумма собрана — проект закрывается.

Пожертвования в проекты поступают по принципу First In, First Out: все пожертвования идут в проект, открытый раньше других; когда этот проект набирает необходимую сумму и закрывается — пожертвования начинают поступать в следующий проект.

### Пожертвования

Каждый пользователь может сделать пожертвование и сопроводить его комментарием. Каждое полученное пожертвование автоматически добавляется в первый открытый проект, который ещё не набрал нужную сумму. Если пожертвование больше нужной суммы или же в Фонде нет открытых проектов — оставшиеся деньги ждут открытия следующего проекта. При создании нового проекта все неинвестированные пожертвования автоматически вкладываются в новый проект.

### Пользователи

Целевые проекты создаются администраторами сайта.

Любой пользователь может видеть список всех проектов.

Зарегистрированные пользователи могут отправлять пожертвования и просматривать список своих пожертвований.

### Отчет

В приложение QRKot есть возможность формирования отчёта в гугл-таблице. В таблице находятся закрытые проекты, отсортированные по скорости сбора средств — от тех, что закрылись быстрее всего, до тех, что долго собирали нужную сумму.

### Установка. Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Alexandra2706/QRkot_spreadsheets.git
```

```
cd QRkot_spreadsheets
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Создать и заполнить файл .env:

```
APP_TITLE=Благотворительный фонд поддержки котиков QRKot
DESCRIPTION=Фонд собирает пожертвования на различные целевые проекты
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=asik
FIRST_SUPERUSER_EMAIL=admin@admin.com
FIRST_SUPERUSER_PASSWORD=admin
EMAIL=<Ваш аккаунт на google>
```

Выполнить миграции:
```
alembic revision --autogenerate -m "First migration"
alembic upgrate head
```
Запустить проект:
```
uvicorn app.main:app --reload
```
Проект будет доступен по адресу: http://127.0.0.1:8000

### Использованные технологии

- Python 3.11
- fastapi 0.78.0
- sqlalchemy 1.4.36
- alembic 1.7.7
- Google API

### Автор

Александра Гаврилова
