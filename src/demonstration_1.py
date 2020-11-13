"""
An `image` is represented by a 2-D array of integers, each integer representing
the pixel value of the image (from 0 to 65535).
​
Given a coordinate `(sr, sc)` representing the starting pixel (row and column)
of the flood fill, and a pixel value `newColor`, "flood fill" the image.
​
To perform a "flood fill", consider the starting pixel, plus any pixels
connected 4-directionally to the starting pixel of the same color as the
starting pixel, plus any pixels connected 4-directionally to those pixels (also
with the same color as the starting pixel), and so on. Replace the color of all
of the aforementioned pixels with the newColor.
​
At the end, return the modified image.
​
Example 1:
​
```plaintext
Input:
image = [
    [1,1,1],
    [1,1,0],
    [1,0,1]
]
sr = 1, sc = 1, newColor = 2
Output: [
    [2,2,2],
    [2,2,0],
    [2,0,1]
 ]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels
connected by a path of the same color as the starting pixel are colored with
the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally
connected to the starting pixel.
```
​
Notes:
​
- The length of `image` and `image[0]` will be in the range `[1, 50]`.
- The given starting pixel will satisfy `0 <= sr < image.length` and
`0 <= sc < image[0].length`.
- The value of each color in `image[i][j]` and `newColor` will be an integer in
`[0, 65535]`.
"""
def flood_fill(image, sr, sc, new_color):
    """
    Inputs:
    image -> List[List[int]]
    sr -> int
    sc -> int
    new_color -> int
​
    Output:
    List[List[int]]
    """ 
    # from the starting position, we need to traverse outward
    # checking in all 4 cardinal directions 
    # either dft or bft will work since we don't care about the
    # order in which pixels are colored 
    # I'll pick dfs since it's a bit easier to implement 
    # change the color at this position to be the new color 
    # we also need to keep track of the original color 
    original_color = image[sr][sc]
​
    if original_color == new_color:
        return image 
​
    R = len(image)
    C = len(image[0])
​
    def dft(row, col):
        if image[row][col] == original_color:
            image[row][col] = new_color
​
            # look up by subtracting 1 from row index 
            if row >= 1:
                dft(row - 1, col)
​
            # look right by incrementing 1 to the col index 
            if col + 1 < C:
                dft(row, col + 1)
​
            # look down by adding 1 to the row index
            if row + 1 < R:
                dft(row + 1, col)
​
            # look left by subtracting 1 from the col index 
            if col >= 1:
                dft(row, col - 1)
​
    dft(sr, sc)
​
    return image 
​
​
image = [
    [1,1,1],
    [1,1,0],
    [1,0,1]
]
​
flood_fill(image, 1, 1, 2)
​
print(image)