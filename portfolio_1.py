'''The Euclidean Algorithm'''
class Cheking_number:
    def __init__(self,number1,number2):
        self.number1=number1
        self.number2=number2
        
    def check_valid_number(self):
        try:
            self.number1=int(self.number1)
            self.number2=int(self.number2)
            return True
        except ValueError:
            print('it is not valid input')
            return False
    def check_0_for_both(self):
        if self.number1==0 and self.number2==0:
            return False
        return True
        
    
class EuclideanAlgorithm:
    def __init__(self,number1,number2):
        self.number1=number1
        self.number2=number2
        
    def devisor(self):
        print(f"The Greatest Common Devisor of {self.number1} and {self.number2}:")
        while self.number2!=0:
            remainder=self.number1 % self.number2 
            self.number1=self.number2
            self.number2=remainder
            
    def check_for_0(self):
        if self.number1==0:
            return self.number2
        elif self.number2==0:
            return self.number1
        
    def declare_common_devisor(self):
        return self.check_for_0()
    
class Runner:
    def __init__(self,number1,number2):
        self.number1=number1
        self.number2=number2
        
    def run_function(self):
        checker=Cheking_number(self.number1, self.number2)
        if not checker.check_valid_number():
            return "Not valid input"
        elif not checker.check_0_for_both():
            return "Not valid input"
        else:
            gcd_calculate=EuclideanAlgorithm(checker.number1, checker.number2)
            gcd_calculate.devisor()
            print(f"{gcd_calculate.declare_common_devisor()}")
        
    
print("To find the Greatest Common Devisor(GCD)!")
num1_for_GCD=input("Please enter the first number: ")
num2_for_GCD=input("Please enter the second number: ")

runner=Runner(num1_for_GCD , num2_for_GCD)
runner.run_function()








