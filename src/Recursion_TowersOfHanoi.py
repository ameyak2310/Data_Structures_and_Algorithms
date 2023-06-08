def hanoi(disks, from_tower, to_tower, alt_tower):
    if disks != 0:
        hanoi(disks-1, from_tower, alt_tower, to_tower)
        print('\nMove disk {} from tower {} to tower {}'.format(disks, from_tower, to_tower ))
        hanoi(disks-1, alt_tower, to_tower, from_tower)

hanoi(3,1,3,2)
