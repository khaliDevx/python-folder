# one:  -------------------
# acc = [[7,1,3],[2,8,7],[1,9,5]]
# wealthes = []
# for i in acc:
#     wealthes.append(sum(i))
# print(max(wealthes))

# two:  -------------------

# def diagonalDifference(arr):
#     temp = 0
#     emp = 0
#     for i in range(0,len(arr)):
#         temp = temp + arr[i][i]
#         print(arr[i][i])

#     for j in range(0,len(arr)):
#         emp = emp + arr[j][len(arr)-1-j]
#         print(arr[j][len(arr)-1-j])

#     # return abs(temp - emp)

# def diagonalDifference2(arr):
#     left = [arr[i][i] for i in range(0, len(arr))]
#     right = [arr[j][len(arr)-1-j] for j in range(0, len(arr))]
#     return abs(sum(left) - sum(right))

# arr = [
#     [11, 2, 4],
#     [4, 5, 6],
#     [10, 8, -12]
# ]
# diagonalDifference(arr)
# print(diagonalDifference2(arr))

# Three :
# def staircase(n):
#     [print((n-i) * " " + i*"#") for i in range(0,n+1) if i]
# staircase(6)

# def birthdayCakeCandles(candles):
#     return len([i for i in candles if i == max(candles)])

# candles = [4,8,7,5,8,7,4,7,8,4,1,2,5,8]
# print(birthdayCakeCandles(candles))


# import re
# def timeConversion(s):
#     if "A" in s:
#         s = re.sub("12", "00", s, 1)

#     elif "P" in s:
#         if int(s[0:2]) < 12: s = re.sub(s[0:2], f"{12 + int(s[0:2])}", s)

#     return re.sub("[A-Z]", "", s)

# s = '12:12:54AM'
# print(timeConversion(s))


# def largestPermutation(k, arr):
#     largest = max(arr) # largest = 5
#     positions = {}
#     for i in range(len(arr)): # range(0, 5) means from 0 to 4
#         positions[arr[i]] = i
#         # positions = {
#         #  1 : 0,
#         #  2 : 1,
#         #  3 : 2,
#         #  5 : 3,
#         #  4 : 4
#         # }
#     for i in range(len(arr)):
#         if k == 0:
#             break

#         if arr[i] == largest:
#             largest -= 1

#         if arr[i] < largest:
#             mind = positions[largest] # mind = 3
#             positions[largest], positions[arr[i]] = positions[arr[i]], positions[largest]
#             arr[i], arr[mind] = arr[mind], arr[i]
#             largest -= 1
#             k -= 1

#     return arr
# arr = [1, 2, 3, 5, 4]
# k = 3
# print(largestPermutation(k, arr))


# def maximumToys(prices, k):
#     toys = []
#     while k > min(prices):
#         toys.append(min(prices)) # toys [1 2 3]
#         k -= min(prices) # k = 1
#         prices.remove(min(prices)) #  prices = [3 4]
#     return len(toys)

# prices = [1, 2, 3, 4]
# print(maximumToys(prices, 7))


# def appendAndDelete(s, t, k):
#     matched_occurrences=0

#     for (char_in_s, char_in_t) in zip(s, t):
#         if char_in_s==char_in_t:
#             matched_occurrences+=1

#         else:
#             break
#     tot_len = len(s) + len(t)

#     if (2*matched_occurrences+k >= tot_len and tot_len%2==k%2) or tot_len<k:
#         return "Yes"

#     return "No"

# s = 'hackerhappy'
# t = 'hackerrank'
# k = 10
# print(appendAndDelete(s, t, k))


# from math import ceil, floor

# def squares(a, b):
#     return floor(b**0.5)+1 - ceil(a**0.5)


# print(squares(85, 999))


# def libraryFine(d1, m1, y1, d2, m2, y2):
#     fine = 0
#     if y1 == y2 and m1 == m2 and d1 <= d2:
#         fine = 0
#     elif y1 == y2 and m1 == m2 and d1 > d2:
#         fine = 15 * (d1 - d2)
#     elif y1 == y2 and m1 > m2:
#         fine = 500 * (m1 - m2)
#     elif y1 > y2:
#         fine = 10000
#     return fine

# print(libraryFine(7, 8, 2015, 4, 9, 2015))


# def stringSimilarity(a):
    # suffixes = []
    # similarity = []
    # while len(s) > 0:
    #     suffixes.append(s)
    #     s = s[1:]
    # for i in suffixes:
    #     i = list(i)
    #     s = list(i)
    #     counter = 0
    #     match = 0
    #     for j in i:
    #         if j == s[counter]:
    #             match += 1
    #         counter += 1
    #     similarity.append(match)
    # print(sum(similarity))

#     n = len(a)
#     z = [0]*n
#     l=r=0
#     for i in range(1,n):
#         if (i<=r):
#             z[i]=min (r - i + 1, z[i - l])
#         while(i + z[i] < n and a[z[i]] == a[i + z[i]]):
#             z[i]+=1
#         if (i + z[i] - 1 > r):
#             l = i
#             r = i + z[i] - 1
#     return sum(z)+n
# print(stringSimilarity('ababaa'))


def gradingStudents(grades):
    multiples5 = list(map(lambda x: x + 5, range(40, 101)))
    print(multiples5)
    for ind in range(0, len(grades)):
        for i in multiples5:
            if i > grades[ind] and (i - grades[ind]) < 3:
                grades[ind] = grades[ind] + (i - grades[ind])


    return grades
grades = [32,65,98,74,14,25,69,98]
print(gradingStudents(grades))
