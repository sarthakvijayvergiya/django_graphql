import graphene
from graphene_django import DjangoObjectType

from django.contrib.auth import get_user_model



class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class Query(graphene.ObjectType):
    user = graphene.Field(UserType, id=graphene.Int(required=True))
    me = graphene.Field(UserType)
    getUser = graphene.List(UserType)

    def resolve_getUser(self,info,**kwargs):
        return get_user_model().objects.all()
    def resolve_user(self, info, id):
        return get_user_model().objects.get(id=id)

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            # raise GraphQLError('Not logged in!')
            raise Exception('Not logged in!')

        return user


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = get_user_model()(
            username=username,
            email=email
        )
        user.set_password(password)
        user.save()
        return CreateUser(user=user)

    
class DeleteUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)

    def mutate(self, info, username):
        user = get_user_model().objects.get(username=username)
        user.delete()
        return DeleteUser(user=user)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    delete_user = DeleteUser.Field()