class BinaryTreeItem:

    def __init__(self, value=0, name=''):
        self.leftItem=None
        self.rightItem=None
        self.value=value
        self.name=name

    def __str__(self):
        return("name: %s, leftItem : %s, rightItem: %s, value: %s"%(self.name, self.leftItem,self.rightItem,self.value))




def bts(item,value):

    if item==None:
        return None

    if item.value==value:
        return item

    if item.value>value:
        return bts(item.leftItem,value)
    else:
        return bts(item.rightItem,value)



ti0=TreeItem(55,'ti0')
ti1=TreeItem(30,'ti1')
ti2=TreeItem(20,'ti2')
ti3=TreeItem(62,'ti3')
ti4=TreeItem(57,'ti4')
ti5=TreeItem(50,'ti5')
ti6=TreeItem(81,'ti6')
ti7=TreeItem(7,'ti7')
ti8=TreeItem(1,'ti8')
ti9=TreeItem(25,'ti9')


ti0.leftItem=ti1    # 55>30
ti0.rightItem=ti3   # 55<62

ti1.leftItem=ti2    # 30>20
ti1.rightItem=ti5   # 30<50

ti3.leftItem=ti4    # 62>57
ti3.rightItem=ti6   # 62<81

ti2.leftItem=ti7    # 20>7
ti2.rightItem=ti9   # 20<25

ti7.leftItem=ti8    # 7>1


itm=bts(ti0,5)
print(itm)

itm=bts(ti0,120)
print(itm)

itm=bts(ti0,7)
print(itm)

itm=bts(ti0,81)
print(itm)