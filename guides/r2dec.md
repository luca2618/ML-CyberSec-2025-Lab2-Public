
---

# 🔍 r2dec Guide (Radare2 Decompiler)

## 📦 Install r2dec

```bash
r2pm -i r2dec
```

Verify:

```bash
r2pm -s r2dec
```

---

# 🚀 Basic Usage

### Open a binary and analyze:

```bash
r2 ./binary
> aaa
```

### Decompile the current function:

```bash
> pdd
```

### Decompile a specific symbol:

```bash
> pdd @ sym.main
> pdd @ sym.win
```

### Decompile at an address:

```bash
> pdd @ 0x00400540
```

---

# 🎯 Navigation + Decompilation

### Seek to a symbol:

```bash
> s sym.main
```

Then decompile:

```bash
> pdd
```

### List functions:

```bash
> afl
```

### Decompile each function quickly:

```bash
> afl~main
> pdd @ <address>
```

---

# 🔧 Useful r2dec Commands

| Command          | Meaning                                    |
| ---------------- | ------------------------------------------ |
| `pdd`            | Decompile current function                 |
| `pdd @ addr`     | Decompile at address                       |
| `pdd @ sym.func` | Decompile named function                   |
| `pdg`            | (alias in newer versions; similar to pdd)  |
| `pdda`           | Decompile ALL functions (verbose)          |
| `aaa`            | Full analysis (required for decompilation) |

---

# 🧠 Improving Decompiler Output

### Rename variables:

```bash
> afvn var1 counter
```

### Rename functions:

```bash
> afr new_name @ sym.old_name
```

### Rename addresses:

```bash
> afn myfunc @ 0x00401020
```

### Add comments:

```bash
> CC Here is a comment
```

---

# 📤 Export Decompiled Code

### Output C-like code to a file:

```bash
> pdd > main.c
```

Or for a specific function:

```bash
> pdd @ sym.main > main.c
```

---

# 🔎 Searching for things to decompile

### Strings:

```bash
> iz
```

### Find references to a string:

```bash
> axt @ <string-address>
```

Then decompile callers:

```bash
> pdd @ <caller-address>
```

---

# 🛠 Quick Reverse Engineering Workflow

### 1. Open binary

```bash
r2 ./vuln
```

### 2. Analyze

```bash
aaa
```

### 3. List functions

```bash
afl
```

### 4. Decompile interesting ones

```bash
pdd @ sym.main
pdd @ sym.check_password
pdd @ sym.win
```

### 5. Rename for clarity

```bash
afn check @ sym.func_1234
```

### 6. Add comments

```bash
CC XOR loop here
```

---

# ⭐ Tips & Limitations

* r2dec works best with **unobfuscated** C binaries.
* Compiler optimizations (O2/O3) may make output messy.
* It’s **much lighter** than Ghidra or IDA.
* You can script r2dec using radare2 pipelines for automation.

---

