module Coursework where
{-
  Your task is to design a datatype that represents the mathematical concept of a (finite) set of elements (of the same type).
  We have provided you with an interface (do not change this!) but you will need to design the datatype and also 
  support the required functions over sets.
  Any functions you write should maintain the following invariant: no duplication of set elements.

  There are lots of different ways to implement a set. The easiest is to use a list
  (as in the example below). Alternatively, one could use an algebraic data type, or 
  wrap a binary search tree.
  Extra marks will be awarded for efficient implementations if appropriate.

  You are NOT allowed to import anything from the standard library or other libraries.
  Your edit of this file should be completely self-contained.

  DO NOT change the type signatures of the functions below: if you do,
  we will not be able to test them and you will get 0% for that part. While sets are unordered collections,
  we have included the Ord constraint on most signatures: this is to make testing easier.

  You may write as many auxiliary functions as you need. Please include everything in this file.
-}

{-
   PART 1.
   You need to define a Set datatype. Below is an example which uses lists internally.
   It is here as a guide, but also to stop ghci complaining when you load the file.
   Free free to change it.
-}

-- you may change this to your own data type
data Set a = EmptySet | Node a (Set a)(Set a) deriving (Show,Read) --Eq
{-
   PART 2.
   If you do nothing else, at least get the following two functions working. They
   are required for testing purposes.
-}

-- toList {2,1,4,3} => [1,2,3,4]
-- the output must be sorted.
toList :: Set a -> [a]
toList EmptySet = []
toList (Node a left right) = toList left ++ [a] ++ toList right 



-- fromList [2,1,1,4,5] => {2,1,4,5}
fromList :: Ord a => [a] -> Set a
fromList = foldr insert EmptySet

{-
   PART 3.
   Your Set should contain the following functions.
   DO NOT CHANGE THE TYPE SIGNATURES.
-}

-- test if two sets have the same elements.
instance (Ord a) => Eq (Set a) where
  s1 == s2 = toList s1 == toList s2 


-- the empty set
empty :: Set a
empty = EmptySet


-- Set with one element
singleton :: a -> Set a
singleton x = Node x EmptySet EmptySet


-- insert an element of type a into a Set
-- make sure there are no duplicates!
insert :: (Ord a) => a -> Set a -> Set a
insert x EmptySet = singleton x
insert x (Node a left right)
    | x == a = Node x left right
    | x < a = Node a (insert x left) right
    | x > a = Node a left (insert x right)


-- join two Sets together
-- be careful not to introduce duplicates.
union :: (Ord a) => Set a -> Set a -> Set a
union EmptySet EmptySet = EmptySet
union EmptySet (Node b left2 right2) = Node b left2 right2
union (Node a left1 right1) EmptySet = Node a left1 right1
union (Node a left1 right1) (Node b left2 right2) 
    | a == b = insert a (union (union left1 left2) (union right1 right2))
    | a > b = insert a (union (union left1 left2) (insert b (union right1 right2)))
    | a < b = insert b (union (insert a (union left1 left2)) (union right1 right2))
    -- let list = toList (Node a left1 right1) ++ toList (Node b left2 right2)
    -- in foldr insert EmptySet list

-- return the common elements between two Sets
-- still one delete
delete :: Ord a => a -> Set a -> Set a 
delete x (Node a l1 r1) = fromList ([y|y <- toList (Node a l1 r1),y/=x])
delete x EmptySet = EmptySet

intersection :: (Ord a) => Set a -> Set a -> Set a
intersection _ EmptySet = EmptySet
intersection EmptySet _ = EmptySet
intersection (Node a l1 r1) (Node b l2 r2) = if member a (Node b l2 r2) 
                                             then insert a $intersection (union l1 r1) (delete a (Node b l2 r2))
                                             else intersection (union l1 r1) (Node b l2 r2)
-- all the elements in Set A *not* in Set B,
-- {1,2,3,4} `difference` {3,4} => {1,2}
-- {} `difference` {0} => {}
difference :: (Ord a) => Set a -> Set a -> Set a
difference (Node a l1 r1) EmptySet = Node a l1 r1
difference EmptySet (Node b l2 r2) = EmptySet
difference EmptySet EmptySet = EmptySet
difference (Node a l1 r1) (Node b l2 r2) = if member a (Node b l2 r2)
                                           then difference (union l1 r1) (Node b l2 r2)
                                           else insert a $difference (union l1 r1) (delete a (Node b l2 r2)) 


