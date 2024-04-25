# Solution for [INSAlgo Code Golf 2024](https://github.com/INSAlgo/Code-Golf-2024)

The language used is [**05AB1E**](https://github.com/Adriandmen/05AB1E), a stacked based golfing language. 

To run code with `osabie encoding`, you might need to change the **05AB1E** source code:  
```elixir
# Line 72 of 05AB1E/lib/reading/reader.ex
# change this
    {_, file} = :file.(file_path, [:read, :binary])
# to this
    {_, file} = File.(file_path, [:read, :binary])
```
and rebuild **05AB1E**. This might be a bug related to operating systems or Elixir and Erlang versions. **05AB1E** is not maintained as the last commit was in 2022.

To convert code from `utf-8` to `osabie encoding`, reference `codebase_convertor.py`

## [Day 1](https://github.com/INSAlgo/Code-Golf-2024/blob/main/1%20-%20premiers/sujet.md): 4 bytes
```
тÅp»
```
To run the `utf8` file, use command:
```
escript path_to/osabie 1utf8.05AB1E
```
Alternatively, to run the `osabie encoded` file, use command:
```
escript path_to/osabie -c 1.05AB1E
```
Explanation:
```
т               # push 100
 Åp             # produces a list of the first (a) primes
   »            # join by newlines
                # implicit output
```

## [Day 2](https://github.com/INSAlgo/Code-Golf-2024/blob/main/2%20-%20palindromes/sujet.md): 9 bytes
```
A3ãεÂ¦«}»
```
Explanation:
```
A               # push "abcdefghijklmnopqrstuvwxyz"
 3ã             # cartesian power of 3, which yields ["aaa", "aab", "aac" ... "zzz"]
   ε   }        # for each element do
    Â           # bifurcate (push reverse to stack)
     ¦          # tail (remove the first element)
      «         # concatenate
        »       # join by newlines
                # implicit output
```

## [Day 3](https://github.com/INSAlgo/Code-Golf-2024/blob/main/3%20-%20spirale/sujet.md): 23 bytes
```
18L18ªX3Ý·.ΛX„[]:ð„  .:
```
Explanation:  
First create a one-caracter wide spiral like this: 
```
111111111111111111
1                1
1 11111111111111 1
1 1            1 1
1 1 1111111111 1 1
1 1 1        1 1 1
1 1 1 111111 1 1 1
1 1 1 1    1 1 1 1
1 1 1 1 11 1 1 1 1
1 1 1 1  1 1 1 1 1
1 1 1 1111 1 1 1 1
1 1 1      1 1 1 1
1 1 11111111 1 1 1
1 1          1 1 1
1 111111111111 1 1
1              1 1
1111111111111111 1
                 1
```
The following code is inspired by [this](https://codegolf.stackexchange.com/a/167486)
```
          .Λ    # (output to string) Draw lines of length:
18L             #     [1, 2 ... 18]
   18ª          #     append another 18 to list
                # with caracter(s):
      X         #     value of X variable (defaults to 1)
                # in the direction of:
       3Ý       #     [0, 1, 2, 3]
         ·      #     times 2 = [0, 2, 4, 6]
```
Then we just need to replace the caracters
```
    :           # replace recursively
X               # value of X variable (defaults to 1)
 „[]            # with 2-char string "[]"
         .:     # replace all
     ð          # whitespace
      „         # with 2-char string "  "
                # implicit output
```

## [Day 4](https://github.com/INSAlgo/Code-Golf-2024/blob/main/4%20-%201202%20Program%20Alarm/sujet.md): 58 bytes
```
',¡12XǝYYǝU[N4*VXÐYÌèèXXY>èèXYèD99Q#Θi+}.g3Qi*}XY3+èǝU]X¬,
```
To run with input file, use either one:
```
escript path_to/osabie 4utf8.05AB1E < 4input.txt
escript path_to/osabie -c 4.05AB1E < 4input.txt
```
Explanation:  
Initialization of input
```
                # implicit input
  ¡             # parse with
',              # character ','
      ǝ         # replace element at index
     X          # value of X variable (defaults to 1)
   12           # with 12
         ǝ      # replace element at index
        Y       # value of Y variable (defaults to 2)
       Y        # with value of Y variable
          U     # assgin to variable X (now X stores the code as a list of integers)
```
State machine with infinite loop
```
[... ...]       # infinite loop
    #           # break loop if true
           ,    # print
         X¬     # first element of X
```
Calculate index `Y`
```
N               # current index of loop (0 to inf)
 4*             # times 4
   V            # assgin to variable Y
```
Calculate `code[code[Y+2]]`
```
     è          # get element of
X               # X
    è           # at index    get element of
 X              #             X
  YÌ            #             at index Y+2
```
Similarly, calculate `code[code[Y+1]]` and `code[Y]` (duplicated for future use)
```
XXY>èè          # calculate code[code[Y+1]]
      XYè       # calculate code[Y]
         D      # duplicate it
```
Break the loop if `code[Y] == 99` (consumes `code[Y]`)
```
   #            # break loop if
99Q             # (a) equals to 99
```
Calculate sum if `code[Y] == 1` (consumes `code[Y]`)
```
 i              # if
Θ               # (a) equals to 1
  +             # then push (a) + (b)
   }            # endif
```
Calculate product if `stack_size == 3` which means `code[Y] == 2`
```
    i           # if
.g              # stack_size
  3Q            # equals 3
     *          # then push (a) * (b)
      }         # endif
```
Finally, update `X`
```
X...            # the list that was put in the stack long ago
         ǝ      # replace element at index
    XY3+è       # code[code[Y+3]]
                # with (a)
          U     # assgin to variable X
```
Note that in the final version `XXX` is replaced by `XÐ` to save a byte. 

## [Day 5](): ?? bytes