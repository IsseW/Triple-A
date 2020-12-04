Ever gotten tired of having to type more than one letter when coding? Yeah not me either, but in Triple-A you code with only variations of the letter A.

This is a language i made in a couple days. Expect bugs and don't expect it to be fast.

If you want to try using this language. Clone this repository and run the interpreter.exe in ./dist/interpreter on the aaa code. If you want syntax highlighting in vs code clone https://github.com/IsseW/aaa-extention and open it in vs code. Then press F5 to start debugging and a new vs code window will open with an extention to highlight AAA code.


Just some info about the language. Mostly for me so that I dont forget.
replace X for either A or a

GENERAL
Â - .
Á - (
À - )
Scopes are based on the current indent

TYPES
ãa - number
ãaA - string
ãaa - function
ãaaaA - member function
ãaaa - list
ãaaA - dictionary

CONSTANTS:
XXXXXX for number, presented in binary where A = 1 and a = 0
ÄXXXXXXXXX XXXXXXXXÄ for string where A = 1 and a = 0 and they are in groups of 8 to present ascii characters in binary.

Á[anything]â[anything]â[anytihng]....À - list with arbitrary length
ÁâÀ - empty list
Á[anything]âÀ - list with one element

VARIABLE
äXXXXX - any type

OPERATORS
åa - assign
åaåXXXX - operation assign
åA - add
åAa - sub or negate
åAA - mul
åAAa - div
åAAA - pow
åAAAa - root
åAaa - bool not
åAaaa - bool and
åAaaA - bool or
åAAaa - bitwise not
åAAaaa - bitwise and
åAAaaA - bitwise or
åAAaaAa - botwise xor

åAaAa - equal
åAaAaa - less than
åAaAaaa - less or equal
åAaAaA - greater than
åAaAaAa - greater or equal

åAaA - function call
åAaAA - index collection

KEYWORDS
Ãa - if
ÃA - function
ÃaaA - return
Ãaa - else if
Ãaaa - else
ÃaA - label
ÃaAa - goto label

BUILTIN FUNCTIONS
ÅAaa - standard out
ÅAaA - standard in
ÅAaaa - read from file
ÅAaaA - write to file


EXAMPLE
äAaAa åa AAA // let AaAa = 7
äaaa åa åAaA ÅAaA // let aaa = input() // Here the call operator is before the function because there are no arguments

Ãa äAaAa åAaAaa ãaÁäaaaÀ // if AaAa < num(aaa)
    ÅAaa åAaA ÁãaAÁäAaAaÀ åA ÄaaAaaaaa aAAaAaaA aAAAaaAA aaAaaaaa aAAaAAaa aAAaaAaA aAAAaaAA 
                         aAAAaaAA aaAaaaaa aAAAaAaa aAAaAaaa aAAaaaaA aAAaAAAa aaAaaaaaÄ åA äaaa À // print(string(AaAa) + " is less than " + aaa)

If you copy paste this code and try to run it it wont. 
Thats because there are non A characters. So if you want to run this you will have to remove the "comments" behind the // symbols.