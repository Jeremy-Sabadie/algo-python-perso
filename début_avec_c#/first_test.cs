using System;

class Program {
  // This is a single line comment

/* This is a multi-line comment
   and continues until the end
   of comment symbol is reached */
  public static void Main (string[] args) {
    //Vprint text:
//_1Console.WriteLine()
    Console.WriteLine ("Hello World!");
  //_2Variable and data type
    string foo = "Hello";
//_3string bar = "How are you?";
int x = 5;
int y = 3;
Console.WriteLine(foo);//_1 Prints: Hello
//_4 Prints: Hello
    Console.WriteLine("the resul of "+x+" + "+y+" is: "+(x+y));//_2Prints: 8
//_5Math.Sqrt()
int i=81;
Console.WriteLine("racine carré de "+ i +" est = "+Math.Sqrt(i));//_4Prints: 9
  
//_6Math.Pw
    int b =5;
    Console.WriteLine(Math.Pow(b,2));//Prints: =25(5^2)

   string str = "Divyesh"; 

// Finding the index of character  
// which is present in string and 
// this will show the value 5 
int index1 = str.IndexOf('h');

Console.WriteLine("The Index Value of character 'h' in "+str+" is: " + index1);
    Console.Write(index1+" is also the number of characters in the word");