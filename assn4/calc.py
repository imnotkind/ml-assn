count = [[[[0 for a in range(2)] for b in range(2)] for c in range(2)] for d in range(2)]

count[0][0][0][0] = 2
count[0][0][0][1] = 5
count[0][0][1][0] = 2
count[0][0][1][1] = 5
count[0][1][0][0] = 2
count[0][1][0][1] = 4
count[0][1][1][0] = 6
count[0][1][1][1] = 8
count[1][0][0][0] = 7
count[1][0][0][1] = 5
count[1][0][1][0] = 7
count[1][0][1][1] = 12
count[1][1][0][0] = 10
count[1][1][0][1] = 10
count[1][1][1][0] = 10
count[1][1][1][1] = 5

m = [(0, 0) for _ in range(4)]

x = 0
y = 0
for b in range(2):
    for c in range(2):
        for d in range(2):
            x += count[0][b][c][d]
            y += count[1][b][c][d]
m[0] = (x / 100,y / 100)

x = 0
y = 0
for b in range(2):
    for c in range(2):
        for d in range(2):
            x += count[b][0][c][d]
            y += count[b][1][c][d]
m[1] = (x / 100,y / 100)

x = 0
y = 0
for b in range(2):
    for c in range(2):
        for d in range(2):
            x += count[b][c][0][d]
            y += count[b][c][1][d]
m[2] = (x / 100,y / 100)

x = 0
y = 0
for b in range(2):
    for c in range(2):
        for d in range(2):
            x += count[b][c][d][0]
            y += count[b][c][d][1]
m[3] = (x / 100,y / 100)

n = [(0, 0, 0, 0) for _ in range(6)]

x = 0
y = 0
z = 0
w = 0
for c in range(2):
    for d in range(2):
        x += count[0][0][c][d]
        y += count[0][1][c][d]
        z += count[1][0][c][d]
        w += count[1][1][c][d]
n[0] = (x / 100,y / 100,z/100, w/100)

x = 0
y = 0
z = 0
w = 0
for c in range(2):
    for d in range(2):
        x += count[0][c][0][d]
        y += count[0][c][1][d]
        z += count[1][c][0][d]
        w += count[1][c][1][d]
n[1] = (x / 100,y / 100,z/100, w/100)

x = 0
y = 0
z = 0
w = 0
for c in range(2):
    for d in range(2):
        x += count[0][c][d][0]
        y += count[0][c][d][1]
        z += count[1][c][d][0]
        w += count[1][c][d][1]
n[2] = (x / 100,y / 100,z/100, w/100)

x = 0
y = 0
z = 0
w = 0
for c in range(2):
    for d in range(2):
        x += count[c][0][0][d]
        y += count[c][0][1][d]
        z += count[c][1][0][d]
        w += count[c][1][1][d]
n[3] = (x / 100,y / 100,z/100, w/100)

x = 0
y = 0
z = 0
w = 0
for c in range(2):
    for d in range(2):
        x += count[c][0][d][0]
        y += count[c][0][d][1]
        z += count[c][1][d][0]
        w += count[c][1][d][1]
n[4] = (x / 100,y / 100,z/100, w/100)

x = 0
y = 0
z = 0
w = 0
for c in range(2):
    for d in range(2):
        x += count[c][d][0][0]
        y += count[c][d][0][1]
        z += count[c][d][1][0]
        w += count[c][d][1][1]
n[5] = (x / 100,y / 100,z/100, w/100)

I = [0 for _ in range(6)]

import math

for c in range(2):
    for d in range(2):
        joint = n[0][2*c + d]
        I[0] += joint * math.log(joint / (m[0][c] * m[1][d]))
        
for c in range(2):
    for d in range(2):
        joint = n[1][2*c + d]
        I[1] += joint * math.log(joint / (m[0][c] * m[2][d]))

for c in range(2):
    for d in range(2):
        joint = n[2][2*c + d]
        I[2] += joint * math.log(joint / (m[0][c] * m[3][d]))

for c in range(2):
    for d in range(2):
        joint = n[3][2*c + d]
        I[3] += joint * math.log(joint / (m[1][c] * m[2][d]))

for c in range(2):
    for d in range(2):
        joint = n[4][2*c + d]
        I[4] += joint * math.log(joint / (m[1][c] * m[3][d]))


for c in range(2):
    for d in range(2):
        joint = n[5][2*c + d]
        I[5] += joint * math.log(joint / (m[2][c] * m[3][d]))





print(count)
print(m)
print(n)
print(I)