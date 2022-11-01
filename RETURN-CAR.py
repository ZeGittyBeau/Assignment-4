#Implement an endpoint ‘return-car’ where a customer-id, car-id is passed as parameters.
#Car’s status (e.g., ok or damaged) during the return will also be passed. The system must
#check that the customer with customer-id has rented the car. The car’s status is changed
#from ‘booked’ to ‘available’ or ‘damaged’
@api_view(['RETURN-CAR'])
def order_car(customerId, carId):
    car_stat = ['ok', 'rented', 'damaged']
    try:
        
        theCustomer = Customer.objects.get(pk=customerId)
        theCar = Car.objects.get(pk=carId)
    except Customer.DoesNotExist and Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)    
    serializer = CustomerSerializer(theCustomer, data=request.data)
    if serializer.is_valid():
        rStatus = random.choice(car_stat)
        theCar.status = rStatus
        if theCar.status == 'ok':
            theCar.status = "available"
        elif theCar.status == 'rented':
            theCar.status = "available"
        else:
            return "car not rented"
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)