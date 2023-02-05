# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

add=lambda x,y:x+y
l=[7,8,1,2,3,4,5]
a=[3,4,1,29,1,5,1]
d=list(map(add,l,a))
print(d)
e=[4,1,69,2,7,3,6]
f=list(map(add,d,e))
print(f)
mul=lambda x,y:x*y
y=list(map(mul,d,f))
print(y)
