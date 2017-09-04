from collections import defaultdict

cont_list = defaultdict(list)
cont_list = {'pooja': [9999999999],'lakha':[8888888888]}

# Number of contacts you want to add or update

n = int(input('Enter contacts limit - '))

for i in range(n):
	name = input()
	number = input()

	if name in cont_list:
		#update number if name exists
		cont_list[name].append(number)
	else:
		#add name and number if name doesn't exixt
		cont_list[name] = [name]
		cont_list[name] = [number]

print(cont_list)