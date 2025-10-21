__author__ = "runekri3"

stairs_amount = int(input())
stair_heights = list(map(int, input().split()))
boxes_amount = int(input())
boxes = []
for _ in range(boxes_amount):
    boxes.append(list(map(int, input().split())))

for width, height in boxes:
    box_bottom = max(stair_heights[0], stair_heights[width - 1])
    print(box_bottom)
    stair_heights[0] = box_bottom + height