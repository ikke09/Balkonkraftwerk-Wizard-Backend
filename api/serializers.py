from rest_framework import serializers
from api.viewmodels import BalconyViewModel
from drf_extra_fields.fields import Base64ImageField


class BalconySerializer(serializers.ModelSerializer):
    img = Base64ImageField(required=True)

    class Meta:
        model = BalconyViewModel
        fields = ('img', 'uri', 'height', 'width')

    def create(self, validated_data):
        img = validated_data.pop('img')
        uri = validated_data.pop('uri')
        height = validated_data.pop('height')
        width = validated_data.pop('width')
        return BalconyViewModel.objects.create(img=img, uri=uri, height=height, width=width)
