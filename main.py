from bs4 import BeautifulSoup
import csv
import re


# methods BeautifulSoup

# .find()    # search from beginning to end
# .find_all()

# .parent     # search from end to beginning
# .find_parent()

# .parents    # analog find_all
# .find_parents()

# .find_next_sibling()    # search in an adjacent block
# .find_previous_sibling()


def get_specialist(t):    # func.filter out text
    whois = t.find('div', id='whois').text.strip()
    if 'Copywriter' in whois:
        return t
    return None


def get_salary(t):
    # salary: 2700 usd per month
    pattern = r'\d{1,9}'    # r = row, '\d' any number, {1,9} sarch from 1 to 9

    # salary1 = re.findall(pattern, t)[0]    # where search, when search; get list    
    salary2 = re.search(pattern, t).group()    # 2nd variant
    print(salary2)
    

def main():    # hub all functions
    file = open('index.html').read()    # open file for read html code

    soup = BeautifulSoup(file, 'lxml')    # variable parser 

    # row = soup.find_all('div', class_='row')    # parse tag div, var1
    # row2 = soup.find_all('div', {'class': 'row'})    # parse tag div, var2
    # row2_1 = soup.find_all('div', {'data-set': 'salary'})
    
    # person = soup.find('div', text='Alena').parent
    # person2 = soup.find('div', text='Alena').find_parent(class_='row')


    # filter out text
    # copywriters = soup.find_all('div', class_='row')    # parse all div's with class row      

    # copywriter = []
    # for i in copywriters:
    #     copywr = get_specialist(i)
    #     if copywr:
    #         copywriter.append(copywr)    

    # print(copywriter)   


    # use regular expressions

    # var 1    
    # salary = soup.find_all('div', {'data-set':'salary'})
    # for i in salary:
    #     get_salary(i.text)

    # var 2
    salary = soup.find_all('div', text=re.compile('\d{1,9}'))    # get all text with numbers from 1 to 9
    for i in salary:
        print(i.text) 



if __name__ == '__main__':    # point of enter
    main()