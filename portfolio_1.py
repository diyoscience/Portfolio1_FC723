'''The Euclidean Algorithm'''

class EuclideanAlgorithm:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def devisor(self):
        while self.b!=0:
            c=self.a % self.b 
            self.a=self.b
            self.b=c
            
    def check_for_0(self):
        if self.a==0:
            return self.b
        else:
            return self.a
        
    def declare_common_devisor(self):
        return f" The Greatest common devisor of {self.a} and {self.b} is {self.check_for_0()} "
        
divid=EuclideanAlgorithm(267,890) 
divid.devisor()   
print(divid.declare_common_devisor())           
        
    









