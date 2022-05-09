"""Import maybe package"""
from functional.maybe import Maybe,Just, Nothing

incr  = lambda x : x + 1
add = lambda x: lambda y: x + y

# def liftA2(f, fx, fy):
#     return fx.map(f).ap(fy)

liftA2 = lambda f: lambda fx: lambda fy: fx.map(f).ap(fy)

rst:Maybe = Just(incr).ap(Nothing())
print(rst)

rst = Just(incr).ap(Just(4))
print(rst)

rst = Just(add).ap(Just(4)).ap(Just(5))
print(rst)

rst = Just(add).ap(Just(4)).ap(Nothing())
print(rst)


rst = liftA2(add)(Just(4))(Just(5))
print(rst)

rst = liftA2(add)(Nothing())(Just(5))
print(rst)