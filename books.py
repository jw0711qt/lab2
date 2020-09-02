
class Author:   #creatinmg Author class
    def __init__(self, name):
        self.name = name
        self.books  = []
    def publish(self, title): #handle duplication of books
        title=title.lower()
        if title in self.books:
            print ( f'sorry, this book is duplicated: {title}')
        else:
            self.books.append(title)

    def __str__(self):# hande Author with out published books
        if self.books:
             book_list=','.join(self.books) 
        else:
            book_list='No Published books'
            
        return f'Name:{self.name}. Books Published: {book_list}'
      
def main():

    shakespeare = Author('William Shakespeare') # Author name
    shakespeare.publish('Hamlet')#Author book
    shakespeare.publish('Richars III')
    print(shakespeare)


    ernest  = Author('Ernest Hemingway') # Author name
    ernest.publish('The Old Man and the Sea')#Author book
    ernest.publish('A Farewell to Arms')
    ernest.publish('The Sun Also Rises')
    ernest.publish('A Farewell to Arms')
    print(ernest)


                            
    fila=Author('filmon') # Author name
    print(fila)
main()

