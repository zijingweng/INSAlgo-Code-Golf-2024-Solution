# Solution for [INSAlgo Code Golf 2024](https://github.com/INSAlgo/Code-Golf-2024)

The language used is [**05AB1E**](https://github.com/Adriandmen/05AB1E), a stacked based golfing language. Apart from the offical github [wiki](https://github.com/Adriandmen/05AB1E/wiki), these [tips](https://codegolf.stackexchange.com/questions/96361/tips-for-golfing-in-05ab1e) helped a lot to optimize the code. 

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

## [Day 2](https://github.com/INSAlgo/Code-Golf-2024/blob/main/2%20-%20palindromes/sujet.md): 8 bytes
```
A5ãʒÂQ}»
```
The code takes about a minute to run on my laptop.

Explanation:
```
A               # push "abcdefghijklmnopqrstuvwxyz"
 5ã             # cartesian power of 5, which yields ["aaaaa", "aaaab", "aaaac" ... "zzzzz"]
   ʒ  }         # keep only elements that
    Â           # itself and its reverse
     Q          # equals
       »        # join by newlines
                # implicit output
```

(Bonus) The following code is a byte longer but way faster : 
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

## [Day 4](https://github.com/INSAlgo/Code-Golf-2024/blob/main/4%20-%20alarme/sujet.md): 49 bytes
```
',¡12XǝYYǝU[N4*VX2EXXYN+èè}XYèD2›#i+ë*}XY3+èǝU]X¬
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
State machine with infinite loop, plus the final output
```
[... ...]       # infinite loop
    #           # break loop if true
         X¬     # get first element of X
                # implicit output
```
Calculate index `Y`
```
N               # current index of loop (0 to inf)
 4*             # times 4
   V            # assgin to variable Y
```
Calculate `code[code[Y+1]]` and `code[code[Y+2]]`
```
2E       }      # loop 2 times (N = 1 and 2)
        è       # get element of
  X             # X
       è        # at index    get element of
   X            #             X
    YN+         #             at index Y+N
```
Similarly, calculate `code[Y]` (duplicated for future use)
```
XYè             # calculate code[Y]
   D            # duplicate it
```
Break the loop if `code[Y] == 99`. Since `code[Y]` can only be 1, 2 or 99, we can use `code[Y] > 2`
```
  #             # break loop if
2›              # (a) > 2
```
Calculate sum or product according to `code[Y]`
```
i               # if code[Y] equals to 1 then
 +              # push (a) + (b)
  ë             # else
   *            # push (a) + (b)
    }           # endif
```
Finally, update `X`
```
X...            # the list that was put in the stack long ago
         ǝ      # replace element at index
    XY3+è       # code[code[Y+3]]
                # with (a)
          U     # assgin to variable X
```

## [Day 5](https://github.com/INSAlgo/Code-Golf-2024/blob/main/5%20-%20nenuphar/sujet.md): 52 bytes
```
|»¤1:U¯[DO©Žñá·Q#X®>èi1ªëX®Ƶû+èiƵûªëX0®ǝU¨]εi'Rë'D]»
```
Big thanks to [polo-diemunsch](https://github.com/polo-diemunsch) for the competition that forced me to come up with a new algorithm. 

The code again takes about a minute to run.

Explanation:  
Because we only have one input which has a solution with only right and down moves, the searching algorithm is simple. At each given position, we only need to search two neighboring cases, prioritising **right** over **down**. If we reach a deadend, we **modify the map**, changing current case to wall and go back one move.

In the implementation, I decided to save the map in a 1-dimensional list, adding 1 padding character between the lines. Because of the lack of variables and to shorten the code, I used a single variable to store the current position. We start at `0`. `current + 1` is the case to the right and `current + 351` is the case to the bottom. Our goal is at position `351*350-2 = 122848`. The interesting part is that if we store `1` as **right** and `351` as **down** in the list of directions, the current position can be calculated by the sum of the list. There is need to maintain the variable.   

Initialization
```
|               # input all
 »              # join by '\n' which makes the padding
  ¤             # get last character (#)
   1:           # replace all of them with 1
     U          # assgin to variable X
      ¯         # empty list (to store directions)
```
The main loop, calculate current position and exit statement
```
[         ...]  # infinite loop
        Q#      # break if the following two equals:
 DO             # sum of list (current position)
   ©            # (save to register_c)
    Žñá·        # 61424*2 = 122848
```
If the case to the right is road, we append `1` to the list
```
    i           # if
   è            # element of
X               # map at
 ®>             # case to the right
                # equals to 1 (road)
     1ª         # then append 1
```
Similarly, else if the case to the bottom is road, we append `351` to the list
```
ëX®Ƶû+èiƵûª     # Ƶû = 351
```
Else we are in a dead end, so we change the map and take one step back
```
ë               # else
    ǝ           # replace the element of
 X              # the map
   ®            # at current position
  0             # with 0
     U          # and save it to variable X
      ¨         # pop list (remove last step)
```
The following character `]` closes all if statements and the infinite loop. The only thing left is the output:
```
ε               # for each element of the list
 i              # if it equals to 1
  'R            # push 'R' as Right
    ë'D         # else push 'D' as Down
       ]        # close if and for statement
        »       # join by newlines
                # implicit output
```