main :: IO ()
main = do
  putStrLn "Hello, world!"

  i <- readFile "hello.txt"
  putStrLn i
