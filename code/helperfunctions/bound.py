def upperbound():
    """ This function does not take in arguments, computes the upperbound
    for (when prompted) given variables and returns this value. """
    print('Hi, you wish to calculate the upper bound to your problem?')
    print()
    nships = input('please give me an integer of how many ships you have? ')
    print()
    npackages = input('now please tell me how many packages you have? ')
    print()
    startnum = int(nships) * int(npackages)
    total = startnum
    for i in range(1, int(npackages)):
        total = total * (startnum - (i * int(nships)))

    f = open('bound.txt', 'w+')
    f.write(str(total))
    f.close
    print('beceause im so awesome i can tell you that your total is: '
          + str(total))
    print('for your convenience the solution is now in bound.txt')
    print('running this on Axels pc will cost ' + str(total / float(2500)) +
          ' seconds or ' + str((total / float(2500))/3600) + ' hours')


upperbound()
