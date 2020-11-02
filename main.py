from bs4 import BeautifulSoup
import csv


# methods BeautifulSoup

# .find()    # search from beginning to end
# .find_all()

# .parent     # search from end to beginning
# .find_parent()

# .parents    # analog find_all
# .find_parents()

# .find_next_sibling()    # search in an adjacent block
# .find_previous_sibling()


def main():    # hub all functions
    file = open('index.html').read()    # open file for read html code

    soup = BeautifulSoup(file, 'lxml')    # variable parser 

    row = soup.find_all('div', class_='row')    # parse tag div, var1
    row2 = soup.find_all('div', {'class': 'row'})    # parse tag div, var2
    row2_1 = soup.find_all('div', {'data-set': 'salary'})
    
    person = soup.find('div', text='Alena').parent
    person2 = soup.find('div', text='Alena').find_parent(class_='row')



    print(person2)





if __name__ == '__main__':    # point of enter
    main()