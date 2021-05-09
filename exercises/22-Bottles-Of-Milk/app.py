def number_of_bottles():
    count = 100
    while count > 0:
        print("{} bottles of milk on the wall, {} bottles of milk.\nTake one down and pass it around, {} bottles of milk on the wall.".format(count,count,count))
        if count == 1:
            print("{} bottles of milk on the wall, {} bottles of milk.\nTake one down and pass it around, no more bottles of milk on the wall".format(count,count))
        count -= 1


number_of_bottles()