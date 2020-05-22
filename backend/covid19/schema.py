import graphene

from graphene_django.types import DjangoObjectType

from .models import Countdown


class CountdownType(DjangoObjectType):
    class Meta:
        model = Countdown


class CountdownCreateInput(graphene.InputObjectType):
    target = graphene.String(required=True)
    target_date = graphene.DateTime(required=True)


class CountdownDeleteInput(graphene.InputObjectType):
    id = graphene.Int()


class Query(graphene.ObjectType):
    all_countdowns = graphene.List(CountdownType)

    def resolve_all_countdowns(self, info):
        return Countdown.objects.order_by("target_date").all()


class CreateCountdown(graphene.Mutation):
    id = graphene.Int()

    class Arguments:
        countdown_data = CountdownCreateInput(required=True)

    def mutate(root, info, countdown_data):
        countdown = Countdown(
            target=countdown_data.target, target_date=countdown_data.target_date
        )
        countdown.save()

        return CreateCountdown(id=countdown.id)


class DeleteCountdown(graphene.Mutation):
    is_delete = graphene.Boolean()

    class Arguments:
        countdown_data = CountdownDeleteInput(required=True)

    def mutate(root, info, countdown_data):
        countdown = Countdown.objects.get(id=countdown_data.id)
        countdown.delete()
        return DeleteCountdown(is_delete=True)


class Mutation(graphene.ObjectType):
    create_countdown = CreateCountdown.Field()
    delete_countdown = DeleteCountdown.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
