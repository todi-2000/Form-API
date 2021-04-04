from rest_framework import serializers
from .models import Client, Weekday

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        exclude = ('client',)

class FormListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

    def to_representation(self, instance):
        rep = super(FormListSerializer, self).to_representation(instance)
        rep['client'] = instance.client.email
        return rep
    

