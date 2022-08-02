import Data.Char
import Data.List (insertBy)
inRange x y xs 
    | y<x = []
inRange x y [] = []
inRange x y (x':xs) = if x < y then x' : inRange (x+1) y xs else inRange x (y-1) xs
 
countPositives [] = 0   
countPositives (x:xs) = if x > 0 then 1+ countPositives xs else countPositives xs

r [] = []
r (x:xs) = r xs ++ [x]

c [] = []
c [x] = [toUpper x]
c (x:xs) = toLower x : c xs

captalisation xs =r(c (r xs))

title [] = []
title [x] = [captalisation x]
title (x:xs) = if length x >3 then captalisation x :title xs else x : title xs
-- how to recurse opposite of a list

insert x [] = [x]
insert x (y:ys) = if x <= y then x:y:ys else y : insert x ys
isort [] = []
isort (x:xs) = insert x (isort xs)

merge [] ys = ys
merge xs [] = xs
merge (x:xs) (y:ys) = if x<=y then x:merge xs (y:ys) else y:merge (x:xs) ys

msort [x] = [x]
msort xs = merge (msort (take n xs)) (msort (drop n xs))
    where n = length xs `div` 2

rotor n x = drop n x ++ take n x

--rotor 0 x = x
--rotor n [] = []
--rotor n x = rotor (n-1) (tail x) ++ [head x]    --tail reverse

makeKey n x = zip x (rotor n x)

lookUp s x = [y | (x',y) <- x, x'==s]

encipher n xs = [lookUp x (makeKey n ['A'..'Z']) | x <- xs]

normalise x = [toUpper x | x <- x, isAlpha x]

encipherStr n xs = [encipher n (normalise x) | x <- xs]