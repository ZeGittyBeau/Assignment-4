
@api_view(['ORDER-CAR'])
def order_car(request, customerId, carId):
    try:
        theCustomer = Customer.objects.get(pk=customerId)
        theCar = Car.objects.get(pk=carId)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CustomerSerializer(theCustomer, data=request.data)
    if carId.status = "booked":
        print ("order found")
        if serializer.is_valid():
            carId.status = "available"
            serializer.save()
        else:
            Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return "car is available"