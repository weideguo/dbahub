
import ctypes
import sys
import os
import platform


if platform.machine() != "x86_64":
    print(f"错误：当前架构是 {platform.machine()}，此脚本仅支持 x86_64。")
    sys.exit(1)

shellcode = (
    b"\x48\xc7\xc0\x01\x00\x00\x00" # mov rax, 1
    b"\x48\xc7\xc7\x01\x00\x00\x00" # mov rdi, 1
    b"\x48\x8d\x35\x12\x00\x00\x00" # lea rsi, [rip+18]
    b"\x48\xc7\xc2\x06\x00\x00\x00" # mov rdx, 6
    b"\x0f\x05"                     # syscall
    b"\x48\xc7\xc0\x3c\x00\x00\x00" # mov rax, 60
    b"\x0f\x05"                     # syscall
    b"\x68\x65\x6c\x6c\x6f\x0a"     # "hello\n"
)


def run_shellcode(code):
    """
    运行shellcode
    """
    # 1. 加载 libc，因为需要mmap
    try:
        libc = ctypes.CDLL("libc.so.6")
    except OSError:
        try:
            libc = ctypes.CDLL("libc.so")
        except Exception as e:
            print(f"错误：无法加载 libc: {e}")
            sys.exit(1)

    # 定义类型别名 (修复 c_off_t 问题)
    # 在 x86_64 Linux 上，off_t 是 long (64-bit)
    c_off_t = ctypes.c_long
    
    # 设置 mmap 参数和返回类型
    libc.mmap.restype = ctypes.c_void_p
    libc.mmap.argtypes = [
        ctypes.c_void_p,  # addr
        ctypes.c_size_t,  # length
        ctypes.c_int,     # prot
        ctypes.c_int,     # flags
        ctypes.c_int,     # fd
        c_off_t           # offset (修复点)
    ]
    
    # 设置 mprotect 参数和返回类型
    libc.mprotect.restype = ctypes.c_int
    libc.mprotect.argtypes = [
        ctypes.c_void_p,
        ctypes.c_size_t,
        ctypes.c_int
    ]

    # 常量
    PROT_READ  = 0x1
    PROT_WRITE = 0x2
    PROT_EXEC  = 0x4
    MAP_PRIVATE   = 0x02
    MAP_ANONYMOUS = 0x20
    
    length = len(code)
    MAP_FAILED = ctypes.c_void_p(-1)

    # --- 1. 分配内存 (RW) ---
    print("[*] 调用 mmap 分配内存...")
    addr = libc.mmap(
        0, 
        length, 
        PROT_READ | PROT_WRITE, 
        MAP_PRIVATE | MAP_ANONYMOUS, 
        -1, 
        0
    )

    if addr == MAP_FAILED or addr is None:
        errno = ctypes.get_errno()
        print(f"[-] mmap 失败: {os.strerror(errno)} (Error {errno})")
        sys.exit(1)

    print(f"[+] 内存分配成功: {hex(addr.value if isinstance(addr, ctypes.c_void_p) else addr)}")

    # --- 2. 写入数据 ---
    # 确保传入 memmove 的是整数地址
    addr_val = addr.value if isinstance(addr, ctypes.c_void_p) else addr
    ctypes.memmove(addr_val, code, length)
    print("[+] Shellcode 写入完成")

    # --- 3. 修改权限 (RW -> RX) ---
    print("[*] 调用 mprotect 设置可执行权限...")
    ret = libc.mprotect(addr_val, length, PROT_READ | PROT_EXEC)
    
    if ret != 0:
        errno = ctypes.get_errno()
        print(f"[-] mprotect 失败: {os.strerror(errno)}")
        print("    提示：内核可能禁止 WX 内存页。尝试 'sudo setenforce 0' 或检查 dmesg。")
        sys.exit(1)
    
    print("[+] 权限修改成功")

    # --- 4. 执行 ---
    print("[!] 正在执行 Shellcode...")
    FUNC_TYPE = ctypes.CFUNCTYPE(None)
    fn = FUNC_TYPE(addr_val)
    
    try:
        fn()
    except Exception as e:
        print(f"[-] 执行异常: {e}")


import struct
import os
import stat

