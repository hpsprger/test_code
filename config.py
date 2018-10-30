import os

# toolchains options
ARCH=''
CPU=''
CROSS_TOOL='gcc'
PLATFORM 	= 'gcc'
EXEC_PATH 	= '/usr/bin/'

if PLATFORM == 'gcc':
    # toolchains
    PREFIX = ''
    CC = PREFIX + 'gcc -m32 -fno-builtin -fno-stack-protector -nostdinc'
    AS = PREFIX + 'gcc -m32'
    AR = PREFIX + 'ar'
    LINK = PREFIX + 'ld -melf_i386'
    TARGET_EXT = 'elf'
    SIZE = PREFIX + 'size'
    OBJDUMP = PREFIX + 'objdump'
    OBJCPY = PREFIX + 'objcopy'
    DEVICE = ''
    CFLAGS = DEVICE + ' -Wall'
    AFLAGS = ' -c' + DEVICE + ' -x assembler-with-cpp'
    LFLAGS = DEVICE + ' -Map rtthread-ia32.map -T x86_ram.lds -nostdlib'
    CPATH = ''
    LPATH = ''
else:
    print('platform  mismatch!')