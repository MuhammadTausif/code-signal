"""
You are given an array of strings names representing filenames. The array is sorted in order of file creation, such that names[i] represents the name of a file created before names[i+1] and after names[i-1] (assume 0-based indexing). Because all files must have unique names, files created later with the same name as a file created earlier should have an additional (k) suffix in their names, where k is the smallest positive integer (starting from 1) that does not appear in previous file names.

Your task is to iterate through all elements of names (from left to right) and update all filenames based on the above. Return an array of proper filenames.

Example

For names = ["doc", "doc", "image", "doc(1)", "doc"], the output should be solution(names) = ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"].

Since names[0] = "doc" and names[1] = "doc", update names[1] = "doc(1)"
Since names[1] = "doc(1)" and names[3] = "doc(1)", update names{3} = "doc(1)(1)"
Since names[0] = "doc", names[1] = "doc(1)", and names[4] = "doc", update names[4] = "doc(2)"
"""

def solution(n):
    for i in range(1,len(n)):
        if n[i] in n[:i]:
            v=1
            while n[i]+'('+str(v)+')' in n[:i]:
                v+=1
            n[i]=n[i]+'('+str(v)+')'
    return(n)

def solution1(names):
    r=[]
    d={}
    for n in names:
        m=n
        c=0
        while m in d:
            c+=d[m]
            m=n+"(" + str(c) +")"
        d[m]=1
        r.append(m)
    return r

def solution2(n):
    for i in range(len(n)):
        if n[i] in n[:i]:
            j = 1
            while n[i]+"("+str(j)+")" in n[:i]:
                j += 1
            n[i] += "("+str(j)+")"
    return n

def solution3(names):
    for i in range(len(names)):
        if names[i] in names[:i]:
            j=1
            while names[i]+"("+str(j)+")" in names[:i]:
                j+=1
            names[i]+="("+str(j)+")"
    return names


def solution4(names):
    solution = []

    for n in names:
        s = n
        i = 1
        while (s in solution):
            s = n + '(' + str(i) + ')'
            i += 1

        solution.append(s)

    return solution

def solution5(names):
    nms = names[:]
    for i in range(len(nms)):
        if nms[i] in nms[:i]:
            k = 1
            new_name = '{0}({1})'.format(nms[i], k)
            while new_name in nms[:i]:
                k += 1
                new_name = '{0}({1})'.format(nms[i], k)
            else:
                nms[i] = new_name
    return nms