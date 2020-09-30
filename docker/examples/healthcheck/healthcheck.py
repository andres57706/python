import os
import sys
_HEALTHY_FILE_PATH = os.getenv('HEALTHY_FILE_PATH', '/tmp/healthy')

if __name__ == "__main__":
    with open(_HEALTHY_FILE_PATH, 'r') as f:
        status = f.read()
        if status.lower().strip() == 'bad':
            sys.exit(f'healt status: {status}')
        else:
            sys.exit()
