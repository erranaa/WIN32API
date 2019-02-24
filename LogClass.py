from ApiBase import *
import datetime
import logging


class LogClass(ApiBase):

    def request(self):
        pass


class LogJoker(LogClass):
    logging.basicConfig(filename='joker.log', level=logging.DEBUG)
    handler2 = logging.FileHandler(filename='joker.log')

    logging.debug('This message should go to the log file')


    def request(self):
        pass


class LogUser(LogClass):
    logging.basicConfig(filename='user.log', level=logging.DEBUG)
    handler1 = logging.FileHandler(filename='user.log')
    logging.log(logging.DEBUG, "new msg")

    logging.debug('This message should go to the log file')


    def request(self):
        pass


class LogBored(LogClass):
    logging.basicConfig(filename='bored.log', level=logging.DEBUG)
    handler = logging.FileHandler(filename='bored.log')

    logging.debug('This message should go to the log file')


    def request(self):
        pass


class decorateFile(LogClass):
    def __init__(self, wrapper):
        self._wrapper = wrapper

    def render(self):
        return "<i>{}</i>".format(self._wrapped.render())


def main():

    real_subject = LogClass()

    bore = BoredApi(real_subject)
    use = UserApi(real_subject)
    joke = JokeApi(real_subject)

    a = input("Please enter your name\n")
    print("Welcome to the Game.", a)

    print("I see you got bored. Let me offer you some nice solutions.")
    number = bore.request()


    if number == 1:
        print("You can do this activity all by yourself!")
        print("I will also make a joke to make you laugh!")
        joke.request()


    elif number > 1:
        print("Go do this activity")

        for i in range(number-1):
            use.request()
            name = getattr(use, 'name')
            surname = getattr(use, 'surname')
            print("WITH", name, surname)


main()