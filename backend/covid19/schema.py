import graphene

from graphene_django.types import DjangoObjectType

from .models import Countdown


class CountdownType(DjangoObjectType):
    class Meta:
        model = Countdown

class Query(object):
    all_countdowns = graphene.List(CountdownType)

    def resolve_all_countdowns(self, info, **kwargs):
        return Countdown.objects.order_by("target_date").all()
