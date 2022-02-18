from ctypes import *

class mCfgNodeLib(Structure):
    pass

mCfgNodeLib._fields_ = [
        ('segmentNum', c_uint16),
        ('startBus', c_uint8),
        ('endBus', c_uint8),
        ('mcfgBaseLow', c_uint32),
        ('mcfgBaseHigh', c_uint32),
        ('next', POINTER(mCfgNodeLib))
    ]

class deviceData(Structure):
    _fields_ = [
        ('pcinode', POINTER(mCfgNodeLib)),
        ('hDev', c_void_p),
        ('libVer', c_uint32),
        ('drvVer', c_uint32),
        ('memPhysAddrLow', c_uint32),
        ('memPhysAddrHigh', c_uint32)
    ]

devHandle = POINTER(deviceData)

# Step one, create deviceData structure with some data on it
structure_deviceData = deviceData()
structure_deviceData.libVer = 9

# Step two, create pointer to above structure.
devHandle2 = pointer(structure_deviceData)

# Step 3, extract data from the pointer with contents
print(devHandle2.contents.libVer) # it should print 9

# In conclusion, our problem was the devHandle pointer:
# devHandle = POINTER(deviceData)
# this line above will create a pointer to the class
# but we needed a pointer to the instance in order to
# read the pointer's content that C Driver was populating.
# If we solve this, driver might interact via the structures.
"""
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
>>> devHandle.contents
<attribute 'contents' of '_ctypes._Pointer' objects>
>>> devHandle.contents.libVer
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'getset_descriptor' object has no attribute 'libVer' <--- This was our legacy issue, now solved!
"""







