import genalg
import data as d

items = d.items
cnt = len(items)
weight_cap = d.wc
voluem_cap = d.vc
res=[]
def reswv(item):
    w = 0
    v = 0
    for i in range(0, cnt):
        if item[i] == 1:
            w += items[i][1]
            v += items[i][2]
    return (w,v)

def func_to_optimize(item):
    price = 0
    w = 0
    v = 0
    for i in range(0, cnt):
        if item[i] == 1:
            price += items[i][3]
            w += items[i][1]
            v += items[i][2]
    if w > weight_cap or v > voluem_cap:
        price = 0
    return price

for i in range(0,10):
    if __name__ == "__main__":
        p = genalg.Population(
            popsize=2000,  # number of individuals in the population
            nchrom=30,  # number of chromosomes per individual
            chromset=range(0, 2)  # set from which to pick chromosomes
        )
        best = p.run(
            eval_fn=func_to_optimize,  # function to optimize
            fitness_goal=float("Inf"),  # maximum fitness to optimize towards
            generations=400  # maximum generations to run for
        )
        res.append((best.chromosomes,best.fitness))
res=sorted(res, key=lambda x: x[1], reverse=True)
for i in range(0,len(res)):
    print(res[i])
print(' ')
print(res[0],reswv(res[0][0]))
