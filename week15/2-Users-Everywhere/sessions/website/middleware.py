class SetUserInRequestMiddleware:
    def process_request(self, request):
        print('Hooked in middleware')
        print(request.session.items())

        request.hook = 'hooked'
