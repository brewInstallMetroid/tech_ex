# the front end shouldn't know about database tables, so thin wrappers are here
# in the BL.  Also all the other business logic is there
from django.http     import JsonResponse

from ..da.CustomerDA import CustomerDA
from ..da.ItemDA     import ItemDA

class FindersBL:

    @staticmethod
    def searchForCustomer(request):
        custNum = request.GET.get("customer_number","").strip()
        customer = CustomerDA.getCustByNum(custNum)
        if customer is None:
            return JsonResponse({
                    "found": False
                })
        return JsonResponse({
                "found": True,
                "name": customer.name
            })
        
    @staticmethod
    def searchForItem(request):
        itemNum = request.GET.get("item_number","").strip()
        item = ItemDA.getItemByNum(itemNum)
        if item is None:
            return JsonResponse({
                    "found": False
                })
        return JsonResponse({
                "found": True,
                "name": item.description
            })

    @staticmethod
    def createInvoice(custNum,custName,items,memo,total):
        return InvoiceDAO.create_invoice(customer_number,
                                         customer_name,
                                         items,
                                         memo,
                                         total)
