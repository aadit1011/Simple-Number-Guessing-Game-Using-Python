#Number Guessing game....By_Aadit Sharma
import random;
import math;
correct_answer=False;
chance=None;
division=None;
count=0;
def random_number():
     higher=int(input("Please Enter the higher limit="));
     calculating_chance(higher);
     number=random.randint(1, higher);
     return number;


def calculating_chance(number):
     global chance;
     chance=math.ceil((math.log2(number)));

def main():
     global chance,correct_answer;
     comp=random_number();
     print(f"You have total {chance} chance.");
     while not correct_answer:
          for _ in range(chance):
               guess=int(input("Guess the number between 1 to 20="));
               if guess==comp:
                    print(f'You have guessed the correct number {comp}');
                    correct_answer=True;
                    break;
               elif guess<comp:
                    print(f'You have guessed the value less than random number.');
                    chance-=1;
                    print(f'You have now {chance} chances left');
                    if chance==0:
                         print(f'You have no chances left.The correct answer is {comp}');
                         break;
                    continue;
               elif guess>comp:
                    print(f'You have guessed the value greater than random number.');
                    chance-=1;
                    print(f'You have now {chance} chances left');
                    if chance==0:
                         print(f'You have no chances left.The correct answer is {comp}');
                         break;
                    continue; 
               else:
                    print(f'You have guessed the wrong number {guess}');
                    chance-=1;
                    print(f'You have now {chance} chances left');
                    if chance==0:
                         print(f'You have no chances left.The correct answer is {comp}');
                         break;
     print(f'Correct answer={comp}');      
main();