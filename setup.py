import os
import shutil

KTOOL_DIR = '/usr/share/ktool'
BIN_DIR = '/usr/local/bin'


def install_ktool():
    try:
        print('[+] Removing existing ktool directory at {}...'.format(KTOOL_DIR))
        shutil.rmtree(KTOOL_DIR)
    except FileNotFoundError:
        pass  # If the directory doesn't exist, continue
    except Exception as e:
        print('[-] Error removing existing ktool directory:', e)
        return

    try:
        print('[+] Installing ktool to {}...'.format(KTOOL_DIR))
        shutil.copytree('.', KTOOL_DIR)
    except Exception as e:
        print('[-] Error installing ktool:', e)
        return

    try:
        with open(os.path.join(BIN_DIR, 'ktool'), 'w') as f:
            f.write('#!/bin/sh\n')
            f.write('python3 {} "$@"\n'.format(os.path.join(KTOOL_DIR, 'src', 'ktool.py')))
        os.chmod(os.path.join(BIN_DIR, 'ktool'), 0o755)
    except Exception as e:
        print('[-] Error :', e)
        return

    print('[+] Ktool installed successfully!')

install_ktool()
