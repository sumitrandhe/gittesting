from selenium import webdriver
import time
from selenium.webdriver.common.by import By

try:
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://testautomationpractice.blogspot.com/")
    time.sleep(2)
    BookNames = '//table[@name="BookTable"]//tbody//tr[{}]//td[1]'
    Author = '//table[@name="BookTable"]//tbody//tr[{}]//td[2]'
    Subject = '//table[@name="BookTable"]//tbody//tr[{}]//td[3]'
    Price = '//table[@name="BookTable"]//tbody//tr[{}]//td[4]'

    books = {}
    book_list=[]
    author_list=[]
    subject_list = []
    price_list = []

    books['BookNames']=[]
    books["author"]=[]
    books["subject"]=[]
    books["price"]=[]


    for i in range(2,8):
        e = BookNames.format(i)
        book_name = driver.find_element(By.XPATH,e)
        book_list.append(book_name.text)
    books['BookNames'] = book_list
    print(books)

    for i in range(2,8):
        e = Author.format(i)
        author_name = driver.find_element(By.XPATH,e)
        author_list.append(author_name.text)
    books['author'] = author_list
    print(books)

    for i in range(2,8):
        e = Subject.format(i)
        subject = driver.find_element(By.XPATH,e)
        subject_list.append(subject.text)
    books['subject'] = subject_list
    # print(books)

    for i in range(2,8):
        e = Price.format(i)
        price = driver.find_element(By.XPATH,e)
        price_list.append(price.text)
    books['price'] = price_list
    print(books)

    for i in range(0,7):
        print(books.get('BookNames')[i],":",books.get('author')[i],":",books.get('subject')[i],":",books.get('price')[i])

except Exception as e:
    print(str(e))
finally:
    driver.close()


