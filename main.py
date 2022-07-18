from controleer.run import Controler

while True:
    try:
        if __name__ == '__main__': # головний файл
            con = Controler() # виклик конролера
            con.run() # виклик метода ран
    except Exception as e:
       print(e)
