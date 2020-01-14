import pickle, os
if not os.path.isfile("user.dat"):
    data = [0, 1, 2]
    data[0] = input("Pick a username: ")
    data[1] = input("Pick a password: ")
    data[2] = input("DATA to store: ")
    file = open('user.dat', 'wb')
    pickle.dump(data, file)
    file.close()
    print('Re-run this program to log in')
else:
    file = open('user.dat', 'rb')
    data = pickle.load(file)
    file.close()
    pcheck = input('Password: ')
    file.close()
    if pcheck == data[1]:
        print("Welcome, " + data[0])
        print("Stored Data:  " + data[2])
        
    else:
        print("Error 403: Access denied")
        
    
    
