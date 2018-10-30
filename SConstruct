import os
import sys
from SCons.Script import *

AddOption('--target',
  dest='target',
  nargs=1, type='string',
  action='store',
  metavar='DIR',
  help='application to be built')

target = GetOption('target')

def DoBuilding(TARGET):
    global Env
    sys.path = sys.path + [os.path.join(Rtt_Root, 'tools'), BSP_Root]
	Env = Environment(TARGET_ARCH='x86')
	Env.Append(CCFLAGS=rtconfig.M_CFLAGS)
	Env.Append(LINKFLAGS=rtconfig.M_LFLAGS)
	Env.Append(CPPPATH=CPPPATH)
	Env.Append(LIBS='rtthread', LIBPATH=BSP_Root)
	Env.Append(CPPDEFINES=GetCPPDEFINES() + ['RTT_IN_MODULE'])
	Env.PrependENVPath('PATH', rtconfig.EXEC_PATH)

    objs = SConscript(SConscriptFile)
    target = Env.Program(target, objs)

if target == None:
  print("none target, please use ")
  print("    scons --target=mcss_so")
  print("    scons --target=all")
  exit(0)
else:
    DoBuilding(target)