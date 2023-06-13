""" 
Towers of Hanoi
Demonstarion of Recursion
"""

# %% Function


def hanoi(disks=3, from_tower=1, to_tower=3, alt_tower=2):
    """Prints out steps to move Towers

    Args:
        disks (int): No. of Towers. Defaults to 3.
        from_tower (int, optional): Original tower of all disks. Defaults to 1.
        to_tower (int, optional): Final tower of all disks. Defaults to 3.
        alt_tower (int, optional): Spare tower. Defaults to 2.
    """
    if disks != 0:
        hanoi(disks - 1, from_tower, alt_tower, to_tower)
        print(f"Move disk {disks} from tower {from_tower} to tower {to_tower}")
        hanoi(disks - 1, alt_tower, to_tower, from_tower)


# %% Function Call

DISKS = 3
FROM_TOWER = 1
TO_TOWER = 3
SPARE_TOWER = 2

hanoi(disks=DISKS, from_tower=FROM_TOWER, to_tower=TO_TOWER, alt_tower=SPARE_TOWER)

# %%
