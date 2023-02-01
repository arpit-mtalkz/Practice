import Contact_book 
from flask import Flask

app=Flask(__name__)



object1=Contact_book.phonebook()

object2=Contact_book.menu()

object3=Contact_book.add_contact()

object4=Contact_book.delete_contact()

object5=Contact_book.delete_all()

object6=Contact_book.search_contact()

object7=Contact_book.update_contact()

object8=Contact_book.display_all()