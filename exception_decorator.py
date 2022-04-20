from utility import my_logger
from utility import exception_handler_logger

# create the object of logger
Obj = my_logger("exception_decorator.log")
loggerObj = Obj.create_logger()


@exception_handler_logger('after_div()', loggerObj)
def div(a, b):
    print("divison is ", a / b)


@exception_handler_logger('after_div1()', loggerObj)
def div1(a, b):
    print("divison is ", a / b)


@exception_handler_logger('add(a,b)', loggerObj)
def div2(a, b):
    print("divison is ", a / b)


@exception_handler_logger(loggerObj=loggerObj)
def after_div():
    print("No Error Found in div")


@exception_handler_logger(loggerObj=loggerObj)
def after_div1():
    print("No Error Found in div1")


@exception_handler_logger(loggerObj=loggerObj)
def after_div2(c, d):
    print("No Error Found in div2")
    print("access of global value of c and d ", c, d)


@exception_handler_logger(loggerObj=loggerObj)
def add(a, b):
    print("addition is", a + b)


def runall():
    global c, d, a, b
    a = 10
    b = 0
    c = "Hello"
    d = "deepak"
    check = []
    check.append(div(a, b))
    check.append(div1(a, b))
    check.append(div2(a=20, b=10))
    print("check", check)
    # based on Flag value it will run the function
    # if there is no error in the code then flag value is 1 else 0
    [eval(i[2]) for i in check if i[1] == 1]
    # log the error occurred
    [loggerObj.error(i[2].split('(')[0] + " had Error. Please check the log file for more Info") for i in check if i[1] == 0]
    print("Do some other works")


if __name__ == "__main__":
    loggerObj.info("Script started")
    runall()
    loggerObj.info("Script completed")

