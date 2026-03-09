from typing import List

class Result:
    def __init__(self, mX, mY, mMoveDistance, mRideDistance):
        self.mX = mX
        self.mY = mY
        self.mMoveDistance = mMoveDistance
        self.mRideDistance = mRideDistance

def init(N : int, M : int, L : int, mXs : List[int], mYs : List[int]) -> None:
    pass

def pickup(mSX : int, mSY : int, mEX : int, mEY : int) -> int:
    return -1

def reset(mNo : int) -> Result:
    return Result(-1, -1, -1, -1)

def getBest(mNos : List[int]) -> None:
    pass