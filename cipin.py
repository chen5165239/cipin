
labels = []
f = open('关键词.txt','r', encoding='gbk')
for label in f.readlines():
    label = label.rstrip('\n')
    #label = label.rstrip(' ')
    print(label)
    #print(type(label))
    single = label.split(';')
    #print(single)
    for i in range(len(single)):
        if single[i]!='':
            labels.append(single[i])


print('labels')

print(labels)
print(len(labels))
labels = list(set(labels))
print(len(labels))

index = []
for i in range(len(labels)):
    index.append(0)
f1 = open('关键词.txt','r', encoding='gbk')
for label in f1.readlines():
    label = label.rstrip('\n')
    single = label.split(';')
    for i in range(len(single)):
        if single[i]!='':
            for j in range(len(labels)):
                if single[i] == labels[j]:
                    index[j]=index[j]+1
                    break


print(index)
print(len(index))

a=0
for i in range(len(index)):
    a = a + index[i]


print(a)

f2 = open('guanjianci.txt', 'w', encoding='gbk')
for i in range(len(labels)):
    f2.write(labels[i])
    print(labels[i])
    f2.write('\n')


f3 = open('cishu.txt', 'w', encoding='gbk')
for i in range(len(index)):
    f3.write(str(index[i]))
    print(index[i])
    f3.write('\n')




