from models import Client


class ClientAlreadyRegistered(Exception):
    pass


class MainController:
    def register(self, email, password):
        user = self.session.query(Client).\
                filter(Client.email == email).first()

        if user is not None:
            raise ClientAlreadyRegistered('Client already registered')

        client = Client(email=email, password=password)
        self.__commit_object(client)

    def __commit(self):
        self.session.commit()

    def __commit_object(self, obj):
        self.session.add(obj)
        self.__commit()

    def __commit_objects(self, objects):
        self.session.add_all(objects)
        self.__commit()

    def __init__(self, session):
        self.session = session
