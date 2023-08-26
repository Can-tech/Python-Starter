age: int
int: str
height: float
is_human: bool

#We can pre define the types and the return types.
def police_check(age:int) -> bool:
    if age > 10:
        can_drive = True
    else:
         can_drive = False
    return can_drive
