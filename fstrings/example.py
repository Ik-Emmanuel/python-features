import datetime
from dataclasses import dataclass



@dataclass
class User:
    first_name: str
    last_name: str
    
    def __str__(self) -> str:
        """Returns a USER friendly representation"""
        return f"{self.first_name} {self.last_name}"
    
    def __repr__(self) -> str:
        """Returns a DEVELOPER friendly representation"""
        # user = User("","")
        # access it using "!r"  print(f"user: {user!r})
        # or repr() = print(repr(user))
        
        

# """
# Different f string methods and usage
# """

# ===========================
# number = 800
# f"number is {number:e}"       --- scientific representation
# f"number is {number:06}"      --- 000800  (add zeros up to 6 chars)
# f"{100.2634834:.2f}"          --- prints in float of 2 decimal places/ //this also rounds up 
# f"{44000000:,.2f}"            --- formats adds "," then 2 decimal = 44,000,000.00
# {0.34566868:%}                ---- prints it in percentage = 34.56%
# {0.34566868:.3%}              ---- prints it in percentage and 3 decimals = 34.567%


# === Text Alignmnet 
# f"number is {number:6}"        --- .   800  (add spaces up to 6 chars) //for integers
# f"The Text is {text:>6}"       --- .   Hi  (add spaces left up to 6 chars) // for strings add :_>6 to use _ instead of space
# f"The Text is {text:^6}"       --- .  Hi   (add spaces left and right up to 6 chars to center text) // for strings
# f"The Text is {text:<6}"       --- . Hi    (add spaces right  up to 6 char) // for strings


# ====== Date time 
# today = datetime.datetime.now()  //2022-08-19 09:10:21.57575
# f"{today:%H:%M:%S.%f}"        //Just time hr:min:sec:ms = 09:10
# time:%Y-%m-%d                 // year-month-day %Y = 2023  %y = 23
# time:%D                       // just date in mm/dd/yy =  08/19/22
# time:%T                       // just time hr:min:sec
# time:%A                       // just week day = Monday Tuesday Wednesday etc
# time:%A, %B %d, %Y            // Friday, January 12, 2024
# time:%x                       // 01/12/24
# time:%X                       // 10:33:09   time Hr:Min:Sec



# === Escape character
# f"{{\"text\"}}"           // {"text"}

# === debugging
# f"{var = }"                    //var = value_of_var


# ===== Multiline  
# sentence = (
#     f"Hi, my name is {name}. "
#     f"I live in {location}"
# )


# ======  Old styles 
# A = "%s is from %s." %(name, country)

# A = "{} is from {}.".format(name, country)

# A = f"{name} is from {country}"   //fatest

# from string import Template
    # name= "Bob"
    # country= "Netherlands"
    # TEMPLATE = Template("$name is from $country")
    # A = TEMPLATE.substitute(name=name, country=country)
    # print(A)




def main():
    from string import Template
    name= "Bob"
    country= "Netherlands"
    TEMPLATE = Template("$name is from $country")
    A = TEMPLATE.substitute(name=name, country=country)
    print(A)
    
if __name__ == "__main__":
    main() 