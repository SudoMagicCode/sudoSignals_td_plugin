import sys


def loadSignalsLibs():
    if me.var("SIGNALS_LIBS") != "":
        signals_libs_path = me.var("SIGNALS_LIBS")+"\python"
    else:
        signals_libs_path = project.folder+"//td-python//packets"

    if signals_libs_path in sys.path:
        pass
    else:
        print("[*] Adding signals libs to path")
        sys.path.insert(0, signals_libs_path)
