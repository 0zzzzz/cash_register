from rest_framework import serializers
from mainapp.models import Item


class ItemSerializer(serializers.ModelSerializer):
    """Cериализатор для товаров"""
    class Meta:
        model = Item
        fields = '__all__'

    def create(self, validated_data):
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance
