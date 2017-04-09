# C89 expressions parsed with the shunting yard algorithm in Python

This is a proof of concept, incomplete and probably buggy implementation of
a parser for C89 expressions using the shunting yard algorithm.  Its goal is
to show how it is possible to parse the complex operators (conditional, function
calls, indexing).
  
Some things are voluntarily absent: 

- the casts.  One reason is that one need semantic feedback to parse C casts, for instance
`(a)-b` can be the cast of a negation or a substraction.
 
- some irregularities in the grammar are left to the next pass to check.  For instance 
assignment operators in C89 have an unary expression as left operand.  The code has no
issue in parsing `a+b=c`.  Similarly the code will parse `a.(36+6)`.

Some things have been added, mostly to be closer to 
[Andy Chu's Pratt parsing demo](https://github.com/andychu/pratt-parsing-demo.git)
which triggered me into making this example and whose tests I've reused.

- an operator ** with right to left associativity
