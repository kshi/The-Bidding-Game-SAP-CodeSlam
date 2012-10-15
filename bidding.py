from math import floor

def calculate_bid(player,pos,first_moves,second_moves):
    my_money = 100
    his_money = 100
    iwinondraw = True
    movestowin = pos
    if player == 1:      
        for turn in range(len(first_moves)):
            if first_moves[turn] < second_moves[turn]:
                his_money -= second_moves[turn]
            elif first_moves[turn] > second_moves[turn]:
                my_money -= first_moves[turn]
            else:
                if iwinondraw:
                    my_money -= first_moves[turn]
                    iwinondraw = False
                else:
                    his_money -= second_moves[turn]
                    iwinondraw = True
    elif player == 2:
        movestowin = 10 - pos
        iwinondraw = False
        for turn in range(len(first_moves)):
            if first_moves[turn] < second_moves[turn]:
                my_money -= second_moves[turn]
            elif first_moves[turn] > second_moves[turn]:
                his_money -= first_moves[turn]
            else:
                if iwinondraw:
                    my_money -= second_moves[turn]
                    iwinondraw = False
                else:
                    his_money -= first_moves[turn]
                    iwinondraw = True

    fractions = [0, 1, 0.366025, 0.211325, 0.154701, 0.133975]    #math ftw
    
    if movestowin < 5:
        rawbid = fractions[movestowin] * my_money
    elif movestowin > 5:
        rawbid = fractions[10 - movestowin] * his_money
    elif movestowin == 5:
        rawbid = fractions[5] * min(my_money, his_money)

    if iwinondraw:
        bid = int(min(floor(rawbid), my_money))
    else:
        bid = int(min(floor(rawbid + 1.01), my_money))

    if my_money == 0:
        return 0
    elif his_money == 0:
        return 1
    else:
        return max(bid,1)
