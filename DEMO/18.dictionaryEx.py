userDetails = {'Id' : 1, 'userName': 'Just_me'}
print(type(userDetails)) 
print(userDetails) #output: {'Id': 1, 'userName': 'Just_me'}

location = dict (s = 'Samtse', t = 'Thimphu', p = 'Paro')
print(location) 
print(userDetails['userName'])
print(location.get('t'))

userDetails['email'] = 'justme@example.com'
print(userDetails) #output: {'Id': 1, 'userName': 'Just_me', 'email': '
userDetails['userName'] = 'Just_me_updated'
print(userDetails) #output: {'Id': 1, 'userName': 'Just_me_updated', 'email': '

del location['p']
print(location) #output: {'s': 'Samtse', 't': 'Thimphu'}

deleted_value = userDetails.pop('email') 
print(deleted_value) #output: justme@example.com

del_key, del_value = userDetails.popitem()
print(f'the deleted key: {del_key} and the deleted value: {del_value}')
location.clear()
print(location) #output: {} #location is now empty
