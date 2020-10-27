from django.shortcuts import render

from datacenter.models import Visit, format_duration


def storage_information_view(request):  # noqa: WPS210
    """
    View function to render storage_information.html template.

    :param request:
    :return: rendered template
    """
    non_closed_visits = []
    visits = Visit.objects.filter(leaved_at=None)
    for visitor in visits:
        duration = visitor.get_duration()
        formated_duration = format_duration(duration)
        is_strange = visitor.is_visit_long()
        non_closed_visits.append(
            {
                'who_entered': visitor.passcard,
                'entered_at': visitor.entered_at,
                'duration': formated_duration,
                'is_strange': is_strange,
            },
        )

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
