from datetime import date


def viernes_13 (year:int,mes:int):
    
    
    d=date(year,mes,13)

    if d.weekday() == 4:
        print("Es viernes 13")
        return True
    return False
    #return viernes

print(viernes_13(2023,1))