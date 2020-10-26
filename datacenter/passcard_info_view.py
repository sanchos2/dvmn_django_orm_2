"""Passcard info view."""
from django.shortcuts import Http404, render

from datacenter.models import Passcard, Visit, format_duration


def passcard_info_view(request, passcode):  # noqa: WPS210
    """
    View function to render passcard_info.html template.

    :param request:
    :param passcode: the number of pass card
    :return: rendered template
    """
    try:
        passcard = Passcard.objects.get(passcode=passcode)
    except Passcard.DoesNotExist:
        raise Http404('Passcode not found')

    this_passcard_visits = []
    visits = Visit.objects.filter(passcard=passcard)

    for visit in visits:
        duration = visit.get_duration()
        formated_duration = format_duration(duration)
        this_passcard_visits.append(
            {
                'entered_at': visit.entered_at,
                'duration': formated_duration,
                'is_strange': visit.is_visit_long(),
            },
        )
    context = {
        'passcard': passcard.owner_name,
        'this_passcard_visits': this_passcard_visits,
    }
    return render(request, 'passcard_info.html', context)
