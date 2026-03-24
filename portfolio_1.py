'''The Euclidean Algorithm'''
#the class will check the input's validation for the Eulidean Algorithm
class Cheking_number:
    def __init__(self,number1,number2):
        self.number1=number1
        self.number2=number2
    #define function that checks whether the input is integer or not. Accepts only integers 
    def check_valid_number(self):
        try:
            self.number1=int(self.number1)
            self.number2=int(self.number2)
            return True
        except ValueError:
            return False
    #define function that will give positive numbers which greater then 0    
    def check_positive(self):
        if self.number1>0 and self.number2>0:
            return True
        False
#the class that will create the usage of Euclidean algorithm   
class EuclideanAlgorithm:
    def __init__(self,number1,number2):
        self.number1=number1
        self.number2=number2
    #define function that will devide numbers by their remainders    
    def divisor(self):
        print(f"The Greatest Common Devisor of {self.number1} and {self.number2}:")
        #the loop will make sure to devide number by its remainder until remainder is equal to 0
        while self.number2!=0:
            remainder=self.number1 % self.number2 
            self.number1=self.number2
            self.number2=remainder
    #define function that gives the number which is not 0        
    def check_for_0(self):
        if self.number1==0:
            return self.number2
        elif self.number2==0:
            return self.number1
    #define function that will declare the common devisor    
    def declare_common_divisor(self):
        return self.check_for_0()
    
class Runner:
    def __init__(self,number1,number2):
        self.number1=number1
        self.number2=number2
        
    def run_function(self):
        checker=Cheking_number(self.number1, self.number2)
        if not checker.check_valid_number():
            return print("Not valid input")
        elif not checker.check_positive():
            return print("Not valid input")
        else:
            gcd_calculate=EuclideanAlgorithm(checker.number1, checker.number2)
            gcd_calculate.divisor()
            print(f"{gcd_calculate.declare_common_divisor()}")
        
    
print("To find the Greatest Common Devisor(GCD)!")
num1_for_GCD=input("Please enter the first number: ")
num2_for_GCD=input("Please enter the second number: ")

runner=Runner(num1_for_GCD , num2_for_GCD)
runner.run_function()








