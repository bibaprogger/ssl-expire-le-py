#!/usr/bin/env python3
import os
from datetime import datetime, timedelta


LE_CERTS_PATH = '/etc/letsencrypt/live'


def list_domains():
    domains = []
    for file in os.listdir(LE_CERTS_PATH):
        fullname = os.path.join(LE_CERTS_PATH, file)
        if os.path.isdir(fullname):
            domains.append(file)
    return domains


def main():
    print(list_domains())


if __name__ == '__main__':
    main()