def create_executable_elf(shellcode, output_filename):
    """
    创建一个包含 shellcode 的最小化 Linux x86_64 ELF 可执行文件。
    """
    # --- 1. 定义 ELF 常量 (x86_64) ---
    EI_MAG = b"\x7fELF"
    EI_CLASS = 2          # 64-bit
    EI_DATA = 1           # Little Endian
    EI_VERSION = 1
    EI_OSABI = 0          # UNIX System V
    ET_EXEC = 2           # Executable file
    EM_X86_64 = 62        # AMD x86-64
    PT_LOAD = 1           # Loadable segment
    PF_X = 1              # Execute permission
    PF_R = 4              # Read permission
    PF_W = 2              # Write permission (通常代码段不需要写，但为了简单我们给 RWX 或 RX)
    
    # --- 2. 计算布局 ---
    # ELF 头大小固定为 64 字节
    EHDR_SIZE = 64
    # 程序头表 (Program Header) 紧跟在 ELF 头后面，大小 56 字节
    PHDR_SIZE = 56
    # 代码偏移量 = 头大小 + 程序头大小
    CODE_OFFSET = EHDR_SIZE + PHDR_SIZE
    
    # 内存加载地址 (通常设为 0x400000，这是 Linux 默认的用户空间基址)
    LOAD_ADDR = 0x400000
    
    # 文件总大小
    FILE_SIZE = CODE_OFFSET + len(shellcode)
    
    # --- 3. 构建 ELF 头 (64 字节) ---
    ehdr = bytearray(EHDR_SIZE)
    
    # e_ident (16 字节)
    ehdr[0:4] = EI_MAG
    ehdr[4] = EI_CLASS
    ehdr[5] = EI_DATA
    ehdr[6] = EI_VERSION
    ehdr[7] = EI_OSABI
    # 其余填充 0
    
    # e_type (2 字节) @ offset 16
    struct.pack_into("<H", ehdr, 16, ET_EXEC)
    # e_machine (2 字节) @ offset 18
    struct.pack_into("<H", ehdr, 18, EM_X86_64)
    # e_version (4 字节) @ offset 20
    struct.pack_into("<I", ehdr, 20, 1)
    # e_entry (8 字节) @ offset 24 -> 入口点虚拟地址 = 加载基址 + 代码偏移
    entry_point = LOAD_ADDR + CODE_OFFSET
    struct.pack_into("<Q", ehdr, 24, entry_point)
    # e_phoff (8 字节) @ offset 32 -> 程序头表偏移 = 64
    struct.pack_into("<Q", ehdr, 32, EHDR_SIZE)
    # e_shoff (8 字节) @ offset 40 -> 无段表，设为 0
    struct.pack_into("<Q", ehdr, 40, 0)
    # e_flags (4 字节) @ offset 48
    struct.pack_into("<I", ehdr, 48, 0)
    # e_ehsize (2 字节) @ offset 52
    struct.pack_into("<H", ehdr, 52, EHDR_SIZE)
    # e_phentsize (2 字节) @ offset 54 -> 单个程序头大小 56
    struct.pack_into("<H", ehdr, 54, PHDR_SIZE)
    # e_phnum (2 字节) @ offset 56 -> 1 个程序头
    struct.pack_into("<H", ehdr, 56, 1)
    # e_shentsize, e_shnum, e_shstrndx (略，设为 0)
    
    # --- 4. 构建程序头 (Program Header, 56 字节) ---
    phdr = bytearray(PHDR_SIZE)
    
    # p_type (4 字节) @ offset 0
    struct.pack_into("<I", phdr, 0, PT_LOAD)
    # p_flags (4 字节) @ offset 4 -> 读 + 执行 (RX)
    # 注意：如果 shellcode 需要自修改，需加上 PF_W
    struct.pack_into("<I", phdr, 4, PF_R | PF_X)
    # p_offset (8 字节) @ offset 8 -> 文件中的偏移
    struct.pack_into("<Q", phdr, 8, CODE_OFFSET)
    # p_vaddr (8 字节) @ offset 16 -> 内存虚拟地址
    struct.pack_into("<Q", phdr, 16, LOAD_ADDR + CODE_OFFSET)
    # p_paddr (8 字节) @ offset 24 -> 物理地址 (忽略，同 vaddr)
    struct.pack_into("<Q", phdr, 24, LOAD_ADDR + CODE_OFFSET)
    # p_filesz (8 字节) @ offset 32 -> 文件中该段的大小
    struct.pack_into("<Q", phdr, 32, len(shellcode))
    # p_memsz (8 字节) @ offset 40 -> 内存中该段的大小
    struct.pack_into("<Q", phdr, 40, len(shellcode))
    # p_align (8 字节) @ offset 48 -> 对齐方式 (通常 0x1000)
    struct.pack_into("<Q", phdr, 48, 0x1000)
    
    # --- 5. 组装并写入文件 ---
    elf_data = bytes(ehdr) + bytes(phdr) + shellcode
    
    with open(output_filename, "wb") as f:
        f.write(elf_data)
    
    
    # 赋予执行权限 (chmod +x)
    os.chmod(output_filename, os.stat(output_filename).st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    
    print(f"[+] 成功生成可执行文件: {output_filename}")
    print(f"    文件大小: {len(elf_data)} 字节")
    print(f"    入口点: {hex(entry_point)}")
    print(f"    运行命令: {output_filename}")
    
    
if __name__ == "__main__":
    print(f"平台: {platform.system()} {platform.machine()}")
    run_shellcode(shellcode)
    print("程序结束。")
    
    create_executable_elf(shellcode, "/tmp/x20260225")
    
    