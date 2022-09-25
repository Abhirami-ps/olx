from django.shortcuts import render

# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Vehicles,Reviews
from api.serializers import VehicleSerializer,ReviewSerializer
from rest_framework.viewsets import ViewSet,ModelViewSet


class ProductsView(APIView):

    def get(self,request,*args,**kwargs):
        qs=Vehicles.objects.all()
        serializer=VehicleSerializer(qs,many=True)

        return Response(data=serializer.data)



    # def post(self,request,*args,**kwargs):
    #     vname=request.data.get("name")
    #     vmodel=request.data.get("model")
    #     vcolor=request.data.get("color")
    #     vprice=request.data.get("price")
    #     vtransmission=request.data.get("transmission")
    #     Vehicles.objects.create(name=vname,model=vmodel,color=vcolor,price=vprice,transmission=vtransmission)
    #     return Response(data="Created")



    def post(self,request,*args,**kwargs):
        serializer=VehicleSerializer(data=request.data)
        if serializer.is_valid():
            Vehicles.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.data)






class ProductDetailsView(APIView):

    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        vehicle=Vehicles.objects.get(id=id)
        serializer=VehicleSerializer(vehicle,many=False)
        return Response(data=serializer.data)


    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Vehicles.objects.get(id=id).delete()
        return Response(data="Deleted")

    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        serializer=VehicleSerializer(data=request.data)
        if serializer.is_valid():
            Vehicles.objects.filter(id=id).update(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)






class ReviewsView(APIView):

    def get(self,request,*args,**kwargs):
        reviews=Reviews.objects.all()
        serilaizer=ReviewSerializer(reviews,many=True)
        return Response(data=serilaizer.data)



    def post(self,request,*args,**kwargs):
        serializer=ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)





class ReviewDetailsView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Reviews.objects.get(id=id)
        serializer=ReviewSerializer(qs,many=False)
        return Response(data=serializer.data)

    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        object=Reviews.objects.get(id=id)
        serializer=ReviewSerializer(instance=object,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)



    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Reviews.objects.get(id=id).delete()
        return Response(data="deleted")





class ProductsViewsetView(ViewSet):

    def list(self,request,*args,**kwargs):
        qs=Vehicles.objects.all()
        serializer=VehicleSerializer(qs,many=True)
        return Response(data=serializer.data)


    def create(self,request,*args,**kwargs):
        serializer=VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)




    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        vehicle=Vehicles.objects.get(id=id)
        serializer=VehicleSerializer(vehicle,many=False)
        return Response(data=serializer.data)



    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        vehicle=Vehicles.objects.filter(id=id)
        serializer=VehicleSerializer(instance=vehicle,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)




    def delete(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Reviews.objects.get(id=id).delete()
        return Response(data="deleted")





class ProductModelViewsetView(ModelViewSet):
    serializer_class = VehicleSerializer
    queryset = Vehicles.objects.all()



class ReviewModelViewsetView(ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Reviews.objects.all()

    def list(self,request,*args,**kwargs):
        all_reviews=Reviews.objects.all()
        if 'user' in request.query_params:
            all_reviews=all_reviews.filter(user=request.query_params.get("user"))
        serializer=ReviewSerializer(all_reviews,many=True)
        return Response(data=serializer.data)












