phones = ['nokia', 'motorolla', 'samsung']
print(phones)
phones_count = len(phones)
print(phones_count)
phones.append('iphpone')
print(phones)
print(phones.count('motorolla'))

print(phones.index('nokia'))

phones.sort()
print(phones) 
phones.remove('motorolla')
print(phones)