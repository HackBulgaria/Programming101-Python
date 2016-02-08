from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from base import Base
from controllers import MainController
from views import MainView

from settings import DB_CONNECTION_STRING


engine = create_engine(DB_CONNECTION_STRING)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

main_controller = MainController(session)
main_view = MainView(main_controller)

main_view.render()
