import configparser  # its's defaults package

config = configparser.RawConfigParser()
config.read('.\\Configuration\\config.ini')


class Readconfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        useremail = config.get('common info', 'username')
        return useremail

    @staticmethod
    def getuserpasswor():
        userpassword = config.get('common info', 'password')
        return userpassword
