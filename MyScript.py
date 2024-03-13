# list of 5 chosen processes
process_list = [168, 1384, 2748, 3128, 3552]

# names of titles used to output associated DLL information
T1 = "Base"
T2 = "Size"
T3 = "LoadCount"
T4 = "Time"
T5 = "Path"

# loop which iterates through the array, changes context and accesses the content within the dll data structure
for i in process_list:
	cc(pid=i)
	print("\n\n\n\nThese are the associated DLL's for {0}:\n".format(i))

        # gathers the DLLs for the currently selected process
	loaded_modules = proc().get_load_modules()
	
        # formatting for output
	print("{0}           {1}          {2}       {3}                               {4}\n".format(T1, T2, T3, T4, T5))
	print("--------------------------------------------------------------------")	

        # nested loop enumerating the info about the DLL
	for module in loaded_modules:
		base = hex(module.DllBase).rstrip("L")
		size = hex(module.SizeOfImage).rstrip("L")
		load = hex(module.LoadCount).rstrip("L")
		time = module.TimeDateStamp
		path = module.FullDllName

                # prints info of the loaded module
		print("|{0} |{1} |{2} |{3} |{4}\n".format(base, size, load, time, path))
	print("--------------------------------------------------------------------")
	print("--------------------------------------------------------------------\n\n\n\n")
