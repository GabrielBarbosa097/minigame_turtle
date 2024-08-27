from turtle import Turtle

t = Turtle()
t.speed(1)

print('Seja Bem vindo ao nosso jogo!!!')

while True:
    direcao = str(input('Para qual direceção devemos ir F=Frente, T=Trás? ')).upper()
    if direcao == 'F':
        distancia = int(input('Quantos pixels devemos ir para frente? '))
        rotacao = str(input('Deseja virar para alguam direção D=Direita, E=Esquerda, N=Não virar ')).upper()
        t.forward(distancia)
        if rotacao == 'D':
            direita = int(input('Quantos graus devemos rotacionar? '))
            t.right(direita)
        elif rotacao == 'E':
            esquerda = int(input('Quantos graus devemos rotacionar? '))
            t.left(esquerda)
    if direcao == 'T':
        distancia = int(input('Quantos pixels devemos ir para frente? '))
        rotacao = str(input('Deseja virar para alguam direção D=Direita, E=Esquerda, N=Não virar ')).upper()
        t.backward(distancia)
        if rotacao == 'D':
            direita = int(input('Quantos graus devemos rotacionar? '))
            t.right(direita)
        elif rotacao == 'E':
            esquerda = int(input('Quantos graus devemos rotacionar? '))
            t.left(esquerda)
    continuar = str(input('Deseja continuar? [S/N]')).upper()
    if continuar == 'S':
        continue
    elif continuar == 'N':
        break
        

