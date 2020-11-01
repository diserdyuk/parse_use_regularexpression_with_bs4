from bs4 import BeautifulSoup
import csv



# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')


def main():    # hub all functions
    file = open('index.html').read()    # open file for read html code
    print(file) 


if __name__ == '__main__':    # point of enter
    main()