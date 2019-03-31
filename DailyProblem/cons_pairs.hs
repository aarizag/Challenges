
cons :: Int -> Int -> (Int -> Int -> Int)
cons a b = \f -> f a b

car :: (Int -> Int -> Int) -> Int
car pair = pair (\a b -> a)

cdr :: (Int -> Int -> Int) -> Int
cdr pair = pair (\a b -> b)

