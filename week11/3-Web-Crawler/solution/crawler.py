from datetime import datetime
import time
from urllib.parse import urljoin

import tldextract
import requests
from bs4 import BeautifulSoup


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from settings import DB_CONNECTION_STRING

from models import Domain, Link


engine = create_engine(DB_CONNECTION_STRING)
Session = sessionmaker(bind=engine)
session = Session()


def is_url(url):
    return tldextract.extract(url).registered_domain != ''


def save(obj):
    session.add(obj)
    session.commit()


def main():
    unvisted_links = session.query(Link)\
            .filter(Link.visited_at == None)\
            .all()

    if len(unvisted_links) == 0:
        print('Nothing to visit right now')

    for link in unvisted_links:
        try:
            print('Trying to visit: {}'.format(link))
            r = requests.get(link)
            soup = BeautifulSoup(r.text, 'html.parser')

            for site_url in set([o.get('href') for o in soup.find_all('a')]):
                if site_url is None:
                    continue

                url = site_url

                if not is_url(site_url):
                    url = urljoin(link.get_domain(),
                                  site_url)

                print('Found: {}'.format(url))

                l = session.query(Link)\
                           .filter(Link.url == url).first()

                if l is not None:
                    continue

                l = Link(url=url)
                domain = l.get_domain()

                domain_in_db = session.query(Domain)\
                                      .filter(Domain.url == domain)\
                                      .first()

                if domain_in_db is None:
                    print('Found new domain: {}'.format(domain))
                    domain_in_db = Domain(url=domain)
                    save(domain_in_db)

                l.domain = domain_in_db
                print('ABOUT TO SAVE')
                save(l)
        except Exception as e:
            print(e.__class__)
            print(e)
            print(e.__dir__)
            print('Something went wrong')
        finally:
            link.visited_at = datetime.now()
            save(link)

if __name__ == '__main__':
    while True:
        main()
        time.sleep(3)
