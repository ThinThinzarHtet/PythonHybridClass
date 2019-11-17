import fibo

fibo.fib(10)

f = fibo.fib
f(100)

fibo.fib(10000)

from fibo import fib, fib2

f = fibo.fib2(500)
print(f)

from fibo import *
fib(500)

import fibo as fi
fi.fib(500)

from fibo import fib as fibonacci
fibonacci(500)