import math, re, numpy, pandas
s1_1 = lambda a, b: a + b
s2_1 = lambda y: math.ceil(y / 100)
s3_1 = lambda s: s[::-1] == s
s4_1 = lambda y: max([a * b for a, b in zip(y[:-1], y[1:])])
s5_2 = lambda n: (n - 1) ** 2 + n ** 2
s6_2 = lambda s: max(s) - min(s) - len(set(s)) + 1
s8_2 = lambda x: sum(x[0] + list(map(sum, [[x[i][j] for j in range(len(x[i])) if x[i - 1][j] != 0] for i in range(1, len(x))])))
s9_3 = lambda y: [i for i in y if len(i) == len(max(y, key=len))]
s10_3 = lambda s1, s2: sum([min(s1.count(i), s2.count(i)) for i in set(s1)])
s11_3 = lambda n: sum(list(map(int, str(n)[:int(len(str(n)) // 2)]))) == sum(list(map(int, str(n)[int(len(str(n)) // 2):])))
s13_3 = lambda s: eval('"' + s.replace('(', '"+("').replace(')', '")[::-1]+"') + '"')
s14_4 = lambda a: [sum(a[::2]), sum(a[1::2])]
s21_5 = lambda s: len(s.split('.')) == 4 and all([n.isdigit() and 0 <= int(n) < 256 for n in s.split('.')])
s48_11 = lambda s: s.isdigit()
s27_6 = lambda n: n.isidentifier()
s25_6 = lambda i, e, s: [x if x != e else s for x in i]
s26_6 = lambda n: all(int(d) % 2 == 0 for d in str(n))
s36_8 = lambda s: len(set(s))

n7_2 = lambda s: 3 > sum((i >= j) + (i >= k) for i, j, k in zip(s, s[1:], s[2:] + [10 ** 6]))
n15_4 = lambda p: ["*" * (len(p[0]) + 2)] + ["*" + i + "*" for i in p] + ["*" * (len(p[0]) + 2)]
n16_4 = lambda A, B: sorted(A) == sorted(B) and sum([a != b for a, b in zip(A, B)]) <= 2
n20_5 = lambda a: max([abs(a[i] - a[i + 1]) for i in range(len(a) - 1)])
n22_5 = lambda ia: min([i for i in range(2, max(ia) + 2) if all([j % i != 0 for j in ia])])
n23_5 = lambda image: [[int(sum(sum(x[i:i + 3]) for x in image[j:j + 3]) / 9) for i in range(len(image[j]) - 2)] for j in range(len(image) - 2)]
n28_6 = lambda s: "".join(chr((ord(i) - 96) % 26 + 97) for i in s)
n29_6 = lambda c1, c2: (ord(c1[0]) + int(c1[1]) + ord(c2[0]) + int(c2[1])) % 2 == 0
n30_7 = lambda n, fn: (fn + n / 2) % n
n31_7 = lambda d, r, t: math.ceil(math.log(t / d, 1 + r / 100))
n32_7 = lambda a: a[(len(a) - 1) // 2]
n34_8 = lambda ia, k: [i for (n, i) in enumerate(ia) if (n + 1) % k != 0]
n38_9 = lambda u, d, h: 1 if h <= u else (h - u - 1) // (u - d) + 2
n39_9 = lambda v1, w1, v2, w2, maxW: max((w1 + w2 <= maxW) * (v1 + v2), (w1 <= maxW) * v1, (w2 <= maxW) * v2)
n40_9 = lambda i: re.findall('^\d*', i)[0]
n42_9 = lambda b, p: abs(ord(b[0]) - ord(p[0])) == abs(ord(b[1]) - ord(p[1]))
n51_11 = lambda n: max([int(str(n)[:i] + str(n)[i + 1:]) for i in range(len(str(n)))])
n52_12 = lambda text: max(re.split('[^a-zA-Z]', text), key=len)
n33_7 = lambda w1, w2: sum([a[0] != a[1] for a in zip(w1, w2)]) == 1
n35_8 = lambda s: re.search('\\d', s).group(0)
n18_4 = lambda i: sum([i.count(i)%2 for i in set(i)]) <= 1
n19_5 = lambda ul, ur, fl, fr: {ul, ur} == {fl, fr}
n44_10 = lambda a: a[a.rfind("@")+1:]
n46_10 = lambda votes, k: (sum(numpy.array(votes) + k > max(votes))) + (k==0 and sum(numpy.array(votes)==max(votes))==1)
n47_10 = lambda i: bool(re.fullmatch(r'([A-F\d]{2}-){5}([A-F\d]{2})', i))
n53_12 = lambda time: int(time[0:2]) < 24 and int(time[3:]) < 60
n54_12 = lambda i: sum(map(int,re.findall('\d+',i)))
n55_12 = lambda matrix: len(set(tuple(matrix[o][n] for o in range(i,i+2) for n in range(j,j+2)) for i in range(len(matrix)-1) for j in range(len(matrix[i])-1)))
n58_12 = lambda c: "".join([chr(int(c[i:i+8],2)) for i in range(0,len(c),8)])

n12_3 = 1
n17_4 = 1
n24_5 = 1
n37_8 = 1

n43_10 = 0
n45_10 = 1

n49_11 = 0
n50_11 = 0

n56_12 = 0
n57_12 = 0
n59_12 = 0
n60_12 = 0

n61_12 = 0
n62_12 = 0
n63_12 = 0

def s41_9(m, d=0):
    while len(str(sum(list(map(int, str(m)))))) > 1: m = str(sum(list(map(int, str(m))))); d = d + 1
    return d
