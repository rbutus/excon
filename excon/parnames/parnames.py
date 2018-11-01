import pandas as pd
import collections


def match():

#  Decide whether or not to create a parameter file (can take a few minutes)
#  If not updates to the 'datnames.xlsx' file have been made, select 'n' as 
#  it's not necesessary.
	choice = input("Generate new parameter file?(y/n): ")
#  Select matrix type, later on this will add a subscript for LEPH, HEPH, VPH etc..
	matrix = input("What matrix are you using?(soil/water/vapour): ")
	
#  Import required Excel tables into pandas dataframes
	datdf = pd.read_excel('datnames.xlsx', encoding='utf-8')
	tabdf = pd.read_excel('tabnames.xlsx', encoding='utf-8')
	aliasdf = pd.read_excel('datnames.xlsx', encoding='utf-8')


#  Creates a list of lists of manually inputed aliases for each parameter from 
#  datnames.xlsx file. 
	params_perm_lists_nan = datdf.values.tolist()

#  Removes 'nan' values from lists within the params_perm_lists_nan list
	params_perm_lists = []
	for params_perm_list_nan in params_perm_lists_nan:
		params_perm_list = [x for x in params_perm_list_nan if str(x) != 'nan']
		params_perm_lists.append(params_perm_list)


#  if YES selected to generate a new parameter file	
	if choice == 'y':       #  

#  Creates a dictionary with every possible sequential segment of letters 
#  of each parameter, including from the manually entered names and saves 
#  into a dictionary: 
		param_segs = {}
		for params in params_perm_lists:  #  For each list in lists
			segs = []					  
			for param in params:		  #  For each item in list
				length = len(param)
				for x in range(0, length):
					for y in range(x + 1, length + 1):
						seg = param[x:y]
						segs.append(seg)  #  Adds segment to list 'segs'
#  Adds first item of list (parametername) to dictionary as the key
#  and the list of possible segments as the value					
			param_segs[params[0]] = segs
			

		param_unique_segs = {}

		for param, segs in param_segs.items():
			counter = collections.Counter(segs)
			counter = dict(counter)
			new_segs = set(segs)
			param_unique_segs[param] = new_segs

#  Create a master list with every possible segment from every parameter.
		all_segs = []
		for key, values in param_unique_segs.items():
			for value in values:
				all_segs.append(value)

#  Create several lists to store segs based on their character length
#  For optimizing procressing time.
		unique1 = []
		unique2 = []
		unique3 = []
		unique4 = []
		unique5 = []
		unique6 = []
		unique7 = []
		unique8 = []
		unique9 = []
		unique10 = []
		unique11 = []
		unique12 = []
		unique13 = []
		unique14 = []
		unique15 = []

#  Counter determines the # of occurences of each segment. Only segments
#  that occur once are used.
		counter = collections.Counter(all_segs)
		counter = dict(counter)
		for key, value in counter.items():
			if value == 1:

#  Segs are stored in different lists based on character length.
				if len(key) == 1:
					unique1.append(key)
				elif len(key) == 2:
					unique2.append(key)
				elif len(key) == 3:
					unique3.append(key)
				elif len(key) == 4:
					unique4.append(key)
				elif len(key) == 5:
					unique5.append(key)
				elif len(key) == 6:
					unique6.append(key)
				elif len(key) == 7:
					unique7.append(key)
				elif len(key) == 8:
					unique8.append(key)
				elif len(key) == 9:
					unique9.append(key)
				elif len(key) == 10:
					unique10.append(key)
				elif len(key) == 11:
					unique11.append(key)
				elif len(key) == 12:
					unique12.append(key)
				elif len(key) == 13:
					unique13.append(key)
				elif len(key) == 14:
					unique14.append(key)
				else:
					unique15.append(key)

