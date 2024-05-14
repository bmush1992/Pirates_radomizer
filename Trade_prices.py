import random
from contextlib import redirect_stdout
import os


# Формирование цены
def sellPriceLow():
    resultSellPriceLow = random.randint(1, 8)*5
    return resultSellPriceLow
    

def sellPriceHigh():
    resultSellPriceHigh = random.randint(1, 8)*5 + random.randint(1, 8)*5
    return resultSellPriceHigh

def buyPriceLow(sellPrice):
    resultBuyPriceLow = max(5, sellPrice - random.randint(1, 4)*5)
    return resultBuyPriceLow

def buyPriceHigh(sellPrice):
    resultBuyPriceHigh = max(5, sellPrice - random.randint(1, 4)*5)
    return resultBuyPriceHigh

# Складываем цены в товары
def goodPairLow(good):
    sellPrice = sellPriceLow()
    resultStringLow = f'{good}: {sellPrice}/{buyPriceLow(sellPrice)}'
    return resultStringLow

def goodPairHigh(good):
        sellPrice = sellPriceHigh()
        resultStringHigh = f'{good}: {sellPrice}/{buyPriceHigh(sellPrice)}'
        return resultStringHigh

def slavesExceptionInd():
        resultStringSlavesInd = f'Рабы: {sellPriceHigh()}/'
        return resultStringSlavesInd

def slavesExceptionTown():
        resultStringSlavesTown = f'Рабы:   /{sellPriceHigh()}'
        return resultStringSlavesTown

def weaponsException():
        resultStringWeaponsInd = f'Оружие: /{sellPriceHigh()}'
        return resultStringWeaponsInd



# Распределяем товары по категориям
def goodType(good):
    if good == 'Припасы' or good == 'Стройматериалы' or good == 'Вино':
        return goodPairLow(good)
    else:
        return goodPairHigh(good)
    
# Складываем с городом
def townTable(town):
    arrayGoods = ['Припасы', 'Стройматериалы', 'Вино', 'Украшения', 'Оружие', 'Рабы']
    # townTableResult = 
    if town == 'Альпокки' or town == 'Мауро' or town == 'Туачча':
            print(f'{weaponsException()}\n{slavesExceptionInd()}')
    else:

        for good in range(0,len(arrayGoods)):
        
            if arrayGoods[good] == 'Рабы':
                print(slavesExceptionTown())
            else:
                print(goodType(arrayGoods[good]))
            
       # Финалка
def finalTable():
    arrayTown = ['Темпора', 'Тирр', 'Байтон', 'Ислан', 'Калпус', 'Айвел', 'Пирайт', 'Хомбор', 'Альпокки', 'Мауро', 'Туачча']
    for town in range(0,len(arrayTown)):
        print(f'\n{arrayTown[town]}\n')
        townTable(arrayTown[town])
directory_path = os.path.dirname(os.path.realpath(__file__))

with open(f'{directory_path}/out.txt', 'w') as f:
    with redirect_stdout(f):
        finalTable()






