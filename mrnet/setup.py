from distutils.core import setup, Extension

mrNetPath = raw_input("Please type the base path to MRNet: ")
if(mrNetPath[-1:]=='/'):
    mrNetPath = mrNetPath[:-1]
mrnet = Extension("MRNet",
                  sources = ["mrnet_module.cpp"],
                  include_dirs = [mrNetPath+"/include"],
                  library_dirs = [mrNetPath+"/lib"],
                  libraries = ["mrnet", "xplat", "boost_timer-mt", "boost_system-mt"],
                  extra_compile_args = [],
                  extra_link_args = ["-Wl,-rpath="+mrNetPath+"/lib", "-Wl,-E"])
setup(name = "MRNet", version = "0.01", description = "Python interface to MRNet", ext_modules = [mrnet])