#  Creates a dictionary with globally unique segments
#  for each parameter. Only searches the appropriate list
#  for uniqueness based on character length of segment.
		unique_segs = {}
		for key, values in param_unique_segs.items():
			unique_values = []
			for value in values:
				if len(value) == 1:
					if value in unique1:
						unique_values.append(value)
				elif len(value) == 2:
					if value in unique2:
						unique_values.append(value)
				elif len(value) == 3:
					if value in unique3:
						unique_values.append(value)
				elif len(value) == 4:
					if value in unique4:
						unique_values.append(value)
				elif len(value) == 5:
					if value in unique5:
						unique_values.append(value)
				elif len(value) == 6:
					if value in unique6:
						unique_values.append(value)
				elif len(value) == 7:
					if value in unique7:
						unique_values.append(value)
				elif len(value) == 8:
					if value in unique8:
						unique_values.append(value)
				elif len(value) == 9:
					if value in unique9:
						unique_values.append(value)
				elif len(value) == 10:
					if value in unique10:
						unique_values.append(value)
				elif len(value) == 11:
					if value in unique11:
						unique_values.append(value)
				elif len(value) == 12:
					if value in unique12:
						unique_values.append(value)
				elif len(value) == 13:
					if value in unique13:
						unique_values.append(value)
				elif len(value) == 14:
					if value in unique14:
						unique_values.append(value)
				else:
					if value in unique15:
						unique_values.append(value)
			unique_segs[key] = unique_values
		
#  Convert dictionary of unique segments into pandas DataFrame
#  and writes to disk (current working directory) as 'param_file.xlsx'
		df_unique_segs = pd.DataFrame.from_dict(unique_segs, orient='index')
		writer = pd.ExcelWriter('param_file.xlsx')
		df_unique_segs.to_excel(writer, 'sheet1')
		writer.save()

#  If NO was selected for generating a new parameter file, program
#  resumes here. The file already exists and a Pandas dataframe is
#  created from the existing file.
	
	df_unique_segs = pd.read_excel('param_file.xlsx')

#  Creates a list of parameter names (alias tuple) from the dataframe that was 
#  created from tabfile.xlsx
	tab_params = tabdf.parameter.tolist()

#  Creates a dicitonary of parameter names (alias tuple) and list of unique segments from
#  the dataframe that was created from generated parameter file (param_file.xlsx)
#  and removes the 'nan' value from the lists.
	dat_unique_dict = {}
	for dat_param, dat_unique_segs_nan in df_unique_segs.iterrows():
		dat_unique_segs = [x for x in dat_unique_segs_nan if str(x) != 'nan'] 
		dat_unique_dict[dat_param] = dat_unique_segs


#  List of parameters that may need the matrix subscript (s,w, or v)
	matrix_subscript = ['LEPH', 'lEPH', 'LEPH (SG)', 'lEPH (SG)',
						'HEPH', 'HEPH (SG)',
					    'VPH']
	no_match = []

#  Find and add a matrix subscript to any parameter name that's included
#  in the matrix_subscript list, before matching begins.
	for n, tab_param in enumerate(tab_params):
		if tab_param in matrix_subscript:
			tab_params[n] = tab_param[0].upper() + tab_param[1:] + matrix[0].lower()

#  Matching of parameter names from tables and pre-determined database
#  parameter names.
	print("\nParameters:\n--------------------")
	for tab_param in tab_params:
		param_match_list = []
		param_match=False
		matches = 0	
		length = 15
		while length > 0:
			length -= 1
			for dat_param, dat_unique_segs in dat_unique_dict.items():
					if tab_param in datdf.loc[datdf.parameter == dat_param].values:
						print(dat_param)
						param_match=True
						length = 0
						break
					else:											
						if matches < 6:
							for dat_unique_seg in dat_unique_segs:
								if len(str(dat_unique_seg)) == length and str(dat_unique_seg) in str(tab_param):
									#print(tab_param + "_two")
									#if str(dat_unique_seg) in str(tab_param):								
									param_match_list.append(dat_param)
									matches =+ 1
									
		num_matches = len(param_match_list)
		if num_matches >=3:
			print(max(set(param_match_list), key=param_match_list.count))
			param_match = True
		if num_matches == 2:
			print(param_match_list[1], "  *** ONLY ONE MATCH")
			param_match = True
		if num_matches == 1:
			print(param_match_list[0], "  *** ONLY ONE MATCH")
			param_match = True
							

#  If not matches are found above then the following is printed. In this case, the
#  table names never encountered before can be added to the datnames.xlsx file.
		if param_match == False:
			print('[{}] ** NO MATCH **'.format(tab_param))
			no_match.append(tab_param)

	print("--------------------")
	if len(no_match) == 0:
		print("All parameter names matched! :)")
	else:
		print("\n A total of {} parameter name(s) didn't match: \n".format(len(no_match)))
		for items in no_match:
			print(items)






