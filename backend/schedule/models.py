from django.core import exceptions
from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils import Choices
from model_utils.models import TimeFramedModel, TimeStampedModel

from conferences.models import Conference, Topic
from submissions.models import Submission


class ScheduleItem(TimeFramedModel, TimeStampedModel):
    TYPES = Choices(
        ('submission', _('Submission')),
        ('custom', _('Custom')),
    )

    conference = models.ForeignKey(
        Conference,
        on_delete=models.CASCADE,
        verbose_name=_('conference'),
        related_name='schedule_items'
    )

    title = models.CharField(_('title'), max_length=100, blank=True)
    description = models.TextField(_('description'), blank=True)

    type = models.CharField(
        choices=TYPES,
        max_length=10,
        verbose_name=_('type')
    )

    topic = models.ForeignKey(
        Topic,
        on_delete=models.PROTECT,
        verbose_name=_('topic')
    )

    submission = models.ForeignKey(
        Submission,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name=_('submission')
    )

    def clean(self):
        if self.type == ScheduleItem.TYPES.submission and not self.submission:
            raise exceptions.ValidationError(
                {'submission': _("You have to specify a submission when using the type `submission`")}
            )

        if self.type == ScheduleItem.TYPES.custom and not self.title:
            raise exceptions.ValidationError(
                {'title': _("You have to specify a title when using the type `custom`")}
            )

    def __str__(self):
        title = self.submission.title if self.type == ScheduleItem.TYPES.submission else self.title
        return f'{self.conference.name}. Start: {self.start} End: {self.end}. {title}'

    class Meta:
        verbose_name = _('Schedule item')
        verbose_name_plural = _('Schedule items')