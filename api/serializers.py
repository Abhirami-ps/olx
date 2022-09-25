from rest_framework import serializers
from api.models import Reviews,Vehicles


class VehicleSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    model=serializers.CharField()
    color=serializers.CharField()
    price=serializers.IntegerField()
    transmission=serializers.CharField()


    def create(self, validated_data):
        return Vehicles.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get("name")
        instance.model=validated_data.get("model")
        instance.color=validated_data.get("color")
        instance.price=validated_data.get("price")
        instance.transmission=validated_data.get("transmission")
        instance.save()
        return instance




    # def validate(self, data):
    #     err_list = []
    #     price = data.get("price")
    #     if price not in range(200000,3500000):
    #         err_list.append(serializers.ValidationError("invalid price"))
    #     if err_list:
    #         raise serializers.ValidationError(err_list)
    #
    #     return data





    def validate_price(self,value):
        if value not in range(200000,3500000):
            raise serializers.ValidationError("invalid price")
        return value





class ReviewSerializer(serializers.ModelSerializer):
    created_date=serializers.CharField(read_only=True)

    class Meta:
        model=Reviews
        fields="__all__"
        # exclude=("created_date",)
        # fields=["vehicle","user","comment","rating"]
