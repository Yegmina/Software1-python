import hashlib
correct_username="python"
password_hash="6c621d1a05138a7888d37d9269a9da8e2e11e4aced2f6cfd24b05ab1b9e61bb0"
#this is sha256 hash, generated separately from this script

def sha256(password): #function for hash calculation
    return hashlib.sha256(password.encode()).hexdigest()
i=1

while i<=5:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username==correct_username and sha256(password)==password_hash:
        print("Welcome")
        exit() #sth like stop command
    else:
        print("Wrong username or password, try again!")
    i=i+1
print("Access denied")
#and now a little explanation
#why didn't I just use password==correct_password?
#so, answer is quite easy
#if use password==correct_password, we should define correct_passsword
#and that means, that everyone, who can see this script, will be able to get access (just stole password and login from script)
#to prevent this, I used hash algorithm. So, we save only hash in script.
#and after user provide password, we can create hash from this password and check this hash (is this hash equal to hash from correct password)
#so, in my opinion, this way is much better than simple checking



