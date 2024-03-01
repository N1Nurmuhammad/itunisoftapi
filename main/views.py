from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response

from main.serializers import *


@swagger_auto_schema(method="get", tags=["api"])
@api_view(['GET', ])
def get_about_us_view(request):
    abouts = AboutUsModel.objects.all()
    serializer = AboutUsModelSerializer(abouts, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method="get", tags=["api"])
@api_view(['GET', ])
def get_products_view(request):
    products = ProductsModel.objects.all()
    serializer = ProductsModelSerializer(products, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method="get", tags=["api"])
@api_view(['GET', ])
def get_services_view(request):
    services = ServiceModel.objects.all()
    serializer = ServiceModelSerializer(services, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method="get", tags=["api"])
@api_view(['GET', ])
def get_docs_view(request):
    docs = DocumentsModel.objects.all()
    serializer = DocumentsModelSerializer(docs, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method="get", tags=["api"])
@api_view(['GET', ])
def get_contacts_view(request):
    contacts = ContactsModel.objects.all()
    serializer = ContactsModelSerializer(contacts, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method="get", tags=["api"])
@api_view(['GET', ])
def get_partners_view(request):
    out_partners = OurPartnersModel.objects.all()
    serializer = OurPartnersModelSerializer(out_partners, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method="get", tags=["api"])
@api_view(['GET', ])
def get_statistics_view(request):
    statistics = OurStatisticsModel.objects.all()
    serializer = OurStatisticsModelSerializer(statistics, many=True)
    return Response(serializer.data)
