from ..models import Item
class ItemDA:
    @staticmethod
    def getItemByNum(itemNum):
        try:
            return Item.objects.get(item_number=itemNum)
        except Item.DoesNotExist:
            return None
