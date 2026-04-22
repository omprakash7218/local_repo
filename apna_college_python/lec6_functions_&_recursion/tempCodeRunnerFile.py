
cars = ["bugati cheron", "scorpio s5", "aulto 800", "renault duster"]

index = 0
def elements(lists):
    global index
    if len(lists)==index:
        return 0
    print( lists[index]) 
    index += 1 
    elements(lists)

(elements(cars))
