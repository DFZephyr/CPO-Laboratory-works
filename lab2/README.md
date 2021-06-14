CPO-lab2
----

#### 1.Title: Computational Process Organization Lab2

#### 2.Group Member: Jie Yu,Dengfeng Zhang

#### 3.Group Name: BIGBANG

#### 4.Date： 2020 .06.14

#### 5.Variant description: Regular expression
          • Sub variants define which construction you should support:
               \w, \s, \d, \, ^, ., $, *, +, ?, |, ( ), \1, \2, \n.
          • Support functions: match, search, sub, split.
          • Visualization as a finite state machine (state diagram and table).
          • You should use default Python logging module to make interpreter work transparent.
          • Should provide complex examples such as a time parsing, JSON parsing and so on.
#### 6.Synopsis:We use the NFA way to write our regular expression state machine, first perform the lexical analysis of the expression, then use the bottom-up method for grammatical analysis, and then establish NFA, and finally used to match the string.

#### 7.Contribution Summary:Dengfeng Zhang's main contribution is in the grammatical analysis and the establishment of NFA, Jie Yu's main contribution is in the lexical analysis and testing
