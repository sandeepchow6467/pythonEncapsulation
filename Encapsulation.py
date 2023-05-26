#If the main function is defined the code doesn't get printed unless we give the remaining code
def main():
    print("sandeep")
print("Hello")
#So we can see from top, unless the remaining code is not executed for main function it doesn't print out.
#The remaining function can be if__name__ == "__main__"
def main():
    print("sandeep")
if __name__ == "__main__":
    main()
print("Hello")
#It is because it needs if statement along with checking whether the __name__ file is equal to __main__
#Only then the code gets executed and prints the main function.(Reusable programs or standalone programs)

def main():
    print("Sandeep Gude")
if __name__ == "__main__":
    main()
print("Python file")
print("variable name is:  ",__name__)
#Also the following main function executes in other way without using if statement. Also make sure to leave space after
#the main function and start from first.
def main():
    print("Ford")

main()
print("Dodge")

# == is used for comparision in python whether argument is true or false. = is used for assigning value to a object.