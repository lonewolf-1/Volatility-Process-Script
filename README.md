# Volatility-Process-DLL-Information-Retrieval-Script

Process DLL Information Retrieval Script

This script retrieves information about the dynamic-link libraries (DLLs) associated with a list of processes from a Windows XP Memory Dump. It utilizes the the Volshell capabilities in the Volatility tool, using cc and proc functions to change the context to each process and gather information about the loaded modules (DLLs) for that process.

Prerequisites
This script in runs within Volatility:
https://github.com/volatilityfoundation/volatility.git




Script Overview
The process_list variable contains a list of process IDs which have been previously identified in an infected Windows XP memory dump, for which DLL information will be retrieved.

The script iterates through each process in the process_list.
For each process:
	It changes the context to the current process using cc(pid=i).
	Retrieves the loaded modules (DLLs) for the current process using proc().get_load_modules().
	Prints information about each loaded module, including base address, size, load count, timestamp, and path.
	The script provides formatted output for easy readability.

Output
The script generates formatted output displaying information about the DLLs loaded into each specified process. The output includes the base address, size, load count, timestamp, and path of each loaded module.
