from enum import Enum

class CanddleType(Enum):
    Second = 'seconds',
    Minute = 'minutes',
    Day = 'days',
    Week = 'weeks',
    Month = 'months',
    Year = 'years'