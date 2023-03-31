class Surface:
    def _init_(self, x, y, w, l):
        self.x=x
        self.y=y
        self.length=1
        self.width=w
    def getRect(self):
        return (self.x, self.y, self.width, self.length)