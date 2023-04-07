preçoMercadoria = float(input('digite o preço da mercadoria: '))
desconto = int(input('digite o percentual de desconto: '))
desconto = (desconto / 100) * preçoMercadoria
preçoComDesconto = preçoMercadoria - desconto
print(f'seu desconto na mercadoria é de R$ {desconto} e o preço a apagar é de R$ {preçoComDesconto}')
