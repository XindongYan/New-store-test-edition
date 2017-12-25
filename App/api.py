from .models import User, Store, Thing, Mac
from django.http import HttpResponseRedirect

# 序列化器，把数据包装成类似字典的格式
from rest_framework import serializers

# 这两个模块把序列化后的数据包装成api
from rest_framework.response import Response
from rest_framework.decorators import api_view


# 创建一个 Store 的序列化器
class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


class ThingSer(serializers.ModelSerializer):
    class Meta:
        model = Thing
        fields = '__all__'


class MacSer(serializers.ModelSerializer):
    class Meta:
        model = Mac
        fields = '__all__'


@api_view(['GET'])
def store(request):
    store_list = Store.objects.all()
    ser = StoreSerializer(store_list, many=True)
    return Response(ser.data)


@api_view(['GET'])
def thing(request):
    thing_list = Thing.objects.all()
    ser = ThingSer(thing_list, many=True)
    return Response(ser.data)


@api_view(['GET'])
def mac(request):
    mac_list = Mac.objects.all()
    ser = MacSer(mac_list, many=True)
    return Response(ser.data)
