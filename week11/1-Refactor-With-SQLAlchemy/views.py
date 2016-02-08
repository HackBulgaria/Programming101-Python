from controllers import ClientAlreadyRegistered


class MainView:
    def __init__(self, controller):
        self.controller = controller

    def render(self):
        while True:
            command = input('Enter command>')

            if command == 'register':
                email = input('Email:')
                password = input('Password:')

                try:
                    self.controller.register(email, password)
                    print('Success!')
                except ClientAlreadyRegistered as e:
                    print(e)
