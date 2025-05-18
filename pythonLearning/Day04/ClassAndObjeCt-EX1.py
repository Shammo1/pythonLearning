class Triangle :
    def __init__(self,base,height):
        self.base=base
        self.height=height
    
    def output(self):
        x=(self.base*self.height)/2
        print(f"area = {x}")



tri_angle_1=Triangle(10,20)
tri_angle_1.output()

tri_angle_2=Triangle(20,30)
tri_angle_2.output()
