largest = None
smallest = None
while True:
    num = input()

    if num=='done':
        print('Maximum is',largest)
        print('Minimum is',smallest)
        break

    try:
        n=int(num)
    except:
        print('Invalid input')
        continue

    if largest is None:
        largest=n
    if smallest is None:
        smallest=n
    if n>largest:
        largest=n
    if n<smallest:
        smallest=n
