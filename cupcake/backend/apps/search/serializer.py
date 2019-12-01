from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    """Serializer for model Person."""

    class Meta(object):
        model = Person
        fields = (
            "document",
            "first_surname",
            "last_surname",
            "name",
            "date_birth",
            "ubigeo",
            "ubigeo_name",
            "address",
            "gender",
            "status_civil",
            "mother_name",
            "father_name"
        )