-- is element *a* in the Set?
member :: (Ord a) => a -> Set a -> Bool
member x EmptySet = False 
member x (Node a left right) 
    | x == a = True
    | x < a = member x left
    | x > a = member x right


-- how many elements are there in the Set?
cardinality :: Set a -> Int
cardinality EmptySet = 0
cardinality (Node a l1 r1) = cardinality l1 + cardinality r1 + 1

setmap :: (Ord b) => (a -> b) -> Set a -> Set b
setmap f EmptySet = EmptySet
setmap f (Node a l1 r1) = Node (f a) (setmap f l1) (setmap f r1)


setfoldr :: (a -> b -> b) -> Set a -> b -> b
setfoldr f EmptySet base = base
setfoldr f  (Node a l1 r1) base = f a (setfoldr f l1 acc)
    where acc = setfoldr f r1 base

-- powerset of a set
-- powerset {1,2} => { {}, {1}, {2}, {1,2} }

{-
insert2 (Node x EmptySet EmptySet) EmptySet = Node (Node x EmptySet EmptySet) EmptySet EmptySet
insert2 (Node x l2 r2) (Node (Node a1 ll1 rr1) l1 r1)
    | x == a1 = Node (Node x l2 r2) l1 r1
    | x < a1 = Node (Node a1 ll1 rr1) (insert2 (Node x l2 r2) l1) r1
    | x > a1 = Node (Node a1 ll1 rr1) l1 (insert2 (Node x l2 r2) r1)
from2List [] = EmptySet
from2List (x:xs) = insert2 (fromList x) (from2List xs)
powerList [] = [[]]
powerList (x:xs) = [z | y <- powerList xs, z <- [y,x:y]]  
-}
powerSet :: Set a -> Set (Set a)
powerSet = undefined



-- cartesian product of two sets
insert' :: t -> Set t -> Set t
insert' x EmptySet = Node x EmptySet EmptySet
insert' x (Node a left right) = Node a (insert' x left) right
insert'' :: (a, b) -> Set (a, b) -> Set (a, b)
insert'' (x,y) EmptySet = Node (x,y) EmptySet EmptySet
insert'' (x,y) (Node a left right) = Node a (insert'' (x,y) left) right
union' :: Set t -> Set t -> Set t
union' EmptySet EmptySet = EmptySet
union' EmptySet (Node b left2 right2) = Node b left2 right2
union' (Node a left1 right1) EmptySet = Node a left1 right1
union' (Node a left1 right1) (Node b left2 right2) = Node a (union' left1 left2) (insert' b (union' right1 right2))
cartesian :: Set a -> Set b -> Set (a, b)
cartesian = undefined 


-- partition the set into two sets, with
-- all elements that satisfy the predicate on the left,
-- and the rest on the right
ans1 :: (t -> Bool) -> Set t -> Set t
ans1 f EmptySet = EmptySet
ans1 f (Node a l1 r1) = if f a 
                        then Node a (ans1 f l1) (ans1 f r1)
                        else ans1 f (union' l1 r1)
ans2 :: (t -> Bool) -> Set t -> Set t
ans2 f EmptySet = EmptySet
ans2 f (Node a l1 r1) = if not(f a)
                        then Node a (ans2 f l1) (ans2 f r1)
                        else ans2 f (union' l1 r1) 

partition :: (a -> Bool) -> Set a -> (Set a, Set a)
partition f (Node a l1 r1) = (ans1 f (Node a l1 r1),(ans2 f (Node a l1 r1)))


{-
   On Marking:
   Be careful! This coursework will be marked using QuickCheck, against Haskell's own
   Data.Set implementation. Each function will be tested for multiple properties.
   Even one failing test means 0 marks for that function.

   Marks will be lost for too much similarity to the Data.Set implementation.

   Pass: creating the Set type and implementing toList and fromList is enough for a
   passing mark of 40%.

-}
