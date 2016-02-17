from datetime import datetime
import time

from models import Domain
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from settings import DB_CONNECTION_STRING

import requests

engine = create_engine(DB_CONNECTION_STRING)
Session = sessionmaker(bind=engine)
session = Session()


def save(obj):
    session.add(obj)
    session.commit()


while True:
    domains_to_visit = session.query(Domain)\
            .filter(Domain.server == None,
                    Domain.visited_at == None)\
            .all()

    if len(domains_to_visit) == 0:
        print('Nothing to visit right now, sleeping')

    for domain in domains_to_visit:
        print('Trying to visit: {}'.format(domain))

        try:
            r = requests.head(domain, allow_redirects=True)

            if 'Server' in r.headers:
                domain.server = r.headers['Server']

        except Exception:
            print('Visiting {} failed'.format(domain))
        finally:
            domain.visited_at = datetime.now()
            save(domain)
            print('Saved: {}'.format(domain.server))

    time.sleep(1)
