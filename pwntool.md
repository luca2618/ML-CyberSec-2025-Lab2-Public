

# 🐍 Pwntools Function Guide

## ▶ Process / Remote

**`process(path)`** — run local binary

```python
p = process("./vuln")
```

**`remote(host, port)`** — connect to remote

```python
p = remote("host", 1337)
```

---

## ▶ Sending Data

**`send(data)`** — send raw bytes

```python
p.send(b"A")
```

**`sendline(data)`** — send + newline

```python
p.sendline(b"hello")
```

**`sendafter(delim, data)`** — wait → send

```python
p.sendafter(b"> ", b"A")
```

**`sendlineafter(delim, data)`**

```python
p.sendlineafter(b"Name:", b"A")
```

---

## ▶ Receiving Data

**`recv()`** — read anything

```python
p.recv()
```

**`recvline()`** — read one line

```python
p.recvline()
```

**`recvuntil(delim)`** — read until delimiter

```python
p.recvuntil(b": ")
```

---

## ▶ Switch to Interactive

**`interactive()`** — get shell

```python
p.interactive()
```

---

# 🔧 Binary / ELF Functions

**`ELF(path)`** — parse ELF binary

```python
elf = ELF("./vuln")
```

**`elf.symbols[name]`** — get symbol address

```python
elf.symbols["main"]
```

**`elf.plt[name]`** — PLT entry

```python
elf.plt["puts"]
```

**`elf.got[name]`** — GOT entry

```python
elf.got["puts"]
```

**`elf.search(bytes)`** — find byte pattern

```python
next(elf.search(b"/bin/sh"))
```

---

# 🔐 Packing / Unpacking

**`p64(x)`** — pack 64-bit

```python
p64(0xdeadbeef)
```

**`u64(bytes)`** — unpack 64-bit

```python
u64(b"A\x00\x00\x00\x00\x00\x00\x00")
```

**`flat([...])`** — flatten payload

```python
flat([b"A"*40, 0xdeadbeef])
```

---

# 🔍 Pattern Tools

**`cyclic(n)`** — generate crash pattern

```python
cyclic(200)
```

**`cyclic_find(value)`** — find offset

```python
cyclic_find(0x6161616c)
```

---

# 🧱 ROP Tools

**`ROP(elf)`** — create ROP object

```python
rop = ROP(elf)
```

**`rop.find_gadget(list)`**

```python
rop.find_gadget(["pop rdi", "ret"])[0]
```

**`rop.call(func, args)`**

```python
rop.call("system", [binsh])
```

**`rop.chain()`**

```python
rop.chain()
```

---

# 🐚 Shellcode

**`asm(shellcraft.sh())`**

```python
shellcode = asm(shellcraft.sh())
```

**`asm("assembly")`**

```python
asm("nop; nop; ret")
```

---

# 🔎 Libc Handling

**`ELF("libc.so.6")`**

```python
libc.symbols["system"]
```

**`next(libc.search(b"/bin/sh"))`**

```python
next(libc.search(b"/bin/sh"))
```

---

# 🧰 Format String Helper

**`fmtstr_payload(offset, writes)`**

```python
fmtstr_payload(6, {elf.got["printf"]: elf.symbols["win"]})
```

---

# 🐞 Debugging

**`gdb.attach(proc, gdbscript="...")`**

```python
gdb.attach(p, "b *main")
```

---

# ⏱ Timeout Controls

**`timeout=` parameter**

```python
p.recv(timeout=1)
```

---
