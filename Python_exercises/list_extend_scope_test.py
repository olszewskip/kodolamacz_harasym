def main():
    li = [1, 2, 3]

    def foo():
        li.extend([4])

    def boo():
        li += [5]

    foo()
    print(li)
    boo()  # this will fail

main()