import sys


def loadSignalsLibs():
    signals_libs_path = me.var("SIGNALS_LIBS")+"\python"

    if signals_libs_path in sys.path:
        pass
    else:
        print("[*] Adding signals libs to path")
        sys.path.insert(0, signals_libs_path)
