import sys
import redis
from uuid import uuid4

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
_MAX_LIMIT = 10000


def data_generator(qty: int):
    print('inserting data...')
    for i in range(1, qty):
        r.set(i, str(uuid4()))
    print('data inserted !!!!')


def fetch_iter(filter_: str = '*', limit: int = 10, offset: int = 0):

    if limit > _MAX_LIMIT:
        print(f'we cannot fetch over {_MAX_LIMIT} records! :(')
        return
    if offset < 0:
        print('offset param must be a positive integer')
        return

    print(
        f'scanning over keys applying filter: "{filter_}" fetching ~ {limit} records')
    idx = 0
    for k in r.scan_iter(filter_, limit):
        if k is None:
            pass

        if idx >= limit:
            break

        if offset > 0:
            offset -= 1
            continue

        d = r.get(k)
        print(f'index: {idx + 1} | key: {k} | data: {d}')
        idx += 1


def fetch(filter_: str = '*', limit: int = 10, offset: int = 0):

    if limit > _MAX_LIMIT:
        print(f'we cannot fetch over {_MAX_LIMIT} records! :(')
        return
    if offset < 0:
        print('offset param must be a positive integer')
        return

    print(
        f'scanning over keys applying filter: "{filter_}" fetching ~ {limit} records')
    idx = 0
    cursor = '0'
    while cursor != 0:
        cursor, keys = r.scan(cursor=int(cursor), match=filter_, count=limit)
        # process batch
        for k in keys:
            if k is None:
                continue

            if idx >= limit:
                break

            if offset > 0:
                offset -= 1
                continue

            d = r.get(k)
            print(f'index: {idx + 1} | key: {k} | data: {d}')
            idx += 1
        if idx >= limit:    
            break

_USAGE = '''
REDIS TEST TOOL

Usage:

\tpython3 scan.py [COMMAND]

Commands:

\tgen [qty] 

\tfetch [filter] [limit] [offset]

Examples:

\tgen: --> python3 scan.py gen 50  

\t(this command will generate and store 50 keys SET type in redis)

\tfetch: python3 scan.py fetch * 50 0 

\t(this command will fetch all keys data stored in redis, searching by filter pattern.\n\t\t\tThe limit param will indicate a quantity of records to fetch,\n\t\t\toffset param is used to move around the records cursor. \n\t\t\tEvery param is optional)
'''

if __name__ == "__main__":

    args = sys.argv[1:]

    if len(args) < 1:
        print(_USAGE)
    else:
        if args[0] == 'gen':
            data_generator(int(args[1]))
        elif args[0] == 'fetch':
            if len(args) == 2:
                fetch(args[1])
            elif len(args) == 3:
                fetch(args[1], int(args[2]))
            elif len(args) == 4:
                fetch(args[1], int(args[2]), int(args[3]))
            else:
                print(_USAGE)
