@api_view(['RENT-CAR'])
def order_car(customerId, carId):
    try:
        theCustomer = Customer.objects.get(pk=customerId)
        theCar = Car.objects.get(pk=carId)
    except Customer.DoesNotExist and Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)    
    serializer = CustomerSerializer(theCustomer, data=request.data)
    if serializer.is_valid():
        if theCar.status == "booked":
            theCar.status = "rented"
        else:
            return "car not booked"
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)