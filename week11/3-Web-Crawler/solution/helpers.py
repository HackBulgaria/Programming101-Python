from models import Domain

import tldextract
from urllib.parse import urlparse


def save(session, obj):
    session.add(obj)
    session.commit()


def domain_exists(session, domain):
    d = session.query(Domain).filter(Domain.url == domain).first()

    return d is not None


def is_url(url):
    return tldextract.extract(url).registered_domain != ''


def get_domain(url):
    url_parts = urlparse(url)
    scheme = url_parts.scheme

    if scheme == '':
        scheme = 'http'

    domain = tldextract.extract(url).registered_domain

    return "{}://{}".format(scheme, domain)
