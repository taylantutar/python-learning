def Hi(func):
    def Wrapper():
        print("Start")
        func()
        print("End")

    return Wrapper    


    
# without decorators
# def func1():
#     print("Hiiiii")

# say_hi = Hi(func1)
# say_hi()



# Within decorators
@Hi
def func1():
   print("Hiiiii")

func1()
