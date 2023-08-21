from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from . import models


def get_data(amount, req, outer_model, outer_serializer):
    match(amount):
        case 'singular':
            model = outer_model

            serialized_model = outer_serializer(model)

            serialized_model_data = serialized_model.data

            return Response(serialized_model_data, status=status.HTTP_200_OK)

        case 'plural':
            model = outer_model

            serialized_model = outer_serializer(model, many=True)

            serialized_model_data = serialized_model.data

            return Response(serialized_model_data, status=status.HTTP_200_OK)

        case _:
            return Response({"msg": "Something went wrong!"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def auto(req, auto_id):
    if req.method == "GET":
        return get_data(
            'singular',
            req,
            models.Auto.objects.get(id=auto_id),
            serializers.SerializedAuto
        )

    if req.method == "PUT":
        old_model = models.Auto.objects.get(id=auto_id)

        updated_item = serializers.SerializedAuto(
            old_model, data=req.data, partial=False)

        updated_item.is_valid(raise_exception=True)
        updated_item.save()

        return Response(serializers.SerializedAuto(models.Auto.objects.all(), many=True).data)

    if req.method == "DELETE":
        old_model = models.Auto.objects.get(id=auto_id)

        old_model.delete()

        return Response(serializers.SerializedAuto(models.Auto.objects.all(), many=True).data)

    if req.method == "POST":
        models.Auto.objects.create(**req.data)

        return Response(serializers.SerializedAuto(models.Auto.objects.all(), many=True).data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def autos(req):
    if req.method == "GET":
        return get_data(
            'plural',
            req,
            models.Auto.objects.all(),
            serializers.SerializedAuto
        )

    if req.method == "PUT":
        old_model = models.Auto.objects.get()

        updated_item = serializers.SerializedAuto(
            old_model, data=req.data, partial=False)

        updated_item.is_valid(raise_exception=True)
        updated_item.save()

        return Response(serializers.SerializedAuto(models.Auto.objects.all(), many=True).data)

    if req.method == "DELETE":
        old_model = models.Auto.objects.all()

        old_model.delete()

        return Response(serializers.SerializedAuto(models.Auto.objects.all(), many=True).data)

    if req.method == "POST":
        models.Auto.objects.create(**req.data)

        return Response(serializers.SerializedAuto(models.Auto.objects.all(), many=True).data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def owner(req, owner_id):
    if req.method == "GET":
        return get_data(
            'singular',
            req,
            models.Owner.objects.get(id=owner_id),
            serializers.SerializedOwner,

        )

    if req.method == "PUT":
        old_model = models.Owner.objects.get(id=owner_id)

        updated_item = serializers.SerializedOwner(
            old_model, data=req.data, partial=False)

        updated_item.is_valid(raise_exception=True)
        updated_item.save()

        return Response(serializers.SerializedOwner(models.Owner.objects.all(), many=True).data)

    if req.method == "DELETE":
        old_model = models.Owner.objects.get(id=owner_id)

        old_model.delete()

        return Response(serializers.SerializedOwner(models.Owner.objects.all(), many=True).data)

    if req.method == "POST":
        models.Owner.objects.create(**req.data)

        return Response(serializers.SerializedOwner(models.Owner.objects.all(), many=True).data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def owners(req):
    if req.method == "GET":
        return get_data(
            'plural',
            req,
            models.Owner.objects.all(),
            serializers.SerializedOwner,

        )

    if req.method == "PUT":
        old_model = models.Owner.objects.all()

        updated_item = serializers.SerializedOwner(
            old_model, data=req.data, partial=False)

        updated_item.is_valid(raise_exception=True)
        updated_item.save()

        return Response(serializers.SerializedOwner(models.Owner.objects.all(), many=True).data)

    if req.method == "DELETE":
        old_model = models.Owner.objects.all()

        old_model.delete()

        return Response(serializers.SerializedOwner(models.Owner.objects.all(), many=True).data)

    if req.method == "POST":
        models.Owner.objects.create(**req.data)

        return Response(serializers.SerializedOwner(models.Owner.objects.all(), many=True).data)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def auto_passport(req, auto_passport_id):
    if req.method == "GET":
        return get_data(
            'singular',
            req,
            models.Auto_Passport.objects.get(id=auto_passport_id),
            serializers.SerializedAuto_Passport
        )

    if req.method == "PUT":
        old_model = models.Auto_Passport.objects.get(id=auto_passport_id)

        updated_item = serializers.SerializedAuto_Passport(
            old_model, data=req.data, partial=False)

        updated_item.is_valid(raise_exception=True)
        updated_item.save()

        return Response(serializers.SerializedAuto_Passport(models.Auto_Passport.objects.all(), many=True).data)

    if req.method == "DELETE":
        old_model = models.Auto_Passport.objects.get(id=auto_passport_id)

        old_model.delete()

        return Response(serializers.SerializedAuto_Passport(models.Auto_Passport.objects.all(), many=True).data)

    if req.method == "POST":
        models.Auto_Passport.objects.create(**req.data)

        return Response(serializers.SerializedAuto_Passport(models.Auto_Passport.objects.all(), many=True).data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def auto_passports(req):
    if req.method == "GET":
        return get_data(
            'plural',
            req,
            models.Auto_Passport.objects.all(),
            serializers.SerializedAuto_Passport
        )

    if req.method == "PUT":
        old_model = models.Auto_Passport.objects.get()

        updated_item = serializers.SerializedAuto_Passport(
            old_model, data=req.data, partial=False)

        updated_item.is_valid(raise_exception=True)
        updated_item.save()

        return Response(serializers.SerializedAuto_Passport(models.Auto_Passport.objects.all(), many=True).data)

    if req.method == "DELETE":
        old_model = models.Auto_Passport.objects.all()

        old_model.delete()

        return Response(serializers.SerializedAuto_Passport(models.Auto_Passport.objects.all(), many=True).data)

    if req.method == "POST":
        models.Auto_Passport.objects.create(**req.data)

        return Response(serializers.SerializedAuto_Passport(models.Auto_Passport.objects.all(), many=True).data)
