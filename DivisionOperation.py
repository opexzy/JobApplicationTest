
class Division:

    def __init__(self,numerator,denominator):
        self.nume = numerator
        self.deno = denominator
        self.main_list = []

    def generateList(self):
        if(self.deno > 0 and self.nume > 0):
            for num in range(1,self.nume+1):
                self.main_list.append(num)
        else:
            for num in range(1,abs(self.nume)+1):
                self.main_list.append(num * -1)


    def binarySearchHelper(self,arg="none"):
        bound_list = [];
        if(arg == "none"):
            bound_list = self.main_list.copy()
        else:
            bound_list = arg

        if(len(bound_list) > 1):
            list_length = len(bound_list)
            if list_length % 2 == 0:
                mid_index = (list_length // 2) - 1
            else:
                mid_index = (list_length // 2)
            self.mid_value = bound_list[mid_index]
            self.L_div = bound_list[0:mid_index].copy()
            self.R_div = bound_list[mid_index+1:list_length].copy()

    def nextMidValue(self,next_list):
        if (len(next_list) > 1):
            list_length = len(next_list)
            if list_length % 2 == 0:
                mid_index = (list_length // 2) - 1
            else:
                mid_index = (list_length // 2)
            self.mid_value = next_list[mid_index]
            self.L_div = next_list[0:mid_index].copy()
            self.R_div = next_list[mid_index + 1:list_length].copy()
            return self.mid_value

    def calc(self):
        if(self.deno == 0):
            print("Division by zero not allowed")
            exit()
        if(self.nume == 0):
            print("Quotient = " + 0 + ", Remainder = " + 0)
        self.generateList()
        self.binarySearchHelper()
        self.last_mid = self.mid_value
        if(self.nume > 0 and self.deno > 0):
            while True:
                if(self.mid_value * self.deno) < self.nume:
                    if(self.mid_value >= self.last_mid):
                        self.last_mid = self.mid_value
                    if len(self.R_div) <= 1:
                        if (self.R_div[0] * self.deno <= self.nume):
                            self.last_mid = self.R_div[0]
                            break
                        else:
                            self.last_mid = self.mid_value
                            break
                    else:
                        self.nextMidValue(self.R_div)
                        continue
                elif(self.mid_value * self.deno > self.nume):
                    if len(self.L_div) <= 1:
                        if (self.L_div[0] * self.deno <= self.nume):
                            self.last_mid = self.L_div[0]
                            break
                        else:
                            self.last_mid = self.mid_value
                            break
                    else:
                        self.nextMidValue(self.L_div)
                        continue
                else:
                    self.last_mid = self.mid_value
                    break
        elif(self.nume > 0 and self.deno < 0):
            return




x = Division(6,-5)
x.calc()
print(x.last_mid)