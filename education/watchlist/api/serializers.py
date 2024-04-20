from rest_framework import serializers
from watchlist.models import movie


class movieserializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=50)
    description=serializers.CharField(max_length=500)
    active=serializers.BooleanField(default=True)

    def create(self,validated_data):
        return  movie.objects.create(**validated_data)
    

    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.description=validated_data.get('description',instance.description)
        instance.active=validated_data.get('active',instance.active)
        instance.save()
        return instance

