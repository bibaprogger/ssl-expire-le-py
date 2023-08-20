#!/usr/bin/env python3
import os
import OpenSSL
import datetime
import requests


LE_CERTS_PATH = '/etc/letsencrypt/live/'
CERT = 'cert.pem'
THRESHOLD = 7


def list_domains() -> list:
    domains = []
    for file in os.listdir(LE_CERTS_PATH):
        fullname = os.path.join(LE_CERTS_PATH, file)
        if os.path.isdir(fullname):
            domains.append(file)
    return domains


def cert_days_left(domain: str) -> int:
    certfilepath = LE_CERTS_PATH + domain + '/' + CERT
    with open(certfilepath, "r") as certfile:
        cert_data = certfile.read()
        x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert_data)
    x509info = x509.get_notAfter()
    cert_expires_dt = datetime.datetime.strptime(x509info.decode('ascii'), '%Y%m%d%H%M%SZ')
    days_left = (cert_expires_dt - datetime.datetime.now()).days

    return days_left


def telegram_send_alert(domain: str, days_left: int) -> None:
    TOKEN = 'token'
    CHAT_ID = '-00000000'
    message = f'ATTENTION! SSL for domain {domain} expire after {days_left} days'
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}'
    requests.get(url)


def main() -> None:
    domains = list_domains()
    for d in domains:
        days_left = cert_days_left(d)
        if days_left <= THRESHOLD:
            telegram_send_alert(days_left)


if __name__ == '__main__':
    main()
