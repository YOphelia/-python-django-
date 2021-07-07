from django.utils import timezone
a = 1
b=0

def print_a(b):
    global a
    a = b
    print( a)

def print_use(u):
    global b
    b=u
    print(b)
def print_b():
    print (a)


def main():
    pass


if __name__ == '__main__':
    # d3=timezone.localtime()
    # print(d3)
    main()