# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add("Twitter")
print(it_companies)

others_companies = {"Meta", "Oracle"}
it_companies.update(others_companies)
print(it_companies)

guardado = it_companies.remove("Facebook")
print(guardado)
print(it_companies)

print(it_companies.discard("IBM"))
print(it_companies)

print(A)
print(B)

a_b = A.union(B)
print(a_b)

interA_B = A.intersection(B)
print(interA_B)