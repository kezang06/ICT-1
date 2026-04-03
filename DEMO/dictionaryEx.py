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