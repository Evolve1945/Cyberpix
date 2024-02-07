import os

sprites_folder = os.listdir('./sprites/npc/people')
L = []
l_spe = {}
for folder in sprites_folder :
    l = [folder, os.listdir(f'./sprites/npc/people/{folder}')]
    if l[1][-1]=='special' :
        l_spe[folder] = True
    else :
        l_spe[folder] = False

    L.append(l)

print(L)
print(l_spe)