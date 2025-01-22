# Mangagraph

#### From Mangalib to Telegraph with ❤️

Асинхронный парсер-конвертер манги из mangalib api в telegraph

## Принцип работы

Даем **ссылку на мангу**
**(такого типа: https://mangalib.me/ru/manga/{slug_url}) и название бд**
куда мы сохраняем _(том, главу, наименование главы, ссылку на главу для чтения и зеркало на случаи_
_если главная ссылка не доступна)_ -> получаем полные данные о главах -> генерируем телеграф страницы
на каждую главу -> ссылки на страницу сохраняем в `SQLite` бд, с использованием `SQLAlchemy`

**-> На выходе**
получаем базу данных готовую к любому использованию и конечную ссылку телеграфа с зеркалом (оглавление) внутри
которой находятся все главы с именами и ссылкой для чтения

## Использование

#### CLI

```bash
mangagraph https://mangalib.me/ru/manga/706--onepunchman?section=chapters&ui=7011590 --db onepunchman.db --mirror --log manga_parser.log
```

#### Raw

```py
from mangagraph.parser import Mangagraph
from mangagraph.exceptions import MangagraphError

async def main():
    try:
        parser = Mangagraph(db_name='ванпанчмен', use_mirror=True)
        toc_url, mirror_toc_url = await parser.process_manga('https://mangalib.me/ru/manga/706--onepunchman')
        print(f"Table of Contents: {toc_url}")
        print(f"Mirror: {mirror_toc_url}")
    except MangagraphError as e:
        print(f"Parser error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

import asyncio

asyncio.run(main())
```
