# Python - Higher level programming

### Learning Objectives
* *How python works with diffrent type of objects?*

#### Exemple
```>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```
is diffrent from

```>>> b
[5, 6, 7]
>>> id (b)
140714363782656
>>> b = b + [4]
>>> id(b)
```
The expression `a += [4]` keeps the id of the object list ` a `
while `a = a + [4]` changes it.