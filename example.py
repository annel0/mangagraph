from mangagraph import Mangagraph
from mangagraph.exceptions import MangagraphError

async def main():
    try:
        parser = Mangagraph(db_name='ванпанчмен', use_mirror=True)
        toc_url, mirror_toc_url = await parser.process_manga('https://mangalib.me/ru/manga/5477--blue-lock?from=catalog&ui=7011590')
        print(f"Table of Contents: {toc_url}")
        print(f"Mirror: {mirror_toc_url}")
    except MangagraphError as e:
        print(f"Parser error: {e}")


import asyncio

try:
    asyncio.run(main())
except (KeyboardInterrupt, SystemExit):
    print('Sayonara!')