# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from page_url import PageUrl
from beautiful_soup import BeautifulSoup
from write_csv import WriteCsv
from write_xls import WriteXls
from write_xlsx import WriteXlsx

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(PageUrl.QUOTES.value)
    print(PageUrl.BOOKS.value)

    bs = BeautifulSoup(PageUrl.QUOTES.value)
    bs.get_page_urls()
    list = bs.get_data()
    #list = [{'quote': '“A day without sunshine is like, you know, night.”', 'author': 'Steve Martin', 'tags': ['humor', 'obvious', 'simile']}, {'quote': '“Life is what happens to us while we are making other plans.”', 'author': 'Allen Saunders', 'tags': ['fate', 'life', 'misattributed-john-lennon', 'planning', 'plans']}, {'quote': '“One good thing about music, when it hits you, you feel no pain.”', 'author': 'Bob Marley', 'tags': ['music']}, {'quote': '“It is never too late to be what you might have been.”', 'author': 'George Eliot', 'tags': ['inspirational']}, {'quote': '“Love does not begin and end the way we seem to think it does. Love is a battle, love is a war; love is a growing up.”', 'author': 'James Baldwin', 'tags': ['love']}, {'quote': "“Life isn't about finding yourself. Life is about creating yourself.”", 'author': 'George Bernard Shaw', 'tags': ['inspirational', 'life', 'yourself']}, {'quote': "“I have heard there are troubles of more than one kind. Some come from ahead and some come from behind. But I've bought a big bat. I'm all ready you see. Now my troubles are going to have troubles with me!”", 'author': 'Dr. Seuss', 'tags': ['troubles']}, {'quote': "“′Classic′ - a book which people praise and don't read.”", 'author': 'Mark Twain', 'tags': ['books', 'classic', 'reading']}, {'quote': '“I believe in Christianity as I believe that the sun has risen: not only because I see it, but because by it I see everything else.”', 'author': 'C.S. Lewis', 'tags': ['christianity', 'faith', 'religion', 'sun']}, {'quote': '“... a mind needs books as a sword needs a whetstone, if it is to keep its edge.”', 'author': 'George R.R. Martin', 'tags': ['books', 'mind']}]

    # write xls file
    #wc = WriteXls(list)
    #wc.write_file()

    # write xlsx file
    wc = WriteXlsx(list)
    wc.write_file()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
