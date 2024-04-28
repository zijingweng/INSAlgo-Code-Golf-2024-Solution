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

## [Day 5](https://github.com/INSAlgo/Code-Golf-2024/blob/main/5%20-%20nenuphar/sujet.md): 84 bytes
```
0UƵûV|YLª»©\[XŽñá·Q#Y1‚εX+®rè'#Q}JCDÉiX>UëD<iXY+Uë[DÍi<XY+U1#}<iXY-UëX<U]JεÉi'Rë'D]»
```
The code again takes about a minute to run. A logically similar code `5.py` is first written in python that is way more readable.

Explanation:  
Because we only have one input which has a single solution, with only right and down moves, the searching algorithm is really simple. At each given position, we only need to look the cases on the right and bottom. If only one of them is `#`, we save the direction in `stack` and move there. If both of them are `#`, we save this information in `stack` and go **right**. If none of them are `#`, it is safe to say that we are on the wrong path, so we go back to the last crossroad (by poping `stack`) and go **down** this time.

To simplify the problem, I decided to add 1 paddings at the right and bottom edge of the map, making it `351 * 351`. Because of the lack of variables and to shorten the code, I used a single variable `X` to store the current position. We start at `0`. `X+1` is the case to the right and `X+351` is the case to the bottom. Our goal is at position `351*350-2 = 122848`.

Initialization of input
```
0U              # assgin 0 to variable X (current position)
  ƵûV           # assgin 351 to variable Y
     |          # input all
      YLª       # put dummy numbers [1, 2 ... 351] as bottom padding
         »      # join by '\n' which makes the right padding
          ©     # save the map to register_C
           \    # remove map from the stack
```
The main loop and exit statement
```
[        ...]   # infinite loop
      Q#        # break if the following two equals:
 X              # current position
  Žñá·          # 61424*2 = 122848
```
We use `flag` to store the information of this position, which can be seen as a binary number, stored in a list. The greater bit represents if the case to the bottom is `#`, and the lower bit checks the case to the right.
```
   ε        }   # for each element in the
Y1‚             # list [351, 1] (down, right) do:
       rè       # get
    X+          # next positon
      ®         # of the map (retrived from register_c)
         '#Q    # if it equals to '#' push 1 else 0
```
We can now check the flag. if `flag == 1` (only right is `#`) or `flag == 3` (both right and down are `#`), or in other words if `flag` is odd, we go the right. 
```
JC                # convert binary list to integer (flag)
  D               # duplicate the flag
   Éi             # if it is odd
     X>U          # assign X with X+1 (go right)
```
Else if `flag == 2` we go down.
```
ë               # else
 D              # duplicate the flag
  <i            # if flag - 1 == 1
    XY+U        # assign X with X+351 (go down)
```
Else `flag` must be `0` which means we have to go back.
```
ë               # else
 [...]          # infinite loop
```
If we find a `3` which is a crossroad, we go down this time. Note that we didn't go left here because it is already done when visiting `0` (explained later). 
```
D               # duplicate the current flag
 Íi        }    # if flag - 2 == 1
   <            # assign flag with 2
    XY+U        # assign X with X+351 (go down)
        1#      # break the loop
```
If we find a `2` we go up.
```
<i              # if flag - 1 == 1
  XY-U          # assign X with X-351 (go up)
```
Else it must be `1` where we have to go left, or `0`. The `0` is always visited once, and instead of going left once on the crossroad (`3`), we can go left here, to save a few bytes.
```
ë               # else
 X<U            # assign X with X-1 (go left)
```
The following character `]` closes all if statements and two infinite loops. The only thing left to do is the output. Instead of replacing characters, I found that using an if statement is 1 byte shorter. 
```
J               # join the stack as a single string
 ε              # for each character of the string
  Éi            # if it is odd (1 or 3)
    'R          # push 'R' as Right
      ë'D       # else push 'D' as Down
         ]      # close if and for statement
          »     # join by newlines
                # implicit output
```