def color(str):
    text = str.strip().capitalize()
    cor = {'Vermelho': '\033[31m',
           'Verde': '\033[32m',
           'Amarelo': '\033[33m',
           'Azul': '\033[34m',
           'Roxo': '\033[35m',
           'Limpa': '\033[m'}
    return cor[text]