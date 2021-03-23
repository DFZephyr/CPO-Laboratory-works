# CPO-Laboratory-works1
## https://github.com/DFZephyr/CPO-Laboratory-works1
### title:CPO-Laboratory-works1

### group name:BIGBANG

### group members:Zhang Dengfeng,Yu Jie

### laboratory work number: 1

### variant description:
    Set based on hash-map (collision resolution: separate chaining, link)
    You can use the built-in list for storing buckets and a bucket itself
    You need to check that your implementation correctly works with None value
### Synopsis:
    This Lab mainly contains two parts, the writing of Hashmap library and the correctness test of the library
#### Contribution summary:
    Zhang Dengfeng complete the mutable version hashmap and Testmutablehashmap
    Yu Jie complete the immutable version hashmap and Testimmutablehashmap
    
#### Explanation of taken design decisions and analysis:
    The library mainly contains two parts, one is a mutable object part, and the functions in it will change the source hashmap.  
    The main operations included in this part are adding, searching, deleting, converting to an array, etc. 
    The other part is the immutable object part, mainly including adding , Delete, merge and other operations.
    
#### Work Demonstration:
    The test file is saved in the src.All you need to do is run it in pycharm.
#### Conclusion:
    First of all, in this lab, I felt many problems that need to be considered as a library developer. 
    An excellent container library should support both types of functions of variable objects and immutable objects. 
    Function, which really helped us to detect many problems, we also learned to use Hypothesis library to do the test
