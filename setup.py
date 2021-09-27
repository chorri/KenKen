from cx_Freeze import setup, Executable
build_exe_options = {"packages": ["pygame", "pygame_menu"], "excludes": ["tkinter"], "include_files":["sum.PNG", "mult.png"]}
setup(
        name = "pyken",
        version = "1.0",
        description = "hello there",
	options={"build_exe": build_exe_options},
        executables = [Executable("pyken.py", base=None)]
)