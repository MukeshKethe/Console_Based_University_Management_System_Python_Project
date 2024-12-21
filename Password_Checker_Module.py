import re
class Password:
    def __init__(self):
        self.epassword = ''
    def password(self):
        while True:
            match = None
            pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
            password = input('Enter a Password: ')
            cpassword = input('Enter Confirm Password: ')
            if password == cpassword:
                match = pattern.match(cpassword)
                self.epassword = cpassword
            else:
                print('Confirm Password Doesn\'t Match with Password')

            if match != None:
                print('Password Created Successfully')
                break
            else:
                print('Password Should Contain Minimum Eight Characters with atleast 1 Capital Letter, 1 Small Letter, 1 Digit and 1 Special Character')

    def verify_password2(self, u_password):
        if u_password == self.epassword:
            return True
        else:
            return False

obj = Password()

        


        

