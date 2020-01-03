import re

str = 'abcfdfafsa'
m = str.find('ab')
print(m)
print(str[m:])

s = ('''134.  Gass CA, Haritoglou C, Messmer EM, et al. Peripheral visual field defects after macular hole surgery: \n'''
'''a complication with decreasing incidence. Br J Ophthalmol 2001;85:549-51.'''
)
print(s)
p = re.compile('^\d+\..*\.$',re.DOTALL)
# p = re.compile('.*\.$')
#s = 'ID: 042 SEX: M DOB: 1967-08-17 Status: Active 1968'
all_items = re.findall(p,s)
print(all_items)