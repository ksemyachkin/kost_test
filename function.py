from dis import dis


def discounted(price, discount, max_discount = 25):
    price = abs(float(price))
    discount = abs(float(discount))
    if discount > max_discount:
        raise ValueError('ты ахуел делать скидку больше 25%')
    else:
        price_with_discount = price - price * discount / 100
    return(price_with_discount)

product = {
    'name': 'auto',
    'model': 'audi',
    'series': 'A8',
    'price': 5200
}

product['discount'] = input('ввидите процент скидки ')

print('Товар: ', product)
print(discounted(product['price'], product['discount']))