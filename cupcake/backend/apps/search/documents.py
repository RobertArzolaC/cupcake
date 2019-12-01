from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Person


@registry.register_document
class PersonDocument(Document):
    class Index:
        name = 'person'
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    class Django:
        model = Person

        fields = [
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
        ]
