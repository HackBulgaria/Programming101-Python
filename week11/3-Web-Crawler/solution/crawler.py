from datetime import datetime
import time
from urllib.parse import urljoin

import tldextract
import requests
from bs4 import BeautifulSoup


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, asc

from settings import DB_CONNECTION_STRING

from models import Domain, Link

from helpers import domain_exists, is_url, get_domain, save


engine = create_engine(DB_CONNECTION_STRING)
Session = sessionmaker(bind=engine)
session = Session()


def main():
    link = session.query(Link)\
            .filter(Link.visited_at == None)\
            .order_by(asc(Link.id))\
            .first()

    if link is None:
        print('Nothing to visit right now')

    try:
        print('Trying to visit: {}'.format(link))

        r = requests.get(link, timeout=5)
        soup = BeautifulSoup(r.text, 'html.parser')

        domain_on_redirect = get_domain(r.url)

        if not domain_exists(session, domain_on_redirect):
            print('Found new domain: {}'.format(domain_on_redirect))
            save(session, Domain(url=domain_on_redirect))
            print('Saved that new domain.')

        for site_url in set([o.get('href') for o in soup.find_all('a')]):

            if site_url is None:
                continue

            url = site_url

            if not is_url(site_url):
                url = urljoin(get_domain(link.url),
                              site_url)

            print('Found: {}'.format(url))

            l = session.query(Link)\
                       .filter(Link.url == url).first()

            if l is not None:
                continue

            l = Link(url=url)
            domain = get_domain(l.url)

            domain_in_db = session.query(Domain)\
                                  .filter(Domain.url == domain)\
                                  .first()

            if domain_in_db is None:
                print('Found new domain: {}'.format(domain))
                domain_in_db = Domain(url=domain)
                save(session, domain_in_db)

            l.domain = domain_in_db
            save(session, l)
    except Exception as e:
        print('Something went wrong')
        print(e)
    finally:
        link.visited_at = datetime.now()
        save(session, link)

if __name__ == '__main__':
    while True:
        main()
        time.sleep(3)
