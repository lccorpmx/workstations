import graphene
from graphene_django import DjangoObjectType

from .models import workstationuser


class WsType(DjangoObjectType):
    class Meta:
        model = workstationuser


class Query(graphene.ObjectType):
    pcs = graphene.List(WsType)

    def resolve_pcs(self, info, **kwargs):
        return workstationuser.objects.all()
    


# ...code
#1
class CreateWS(graphene.Mutation):
    cpu = graphene.String()
    gpu = graphene.String()
    ram = graphene.String()
    mobo = graphene.String()
    psu = graphene.String()
    data = graphene.String()
    gabo = graphene.String()
    monitor = graphene.String()
    teclado = graphene.String()
    mouse = graphene.String()

    #2
    class Arguments:
        cpu = graphene.String()
        gpu = graphene.String()
        ram = graphene.String()
        mobo = graphene.String()
        psu = graphene.String()
        data = graphene.String()
        gabo = graphene.String()
        monitor = graphene.String()
        teclado = graphene.String()
        mouse = graphene.String()

    #3
    def mutate(self, info, cpu, gpu, ram, mobo, psu, data, gabo, monitor, teclado, mouse):
        ws = workstationuser(cpu=cpu, gpu=gpu, ram=ram, mobo=mobo, psu=psu, data=data, gabo=gabo, monitor=monitor, teclado=teclado, mouse=mouse)
        ws.save()

        return CreateWS(
            cpu=ws.cpu,
            gpu=ws.gpu,
            ram=ws.ram,
            mobo=ws.mobo,
            psu=ws.psu,
            data=ws.data,
            gabo=ws.gabo,
            monitor=ws.monitor,
            teclado=ws.monitor,
            mouse=ws.mouse,
        )


#4
class Mutation(graphene.ObjectType):
    create_ws = CreateWS.Field()



schema = graphene.Schema(query=Query, mutation=Mutation)

#hola