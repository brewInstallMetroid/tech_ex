from ..models import Customer

class CustomerDA:
    @staticmethod
    def getCustByNum(custNum):
        try:
            return Customer.objects.get(customer_number=custNum)
        except Customer.DoesNotExist:
            return None
