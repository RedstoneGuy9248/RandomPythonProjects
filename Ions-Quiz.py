import random
while True:
    names_list = ['Sodium','Potassium','Silver','Copper I','Magnesium','Calcium','Zinc','Iron II','Copper II','Aluminium','Iron III','Hydrogen','Hydride','Chloride','Bromide','Iodide','Oxide','Sulphide','Nitride','Ammonium','Hydroxide','Nitrate','Hydrogen Carbonate','Carbonate','Sulphite','Sulphate','Phosphate']
    symbols_list = ['Na+','K+','Ag+','Cu+','Mg^2+','Ca^2+','Zn^2+','Fe^2+','Cu^2+','Al^3+','Fe^3+','H+','H-','Cl-','Br-','I-','O^2-','S^2-','N^3-','NH4+','OH-','NO3-','HCO3-','CO3^2-','SO3^2-','SO4^2-','PO4^3-']
    score = 0
    random.seed(random.getrandbits(128))
    l=list(range(0,len(names_list)))
    random.shuffle(l)
    wrong = list()
    for i in l:
        ans=input("{}. Symbol? ".format(names_list[i]))
        if(ans != symbols_list[i]):
            print("Wrong! Answer Was: {}! Score = {}".format(symbols_list[i],score))
            wrong.append(i)
        else:
            score+=1
            print("Correct! Score = {}".format(score))
    print("Score: {} / {}".format(score,len(names_list)))
    if(len(wrong) != 0):
        print("Wrong Answers:")
        for i in wrong:
            print("{}: {}".format(names_list[int(i)],symbols_list[int(i)]))
    else:
        print("All Correct! Nice!")
    while True:
        retry = input("Retry? (Y/N): ")
        if(retry == "Y"):
            break
        elif(retry == "N"):
            exit()
        else:
            print("Enter Y or N")


        
