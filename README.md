# ctypes
ctypes

The idea of this repository is to learn from ctypes and the way we can create and populate the structures.

# no lo pierdas

It is the starting file from where we want to understand how to populate and print the structures once populated.
Notice this is a Python Project and the idea is to connect this structures to a C Driver, but that is private part.

# Solution
```py
# Create a pointer to the instance of the structure class
devHandle2 = pointer(structure_deviceData)
```
```sh
>>> devHandle2 = pointer(structure_deviceData)
>>> 
>>> 
>>> 
>>> devHandle2
<__main__.LP_deviceData object at 0x100d11cc0> <---- Notice this is an instance
>>> 
>>> 
>>> 
>>> devHandle
<class '__main__.LP_deviceData'>     <----- Notice this is a class
>>> 
>>> 
>>> 
>>> devHandle2.contents
<__main__.deviceData object at 0x100d2ed40> <---- Still an instance
>>> devHandle2.contents.libVer
9
>>> print(devHandle2.contents.libVer) # it should print 9
9 <--- It did, nice it work this way!!!
```

# Problem
```py
# Created a pointer to the class of the structure
devHandle = POINTER(deviceData)
```
```sh
>>> devHandle.contents
<attribute 'contents' of '_ctypes._Pointer' objects>
>>> devHandle.contents.libVer
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'getset_descriptor' object has no attribute 'libVer' <--- This was our legacy issue, now solved!
```
