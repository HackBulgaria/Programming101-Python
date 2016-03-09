from django.shortcuts import render


def home(request):

    if request.method == 'POST':
        if request.POST.get('delete_session', False):
            session_key = request.POST.get('session_key')
            if session_key in request.session:
                del request.session[session_key]
        else:
            session_key = request.POST.get('session_key')
            session_value = request.POST.get('session_value')

            request.session[session_key] = session_value

    return render(request, 'index.html', locals())
