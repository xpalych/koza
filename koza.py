import random as rnd

# Стратегия игрока, согласного с предложением ведущего
# b - ставка игрока, k - коза, x - закрытая дверь
StrategySoglashatel = {
    'bkx':['x','k','b'],
    'bxk':['x','b','k'],
    'kbx':['k','x','b'],
    'xbk':['b','x','k'],
    'kxb':['k','b','x'],
    'xkb':['b','k','x']
}

class Gamer(): 
    def __init__(self, strategy = 'Soglashatel'):
        self.__strt = strategy

    def bet(self, bank):
        if bank==['x','x','x']:                         # начало игры
            bank[rnd.randint(0,2)] = 'b'        # первоначальная ставка
        else:                                   # надо реагировать на предложение ведущего
            if (self.__strt=='Soglashatel'):    # если принимаем предложение ведущего, следуем стратегии
                bank = StrategySoglashatel[''.join(bank)] 
            elif (self.__strt=='Upertiy'):      # если нет, то нет
                pass
            else:
                bank = ['x','x','x']
        return bank


class MontyHall():
    def openthedoor(self, bank, gde_mashinka):
        idx=[0,1,2]                             # номера дверей
        idx.remove(gde_mashinka)                # получим номера дверей, где машины нет
        if (bank[gde_mashinka]=='b'):           # игрок угадал с первого захода
            bank[rnd.choice(idx)] = 'k'         # открываем случайную из тех, где нет машины, там полюбому коза
        else:                                   # игрок не правильно указал на дверь
            if bank[idx[0]]=='b':               # \
                bank[idx[1]]='k'               #  |открываем ту, на которую он не ставил
            else:                               #  |и за которой нет машинки
                bank[idx[0]]='k'               # /
        return bank
                
            

def game(n,g,mh):           # n - число прогонов, 
                            # g - экземпляр класса Gamer
                            # mh - экземпляр класса Монти Холла
    bingo, cnt = 0, 0       # счетчики "попал с первой попытки" и "выиграл раунд", соответственно
    for _ in range(n):
        bnk = ['x','x','x']             # Двери закрыты
        pos = rnd.randint(0, 2)         # Решим, где машинка
        bnk = g.bet(bnk)                # Игрок делает ставку на дверь
        if bnk[pos]=='b':               # Если сразу попал, отметим у себя в блокнотике
            bingo += 1                  # 
        bnk = mh.openthedoor(bnk, pos)  # Откроем дверь с козой
        bnk = g.bet(bnk)                # Примем ставку игрока
        if bnk[pos]=='b':               # Если выиграл, напишем плюс
            cnt += 1                    #
    return bingo, cnt


veduschiy = MontyHall()

N=100000
print('Раундов: ',N)

igorek = Gamer('Upertiy')                       # Играем с упертым
print('Игрок не соглашается на предложение:')
x,y = game(N, igorek, veduschiy)
print('Попал сразу:', x)
print('Выиграл:    ', y)

igorek = Gamer('Soglashatel')                   # Играем с хитрым
print('Игрок соглашается на предложение:')
x,y = game(N, igorek, veduschiy)
print('Попал сразу:', x)
print('Выиграл:    ', y)
