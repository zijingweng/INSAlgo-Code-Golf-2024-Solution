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

## Day 1: 4 bytes
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
т       # Push 100
 Åp     # Produces a list of the first (a) primes
   »    # Join by newlines
        # Implicit output
```

## Day 2: 9 bytes
```
A3ãεÂ¦«}»
```
Explanation:
```
A           # Push "abcdefghijklmnopqrstuvwxyz"
 3ã         # Cartesian power of 3, which yields ["aaa", "aab", "aac" ... "zzz"]
   ε   }    # For each element do
    Â       # Bifurcate (push reverse to stack)
     ¦      # Tail (remove the first element)
      «     # Concatenate
        »   # Join by newlines
            # Implicit output
```

## Day 3: 23 bytes
```
18L18ªX3Ý·.ΛX„[]:ð„  .:
```
Explanation:
```
18L18ªX3Ý·.ΛX„[]:ð„  .:
```