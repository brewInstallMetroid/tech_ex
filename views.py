from django.shortcuts import render
import json

# business logic layer - communicates with data access layer
from .bl.FindersBL import FindersBL

# Create your views here.
def credit_memo(request):
    context = {"credit_items": [],
               "total_credit": "0.00",}
    return render(request, "credit_memo.html", context,)

def search_customer(request):
    #static method that gives JSON response for customer, None if not found
    return(FindersBL.searchForCustomer(request))

def search_item(request):
    #static method that gives JSON response for item, None if not found
    return(FindersBL.searchForItem(request))

def create_invoice(request):
    if request.method != "POST":
        return JsonResponse({
            "success": False
        })

    try:
        data = json.loads(request.body)

        invoice = FinderBL.create_invoice(
            data["customer_number"],
            data["customer_name"],
            data["items"],
            data["memo"],
            data["total"]
        )

        return JsonResponse({
            "success": True,
            "invoice_id": invoice.id
        })

    except Exception:
        return JsonResponse({
            "success": False
        })
