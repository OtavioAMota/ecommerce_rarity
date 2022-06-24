from django import template
# script necessario para criar um filtro que nao tem no django
register = template.Library() # linha necessaria registrar um filtro diferente

@register.filter() #decoreitor
def remainder(n): # retorna o resto
    return n % 3
