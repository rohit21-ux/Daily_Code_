# Python Memory Model and Mutability

1. What is an object in python ?
- Everything in python is an object 
  An object has : Identity , Type , Value

2. What does a python variable stores?
-  A variable stores a reference to an object, not the actual value

3. Where are python objects stored?
-  Objects are stored in heap memory.
   Variables live in stack frames but store refrences .

4. What is the difference between assignment and mutation?
-  Assignment changes reference 
   Mutation changes the object itself

5. What are mutable and immutable objects?
-  Mutable : list , dict , set (we can change or modify the object )
   Immuatble : int , float , str , tuple

6. Explain difference between  ==  amd is .
-  "==" compares values
   "is" compares memory identity.

7. What is shallow copy?
-  Creates new outer container but keeps  references to inner objects.
ex - b = a.copy

8. What is deep copy?
-  Creates new outer container and recursively copies inner objects.
ex - import copy
     b = copy.deepcopy(a)

9. Why is .copy() shallow by default?
-  For performance and memory efficiency.
   Deep copying everythin would be expensive.

10. What happens when you reassign a variable?
-  The reference changes to a new object.
   The old object may get garbage collected if no references remain.
   