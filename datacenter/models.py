"""Models."""
from django.db import models
from django.utils import timezone


class Passcard(models.Model):
    """Passcard class."""

    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)  # noqa: WPS432
    owner_name = models.CharField(max_length=255)  # noqa: WPS432

    def __str__(self):
        """Return text for humans."""
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'

    class Meta:  # noqa: WPS306
        """Sorting."""

        ordering = ('owner_name',)


class Visit(models.Model):
    """Visit class."""

    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        """Return text for humans."""
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=f'leaved at {str(self.leaved_at)}' if self.leaved_at else 'not leaved',
        )

    def get_duration(self):
        """
        Calculate the difference between entering and exiting the store.

        :return: total_seconds
        """
        entered_at = timezone.localtime(self.entered_at)
        if self.leaved_at:
            leaved_at = timezone.localtime(self.leaved_at)
        else:
            leaved_at = timezone.localtime()
        delta = leaved_at - entered_at
        return delta.total_seconds()

    def is_visit_long(self, minutes=60):
        """
        If a visit longer than 60 minutes returns true.

        :param minutes:
        :return:
        """
        duration = self.get_duration()
        duration_minutes = duration // 60
        return duration_minutes >= minutes


def format_duration(duration):
    """
    Format total seconds in HH:MM:SS.

    :param duration:
    :return:
    """
    sec_on_hour = 3600
    hour = str(int(duration // sec_on_hour))
    minutes = str(int(duration % sec_on_hour // 60))
    seconds = str(int(duration % sec_on_hour % 60))
    return f'{hour.zfill(2)}:{minutes.zfill(2)}:{seconds.zfill(2)}'  # noqa: WPS221
