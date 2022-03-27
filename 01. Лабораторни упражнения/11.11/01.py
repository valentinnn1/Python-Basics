def func(list):
    biggestnum = 0
    theindex = 0

    for i in range(0, len(list)):
        if (list[i] > biggestnum):
            biggestnum = list[i]
            theindex = i
    
    print(f'Най-голямото число е {biggestnum} на индекс {theindex}')

func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
func([4, 12, 33, 24, 75, 56, 37, 18, 29, 1])
func([11, 27, 39, 44, 25, 16, 47, 98, 19, 6])
