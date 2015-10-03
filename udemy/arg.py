

#* means looking for a list
#** means looking for a dict
def F(*args, **kwargs):
    for arg in args:
        print arg
    print kwargs
    pass

hair_color = 'Brown'

F(hair_color)

F(hair_color, eyes='Blue')


def F(hair, eyes='Green'):
    print hair, eyes
    
F(hair_color)
