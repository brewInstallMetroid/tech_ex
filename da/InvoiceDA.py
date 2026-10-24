```python
from decimal import Decimal
from ..models import Invoice


class InvoiceDA:
    # exists basically just to create an invoice record at the end of 
    # the workflow
    def add_item(self, item_number, description):
        item = {
            "item_number": item_number,
            "description": description
        }
        self.items.append(item)
        return item

    def get_items(self):
        return self.items

    def create_invoice(self,
                       customer_number,
                       customer_name,
                       memo,
                       total):
        invoice = Invoice.objects.create(
            customer_number=customer_number,
            customer_name=customer_name,
            items=self.items,
            memo=memo,
            total=Decimal(total))

        return invoice
