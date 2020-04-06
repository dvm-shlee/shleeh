import enum


@enum.unique
class DataType(enum.Enum):
    PVDATASET = 1
    NIFTI1 = 2
    NSX = 3
    NEV = 4
    NWB = 5
