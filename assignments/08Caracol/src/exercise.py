def main():
    #escribe tu código abajo de esta línea
    min=0
    cm=0
    seg=0
    mm=0
    
    min=float(input())
    seg=min*60
    
    mm=(seg*5.7)
    cm=(mm/10)
    
    print(cm)
    
    pass

if __name__ == '__main__':
    main()
