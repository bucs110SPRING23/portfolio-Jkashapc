class Rectangle():
    def _init_(self,x,y,l,w):
        self.x=x
        self.y=y
        self.length=1
        self.width=w
    def _str_(self):
        return f"Rectangle(width={self.width}, length={self.length})"