"""
=======================================================
Controlling style of text and labels using a dictionary
=======================================================

This example shows how to share parameters across many text objects and labels
by creating a dictionary of options passed across several functions.
"""

import numpy as np
import matplotlib.pyplot as plt
from binascii import unhexlify


font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }

#snrstr ='00777B726D77797E81767A7D7B77757A8484847A717D88857D78777C7F84887F7E838180858A817F858C8A88898B8A86808181888385897D797F8983868B878A888786857D7E7E8083808A87777C7F8583757D767581867C7574788288838083817A7C828580827E' 

#snrstr ='006C696D7F858271655D69767A796C6C7D8685807F73584C4947474F66726D63606571788282898886807E7975775E5653504E475165777C7A7A7877796C5C5A594F5357554D4C4C47454B4C454546454445464645444547454443454745494745484747494B4C5256505354524B474444444645464B454B4D4B454644454844434445444445474445434445434242424343444749484646454747464547444544454A4E4649'

#snrstr = '00817F8587838284817F888C817E8283827D614B4E6D715B4E494C4D4C474849586D67686A6F746458544F50534D515352575A59545E5D5C5A5750444A4746454544474444464545474945444645464645464644444545444343464545454746464A44444446454545474547444544444444444442454445484646474546454342424346454444444546464746484945464B4D4D53514B51504F4A4848434547464544424445'

snrstr = '000000695E5D5E5757525659565762686400000000000053616B6060635C555A5D5F59550000626059625B5655585F5455595E6063000000005359575B5D5C5E5960615A5C5F5E59535D5E5F645F5D58555E676600005A5F60595B645F5858615C5A5C5661615F5C5454575D5C5559505A54555D565258574E585B5D00000000004E595B5954585958575356565A5852525A5A5B5B565458565257534E5B52575C51515A595600005156585252525A51554D50504F5151524F4D504F4D4F4D524B47474A000000000000474A4A4A494C4644464547484A43424649454649494F48484A464746474E4D4245440000474545464343484447434449494747484444464546424444474B4B45473700000000000000000000'

yaxi = []


step = len(snrstr)
step = step /2

print step

for i in range(step):
    #byte = int(snrstr[i:i+1],16)
    #print snrstr[i*2:i*2+2]
    yaxi.append(int(snrstr[i*2:i*2+2],16))

print yaxi    

y = np.array(yaxi)

if step >= 278:
    x = np.linspace(2.0, 30.0, step)
else:
    x = np.linspace(2.0, 18.0, step)

plt.plot(x,y)
plt.xlabel('Frequency (MHz)')
plt.ylabel('Strength')


# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
plt.show()