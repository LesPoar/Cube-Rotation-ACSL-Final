# Cube-Rotation-ACSL-Final
PROBLEM: The ACSL Cube is a 3x3x3 cube with colored tiles on each side. In the initial
configuration of the cube, the front side is Purple, the right side is Green, the top is Red, the left
side is Blue, the back side is Orange, and the bottom is Yellow. The tiles are numbered as
shown. The tiles will be referred to by color and number (e.g. P2). The left diagram below
shows the cube in 3D and the right
diagram shows the cube unfolded.
You’ll be given a focus tile, and then asked to rotate the column or row containing that tile
through a sequence of moves. The focus tile is specified by color and number. For example, P2
is the tile labeled 2 on the purple side, the upper right as you orient the cube looking at the purple
side. The tile G7 would be in the middle of the bottom row as you look at the green side with
the 0-1-2 row at the top.
A row or column can be rotated either clockwise or counterclockwise. First orient the cube so
that the side with the focus tile is in front of you, and then orient that side in such a way that the
initial 0-1-2 of that side would be the top row. A clockwise rotation of a column would take the
tiles in that column and circulate them upwards so that the tiles on the front face go to the top
face, the tiles on the top face go to the back face, and so on. The diagrams below show a
one-step clockwise column rotation of P2.
2021-2022 ● Finals Program #4: Cube Rotation ● Senior Division
A clockwise rotation of a row would rotate the row to the left. The diagram below takes the
diagram above and performs a 4-step clockwise row rotation of P2. The 3D cube is displayed
with two orientations so you can see more of it. In the second image (with the orange side on
top), you see the cube oriented so that the P2 tile is prepared for its next rotation.
A 3-step counterclockwise column rotation of the P2 tile is illustrated below.
Note that rotations are not like a Rubik’s cube that you might be familiar with: only the tiles in
the column or row circulate. For example, the initial clockwise column rotation of P2 did not
change the green side; the next clockwise row rotation of P2 did not change the purple side.
2021-2022 ● Finals Program #4: Cube Rotation ● Senior Division
INPUT: Each input will consist of the focus tile followed by a sequence of up to 10 moves. The
focus tile is a string with 2 characters: a color (O,B,R,G,Y, P) followed by a number (0 through
8). Each move is a string of three characters indicating how the focus tile should be moved. The
3 characters are: R for a row rotation or C for a column rotation; C for clockwise or R for
counterclockwise; and a number (0 through 9) indicating the number of clicks to rotate.
OUTPUT: After each sequence of moves has been made beginning with the initial cube, print
all of the tiles on the side with the focus tile after orienting that side so that the original 0-1-2 is
in the top row. Print the tiles in row-major order. For the sequence of moves described above
(P2 CC1 RC4 CR3), the output would be: P0P1P5B1B4P2P6P7Y6.
SAMPLE INPUT:
1. P2 CC1 RC4 CR3
2. G5 RC5
3. O7 CR7
4. Y2 RR1 CC1
5. G1 CC1 RR5 CR7 RC3
SAMPLE OUTPUT:
1. P0P1P5B1B4P2P6P7Y6
2. R0R1R2G5Y3Y4R6R7R8
3. Y0R4Y2Y3R1Y5Y6O7Y8
4. Y2O0O1O3O4O5O6O7O8
5. B0P4O8B3P5G1B6G7O6
2021-2022 ● Finals Program #4: Cube Rotation ● Senior Division
TEST DATA
TEST INPUT:
1. O8 CC2
2. P3 CR4
3. G0 RR3
4. B6 RC1
5. R5 RC1 CR2
6. R8 CR4 RC3
7. Y5 RC1 CR1 RR1 CC1
8. B6 CR3 CC4 RC1 RR2
9. P4 RR0 CC0 RC7 CR9
10. Y2 CR1 RC2 CR3 RC4 CC5 RC6 CR7 RC8 CR9
TEST OUTPUT:
1. O0O1O8O3O4R2O6O7R5
2. Y0Y1P3Y3Y4P0Y6Y7R6
3. G0G1G2Y3Y4Y5Y6Y7Y8
4. Y0Y1Y2Y3Y4Y5Y7Y8B6
5. P0R5P2P3R7P5P6P1P8
6. G0G1G2G3G4G5R8Y7Y8
7. Y0O1B3Y4Y1Y5G8Y6P6
8. G0G1P8B6G3G4G6G7P6
9. O8Y1Y2P4Y4Y5O2Y7Y8
10. Y5O1R2Y2B1O6P2O7R8
