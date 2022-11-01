@api_view(['ORDER-CAR'])
def order_car(request, customerId, carId):
    try:
        theCustomer = Customer.objects.get(pk=customerId)
        theCar = Car.objects.get(pk=carId)
    except Customer.DoesNotExist and Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)    
    serializer = CustomerSerializer(theCustomer, data=request.data)
    if serializer.is_valid():
        if Car.status == "available":
            Car.status = "booked"
        else:
            return "car unavailable"
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)