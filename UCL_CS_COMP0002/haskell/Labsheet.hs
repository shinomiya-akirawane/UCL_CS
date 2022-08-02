import Data.Char
square x=x*x
pyth x y = square x + square y
isTriple x y z = pyth x y == square z
isTripleAny x y z = isTriple x y z || isTriple x z y || isTriple y z x
halfEvens xs = [if even x then div x 2 else x | x <- xs]
inRange a b xs=[x | x <- xs, x>=a, x<=b]
countPositives xs = length [x | x <- xs, x>0]
capitalised xs = [if isUpper x then toLower x else x | x <- xs]
title xs = [if length x >=4 then upperWord x else capitalised x | x <- xs]
upperWord [] = error "Empty string"
upperWord (s:l) = toUpper s : [toLower x | x <- l]