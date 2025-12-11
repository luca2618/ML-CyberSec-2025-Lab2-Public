

# radare2 Symbols Quick Guide

## 1. Open Binary and Analyze

```bash
r2 ./vuln
[0x00000000]> aaa        # auto-analysis (functions, xrefs, etc.)
[0x00000000]> afl        # list functions
[0x00000000]> is         # list symbols
```

---

## 2. Get Address of `main` / `win`

```bash
[0x00000000]> is~main           # filter symbols containing "main"
[0x00000000]> afl~main          # filter functions containing "main"

[0x00000000]> s sym.main        # seek to main
[0x00400560]> ?v $$             # print current address as value
```

Or directly:

```bash
[0x00000000]> ?v sym.main       # show numeric value of sym.main
[0x00000000]> ?v sym.win
```

---

## 3. PLT and GOT Entries

```bash
[0x00000000]> is~plt            # symbols in .plt
[0x00000000]> is~got            # symbols in .got

[0x00000000]> afl~sym.imp.puts  # imported puts() (like libc puts)
[0x00000000]> ?v sym.imp.puts   # its address
```

---

## 4. Disassemble a Function by Symbol Name

```bash
[0x00000000]> pdf @ sym.main    # print disasm of main()
[0x00000000]> pdf @ sym.win     # print disasm of win()
```

---

## 5. Search Symbols by Name

```bash
[0x00000000]> is~secret         # any symbol containing "secret"
[0x00000000]> afl~secret        # any function containing "secret"
```

---

## 6. Get Symbol Addresses Programmatically (r2pipe + Python)

```python
import r2pipe

r2 = r2pipe.open("./vuln")
r2.cmd("aaa")

# list functions (JSON)
funcs = r2.cmdj("aflj")

for f in funcs:
    if "main" in f["name"]:
        print("main at:", hex(f["offset"]))

# get address of sym.win directly
win = r2.cmdj('fdj sym.win')  # may be empty if not used
```

*(Or simply parse `isj` / `aflj` JSON outputs to get symbol/function addresses.)*

---

