class TreeItem:

    def __init__(self, value=0):
        self.leftItem=None
        self.rightItem=None
        self.value=value


ti0=TreeItem(55)
ti1=TreeItem(50)
ti2=TreeItem(20)
ti3=TreeItem(62)
ti4=TreeItem(21)
ti5=TreeItem(74)
ti6=TreeItem(81)
ti7=TreeItem(7)
ti8=TreeItem(1)
ti9=TreeItem(95)


ti0.leftItem=ti1    # 70>50
ti0.rightItem=ti3   # 70<62

ti1.leftItem=ti2    # 50>20
ti1.rightItem=ti5   # 50<74

ti3.leftItem=ti4    # 62>21
ti3.rightItem=ti6   # 62<81

ti2.leftItem=ti7    # 20>7
ti2.rightItem=ti9   # 20<95

ti3.leftItem=ti9    # 62>1


