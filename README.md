## Introduction to Python

Github Classroom Assignment Link : https://classroom.github.com/a/oUE_Og9m

Tasks Definition : https://docs.google.com/document/d/1V1gYEKLtOPYzZL7F9koaDVdgIlOXl_ALspjyzOZJN7Q/edit?usp=sharing

### Understanding solid principles.

SOLID principle is a convention in OOP that makes code reuseable, maintainable and stable. It helps to minimize changes in code by ensuring classes are loosely coupled. (Loosely coupled means that classes are minimally dependent on each other).

                            S 
Single Responsibility Principle (SRP): this states that "a class should have only one reason to change" and it simply means that a function should achieve only one goal. All methods and attributes in the class definition should work towards producing a single result.
If a class has an "and" in its responsibility description then its is necessary to have another class handle whatever comes after the "and".

For Example:
Saying "It is the duty of a chef to cook and serve the food", serve the food which comes after "and" should be someone else's duty - so this can be given to the server. THe chef cooks, the server serves. One person one responsibility. 

In python we can have the code below to illustrate one class one responsibilty:
    <!-- //////////////WRONG APPROACH/////////////////// -->
class User:
    def __init__(self,name,occupaton,gender,date_of_birth):
        self.name = name
        self.occupation = occupation
        self.gender = gender
        self.date_of_birth = date_of_birth
    def create_user(self, name):
        <!-- #some code to create user object here-->
    def calculate_user_age():
        <!-- some code to calculate user age from date of birth -->

        

 <!-- /////////APPROACH THAT FULFILLS SRP//////////////// -->
class User:
    def __init__(self,name,occupaton,gender,date_of_birth):
        self.name = name
        self.occupation = occupation
        self.gender = gender
        self.date_of_birth = date_of_birth
    def create_user(self, name):
        <!-- ///////////SOME CODE HERE/////////////// -->
class UserAge(CreateUser):
    def calculate_age():
    <!-- some code to calculate user age -->

                            O

OPEN/CLOSE PRINCIPLE states that software entities should be open for extension but closed for modification. A class behaviour should be scalable without modifying what was originally define in the class.

For Example:
A fast growing grocery store want to add a fresh vegetable section based on customer's demand. This is to be done without changing the position of anything in the store. The new section was simply added as an extension at the backside. -------- This is a simply illustration of extension without modification.

<!-- ///////////IN PYTHON///////// -->

<!-- /////////THIS WAS MODIFIED///////// -->
class Customer:
  def __init__(self, name, age):
      self.name = name
      self.age = age
  def checkAgeRange(self):
      if self.age >= 30:
          return "Adult "
      else:
        return "Still a youth, Enjoy!"

<!-- /////////THIS WASN'T MODIFIED, IT'S EXTENDED///////// -->

class Customer:
    def __init__(self, name, age):
      self.name = name
      self.age = age
    def check_age:
        return "Still a youth, Enjoy!"
class Adult(Customer):
    def check_age:
        return "Adult"


                            L
LISKOV SUBSTITUTION PRINCIPLE states that a child class must be substituteable for its parent's class without causing unexpected behaviour. That is, clients are unaware of changes in class heirarchy and work perfectly with any child of the parent class.

<!-- ///////////////LSP ExAMPLE WITH A CHESS GAME//////// -->
class Player():
  def __init__(self, color, board):
    create_pawn()
    self.color = color
    self.board = board
  def move(self, pawn:Pawn, position:int):
      pawn.move(position)
      chessmate_check()
  board = ChessBoard()
  player_white = Player("white", board)
  player_black = Player("black", board)
  pawn = Player_white.Pawn
  horse = helper.getHorse(Player_white, 1)
  Player.move(horse)
 
 /////pawn.move and Player.move
    
                            I
                    
INTERFACE SEGREGATION PRINCIPLE: this states that a client should not implemement an interface that it doesn't use. That is interfaces should be broken into smaller chunks to meet the exact needs of clients. Clients should not be forced to depend on methods thye donot use


                                D
                    
DEPENDENCIES INVERSION PRINCIPLE: states that high level modules should not depend on low level modules. Both high level and low level should depend on abstraction rather than details.




