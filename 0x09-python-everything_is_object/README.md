# 0x09 Python Everything is Objet

## Introduction

This is the right thing to do in python right
```
>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
>>>
```
But look: 
```
>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'X'
>>> m
['X', 2, 3]
>>>
```

What is happening?
