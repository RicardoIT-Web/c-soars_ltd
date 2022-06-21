from django.shortcuts import render, redirect


def view_briefcase(request):
    """ View to render briefcase page to show services booked"""

    return render(request, 'briefcase/briefcase.html')

def add_to_briefcase(request, item_id):
    """ add qty of specified service to briefcase """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    briefcase = request.session.get('briefcase', {})

    if item_id in list(briefcase.keys()):
        briefcase[item_id] += quantity
    else:
        briefcase[item_id] = quantity

    request.session['briefcase'] = briefcase
    print(request.session['briefcase'])
    return redirect(redirect_url)
