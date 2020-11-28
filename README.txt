Ever gotten tired of having to type more than one letter when coding? Yeah not me either, but in Triple-A you code with only variations of the letter A.



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


EXAMPLE
äAaAa åa AAA // let AaAa = 7
äaaa åa åAaA ÅAaA // let aaa = input() // Here the call operator is before the function because there are no arguments

Ãa äAaAa åAaAaa ãaÁäaaaÀ // if AaAa < num(aaa)
    ÅAaa åAaA ÁãaAÁäAaAaÀ åA ÄaaAaaaaa aAAaAaaA aAAAaaAA aaAaaaaa aAAaAAaa aAAaaAaA aAAAaaAA 
                         aAAAaaAA aaAaaaaa aAAAaAaa aAAaAaaa aAAaaaaA aAAaAAAa aaAaaaaaÄ åA äaaa À // print(string(AaAa) + " is less than " + aaa)

If you copy paste this code and try to run it it wont. 
Thats because there are non A characters. So if you want to run this you will have to remove the "comments" behind the // symbols.