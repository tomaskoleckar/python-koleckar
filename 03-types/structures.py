veta = "Tři sta třicet tři stříbrných stříkaček přestříkalo přes tři sta třicet tři stříbrných střech."
all_freq = {}
def charFrequency(veta):

    for i in veta:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
charFrequency(veta)


#def bubbleSort(arr):
#    n = len(arr)
#    for i in range(n):
#        swapped = False
#       for j in range(0, n - i - 1):
#            if arr[j] > arr[j + 1]:
#                arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                swapped = True
#        if swapped == False:
#            break
#
arr = all_freq

#bubbleSort(arr)


print ("Znaky v rikance :\n " + str(arr))