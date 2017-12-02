import random
import data as d
weight_cap=d.wc
voluem_cap=d.vc
items=d.items
population=[]
fit=[]
cnt=len(items)
old=[]
new=[]

def reswv(item):
    w = 0
    v = 0
    p = 0
    for i in range(0, cnt):
        if item[i] == 1:
            w += items[i][1]
            v += items[i][2]
            p+= items[i][3]
    return (p,w,v)

def FitnessFunc(item):
    price=0
    for i in range(0,cnt):
        if item[i]==1:
            price+=items[i][3]
    return price

def InitItem():
    list =sorted(items, key=lambda x: x[3], reverse=True)
    i=0
    for l in list:
        list[i]=list[i][0]
        i+=1
    start_item=random.randint(0, cnt-1)
    new_item=[]
    lw_cap=0
    lv_cap = 0
    for i in range(0,cnt):
        new_item.append(0)
    i=start_item
    while i<cnt and lw_cap+items[list[i]][1]<=weight_cap and lv_cap+items[list[i]][2]<=voluem_cap:
        new_item[list[i]]=1
        lw_cap+= items[list[i]][1]
        lv_cap+= items[list[i]][2]
        i+=1
    price=FitnessFunc(new_item)
    return [new_item,price]
def Selection():
    sum=0
    for p in population:
        sum+=p[1]
    selectp = random.randint(0, sum)
    sum=0
    i=0
    while sum<selectp:
        sum+=population[i][1]
        i+=1
    item=population[i-1]
    old.append(item)
    del population[i-1]

    return item
def SelectPar():
    item1=Selection()
    item2 = Selection()
    children=Cross(item1[0],item2[0])
    for c in children:
        new.append([c,FitnessFunc(c)])

def Cross(item1,item2):
    child1= []
    child2= []
    cnt=len(item2)
    dot1=random.randint(0, cnt//2)
    dot2=random.randint(dot1, cnt-1)
    dot3=random.randint(dot2, cnt-1)
    for i in range(0,dot1):
        child1.append(item1[i])
        child2.append(item2[i])
    for i in range(dot1,dot2):
        child1.append(item2[i])
        child2.append(item1[i])
    for i in range(dot2, dot3):
        child1.append(item1[i])
        child2.append(item2[i])
    for i in range(dot3,cnt):
        child1.append(item2[i])
        child2.append(item1[i])
    return [child1,child2]

def Mutations():
    r=random.randint(0, 200)
    mitem = new[r][0]
    newitem=[]
    for i in range(0,cnt):
        if mitem[i]==1:
            newitem.append(0)
        else:
            newitem.append(1)
    new[r]=[newitem,FitnessFunc(newitem)]
def Filter():
    #Корректировка старых
    for i in range(0,len(old)):
        old[i][1]=round(old[i][1]*0.8)
    #Профильтровать new по весу
    num=0
    for n in new:
        w = 0
        v = 0
        for i in range(0,cnt):
            if  n[0][i]==1:
                w+=items[i][1]
                v+=items[i][2]
        if w>weight_cap or v>voluem_cap:
            del new[num]
        num+=1
    old.extend(new)
    p = sorted(old, key=lambda x: x[1], reverse=True)[:200]
    population.extend(p)

for i in range(0,200):
    population.append(InitItem())
population=sorted(population, key=lambda x: x[1], reverse=True)
#print(population)
pok=0
while (pok<100):
    for i in range(0,100):
        SelectPar()
    Mutations()
    Filter()
    best=population[0]
    pok+=1

print(best,reswv(best[0]))







