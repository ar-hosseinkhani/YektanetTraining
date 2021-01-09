from Advertiser import Advertiser
from Ad import Ad
class BaseAdvertising:
    def __init__(self, id=-1):
        self.__id = id
        self.__clicks = 0
        self.__views = 0

    def inc_views(self):
        self.__views += 1

    def inc_clicks(self):
        self.__clicks += 1

    def get_clicks(self):
        return self.__clicks

    def get_views(self):
        return self.__views

    @staticmethod
    def describe_me():
        return "I am BaseAdvertising class :)"


baseAdvertising = BaseAdvertising()
advertiser1 = Advertiser(1, 'name1')
advertiser2 = Advertiser(2, 'name2')
ad1 = Ad(1, 'title1', 'image-url1', 'link1', advertiser1)
ad2 = Ad(2, 'title2', 'image-url2', 'link2', advertiser2)
print(baseAdvertising.describe_me())
ad2.describe_me()
advertiser1.describe_me()
ad1.inc_views()
ad1.inc_views()
ad1.inc_views()
ad1.inc_views()
ad2.inc_views()
ad1.inc_clicks()
ad1.inc_clicks()
ad2.inc_clicks()
print(advertiser2.get_name())
advertiser2.set_name('new name')
print(advertiser2.get_name())
print(ad1.get_clicks())
print(advertiser2.get_clicks())
print(Advertiser.get_total_clicks())
print(Advertiser.help())