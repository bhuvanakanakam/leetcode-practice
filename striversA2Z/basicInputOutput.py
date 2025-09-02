// Complete the function printNumber which takes an integer input from the user and prints it on the screen.
// Input(user gives value): 7
// Output: 7

class Solution:
  def printNumber(self):
    number = input();
    // have to convert the number to int, because the input() takes string by default
    integerNumber = int(number)
    print(integerNumber);
