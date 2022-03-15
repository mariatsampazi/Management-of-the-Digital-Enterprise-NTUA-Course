from scipy import spatial

query = [0.0969, 0.2218, 0.3979]

#movie 1
movie1 = [0.0969, 0.6654, 1.1937]
result = 1 - spatial.distance.cosine(query, movie1)
print(round(result,4))

#movie 2
movie2 = [0, 0.4436, 0]
result = 1 - spatial.distance.cosine(query, movie2)
print(round(result,4))

#movie 3
movie3 = [0.0969, 0.6654, 0]
result = 1 - spatial.distance.cosine(query, movie3)
print(round(result,4))

#movie 4
movie4 = [0.1938, 0, 0.7958]
result = 1 - spatial.distance.cosine(query, movie4)
print(round(result,4))

#movie 5
movie5 = [0.2907, 0, 0]
result = 1 - spatial.distance.cosine(query, movie5)
print(round(result,4))


