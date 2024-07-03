"""
Last night you partied a little too hard. 
 Now there's a black and white photo of you that's about to go viral!
 You can't let this ruin your reputation,
 so you want to apply the box blur algorithm to the photo to hide its content.

The pixels in the input image are represented as integers.
 The algorithm distorts the input image in the following way:
 Every pixel x in the output image has a value equal to the
 average value of the pixel values from the 3 × 3 square 
 that has its center at x, including x itself. 
 All the pixels on the border of x are then removed.

Return the blurred image as an integer, with the fractions rounded down.

Example

For

image = [[1, 1, 1],
         [1, 7, 1],
         [1, 1, 1]]
the output should be solution(image) = [[1]].

To get the value of the middle pixel in the input 3 × 3 square: (1 + 1 + 1 + 1 + 7 + 1 + 1 + 1 + 1) = 15 / 9 = 1.66666 = 1. The border pixels are cropped from the final result.

For

image = [[7, 4, 0, 1],
         [5, 6, 2, 2],
         [6, 10, 7, 8],
         [1, 4, 2, 0]]
the output should be

solution(image) = [[5, 4],
                  [4, 4]]
There are four 3 × 3 squares in the input image, so there should be four integers in the blurred output. To get the first value: (7 + 4 + 0 + 5 + 6 + 2 + 6 + 10 + 7) = 47 / 9 = 5.2222 = 5. The other three integers are obtained the same way, then the surrounding integers are cropped from the final result.
"""

def solution(m):
    r = len(m)
    c = len(m[0])
    ans = []
    for i in range(1,r-1):
        row=[]
        for j in range(1,c-1):
            row.append(sum([m[i+k][j+l] for k in [-1,0,1] for l in [-1,0,1]])//9)
        ans.append(row)
    return ans


def solution(image):
    # print ([[x[i:i+3] for x in image[j:j+3] for i in range(len(image[j])-2)] for j in range(len(image)-2)])

    return [[int(sum(sum(x[i:i + 3]) for x in image[j:j + 3]) / 9) for i in range(len(image[j]) - 2)] for j in
            range(len(image) - 2)]

def solution(image):

    r = []
    for i in range(len(image)-2):
        r.append([])
        for j in range(len(image[0])-2):
            r[i].append(sum(image[i][j:j+3] + image[i+1][j:j+3] + image[i+2][j:j+3])/9//1)
    return r

def solution(image):
    tmp = [[sum(g) for g in zip(r, r[1:], r[2:])] for r in image]
    tmp2 = [[sum(g)//9 for g in zip(c, c[1:], c[2:])] for c in zip(*tmp)]
    return [[h for h in x] for x in zip(*tmp2)]


def solution(image):
    boxRows = len(image)
    boxCols = len(image[0])
    blurRows = boxRows - 2
    blurCols = boxCols - 2
    output = [[0 for x in range(blurCols)] for y in range(blurRows)]
    currentValue = 0

    for i in range(0, blurRows):
        for j in range(0, blurCols):
            currentValue = image[i][j] + image[i][j + 1] + image[i][j + 2] + image[i + 1][j] + image[i + 1][j + 1] + \
                           image[i + 1][j + 2] + image[i + 2][j] + image[i + 2][j + 1] + image[i + 2][j + 2]
            currentValue = int(currentValue / 9)
            output[i][j] = currentValue
        currentValue = 0

    return output

def solution(g):
    res = []
    for i, row in enumerate(g):
        lst = []
        for j, col in enumerate(row):
            if i != 0 and i != len(g) - 1 and j != 0 and j != len(row) - 1:
                upperSum = g[i-1][j-1] + g[i-1][j] + g[i-1][j+1]
                centerSum = col + row[j+1] + row[j-1]
                lowerSum = g[i+1][j-1] + g[i+1][j] + g[i+1][j+1]
                lst.append(math.floor((upperSum + centerSum + lowerSum)/9))
        res.append(lst)
    return [x for x in res if len(x) != 0]

import numpy as np

def solution(image):
    img = np.array(image)
    stride = np.array([1,1])
    kernel = np.array([3,3])
    output_shape = img.shape - kernel + stride
    strides = np.lib.stride_tricks.as_strided(
        x=img,
        shape=np.append(output_shape, kernel),
        strides = img.strides + img.strides
    )
    return np.floor(np.mean(strides, axis=(2,3))).astype(np.int).tolist()


def solution(image):
    numrows = len(image)
    numcols = len(image[0])
    print(numrows)
    print(numcols)
    NewMatrix = [[0 for x in range(numcols - 2)] for y in range(numrows - 2)]
    for i in range(numrows - 2):
        for j in range(numcols - 2):
            NewMatrix[i][j] = (image[i][j] + image[i + 1][j] + image[i + 2][j] + image[i][j + 1] + image[i + 1][j + 1] +
                               image[i + 2][j + 1] + image[i][j + 2] + image[i + 1][j + 2] + image[i + 2][j + 2]) // 9
    return NewMatrix


def solution(image):
    def avg_matrix(image, r, c):
        s = 0
        for i in range(r - 2, r + 1):
            for j in range(c - 2, c + 1):
                s += image[i][j]
        return s / 9
    ret = []
    for r, row in enumerate(image):
        if r < 2:
            continue
        nrow = []
        ret.append(nrow)
        for c, col in enumerate(row):
            if c < 2:
                continue
            nrow.append(int(avg_matrix(image, r, c)))
    return ret

from scipy.ndimage import generic_filter as gf
def solution(im):
    im = numpy.array(im)
    ims = im.shape
    ni = gf(im,lambda x: numpy.floor(numpy.mean(x)),3)
    return ni[1:ims[0]-1,1:ims[1]-1]

