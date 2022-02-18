from ctypes import *

class mCfgNodeLib(Structure):
    pass

mCfgNodeLib._fields_ = [
        ('segmentNum', c_uint16),
        ('startBus', c_uint8),
        ('endBus', c_uint8),
        ('mcfgBaseLow', c_uint32),
        ('mcfgBaseHigh', c_uint32),
        ('next', ctypes.POINTER(mCfgNodeLib))
    ]

class deviceData(Structure):
    _fields_ = [
        ('pcinode', ctypes.POINTER(mCfgNodeLib)),
        ('hDev', c_void_p),
        ('libVer', c_uint32),
        ('drvVer', c_uint32),
        ('memPhysAddrLow', c_uint32),
        ('memPhysAddrHigh', c_uint32)
    ]

devHandle = pointer(deviceData)
