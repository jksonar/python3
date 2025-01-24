# **1. What is py2exe?**

`py2exe` is a Python library used to convert Python scripts (`.py` files) into standalone Windows executable files (`.exe`). This allows you to distribute your Python application without requiring the user to install Python on their system.

---

### **Key Features**

- Creates standalone `.exe` files that can be run on Windows.
- Packages all required dependencies into a single directory.
- Supports GUI and console-based Python applications.

---

### **Installing py2exe**

You can install `py2exe` using pip:

```bash
pip install py2exe
```

> Note: `py2exe` supports Python 3.4 to 3.10. Ensure your Python version is compatible.

---

### **Steps to Use py2exe**

#### **1. Create a Python Script**

Prepare the Python script (`example.py`) that you want to convert to an executable. For example:

```python
# example.py
print("Hello, World!")
```

---

#### **2. Create a `setup.py` File**

Create a `setup.py` file to configure `py2exe`. This script tells `py2exe` how to process your Python file.

```python
# setup.py
from setuptools import setup
import py2exe

setup(
    console=['example.py'],  # Replace 'example.py' with your script's name
)
```

- **`console`:** For console applications (command-line).
- **`windows`:** For GUI applications (no console window).

---

#### **3. Build the Executable**

Run the `setup.py` script from the command line to create the executable:

```bash
python setup.py py2exe
```

- A `dist` directory will be created, containing:
  - The `.exe` file for your script.
  - Supporting files and dependencies.

---

#### **4. Distribute the Application**

You can distribute the contents of the `dist` directory to others. They can run the `.exe` file without installing Python.

---

### **Advanced Configuration**

You can customize the `setup.py` file for more complex requirements:

#### **a. Exclude Unused Modules**

```python
setup(
    console=['example.py'],
    options={
        'py2exe': {
            'excludes': ['tkinter', 'unittest'],  # Exclude unnecessary modules
        }
    }
)
```

#### **b. Bundle Files into a Single Executable**

You can bundle everything into a single `.exe` file:

```python
setup(
    console=['example.py'],
    options={
        'py2exe': {
            'bundle_files': 1,  # Bundle all files into one executable
            'compressed': True  # Compress the executable
        }
    },
    zipfile=None  # No external ZIP file
)
```

---

### **Limitations**

- **Windows Only:** `py2exe` is designed for Windows systems.
- **Large Executables:** The `.exe` file might be large because it includes Python and dependencies.
- **Active Development:** Some newer Python features may not be fully supported.

---

### **Alternatives to py2exe**

If `py2exe` does not suit your needs, consider these alternatives:

- **PyInstaller:** Supports multiple platforms (Windows, macOS, Linux).
- **cx_Freeze:** Cross-platform with support for Python 3.
- **Nuitka:** Converts Python code into C for better performance.

---

# **2. What is PyInstaller?**

PyInstaller is a great tool to package Python scripts into standalone executables. Here’s a step-by-step guide to using PyInstaller to create a build:

---

### **1. Install PyInstaller**

```bash
pip install pyinstaller
```

---

### **2. Basic Usage - Create a Simple Executable**

```bash
pyinstaller your_script.py
```

- This will generate a **dist/** directory with the executable inside.

---

### **3. Generate a Single Executable (One-File Build)**

```bash
pyinstaller --onefile your_script.py
```

- The `--onefile` option creates a single executable (all dependencies packed inside).
- The resulting file is larger but portable.

---

### **4. Add Custom Icon to Executable**

```bash
pyinstaller --onefile --icon=app_icon.ico your_script.py
```

- Use the `--icon` option to include an `.ico` file as the app icon.

---

### **5. Suppress Terminal (For GUI Applications)**

```bash
pyinstaller --onefile --noconsole your_gui_script.py
```

- `--noconsole` (or `--windowed`) prevents the console from opening (useful for GUI apps).

---

### **6. Specify Output Directory**

```bash
pyinstaller --onefile --distpath ./build_output your_script.py
```

- Saves the executable in `./build_output`.

---

### **7. Include Additional Files (e.g., Configs, Images)**

```bash
pyinstaller --onefile --add-data 'config.ini;.' your_script.py
```

- The format is `source;destination` (on Windows, use `;`, on Linux/Mac use `:`).

---

### **8. Use a .spec File for Custom Builds**

```bash
pyinstaller your_script.py --onefile
```

- This generates a `.spec` file. Modify it for advanced configurations.
- Rebuild using:
  ```bash
  pyinstaller your_script.spec
  ```

---

### **9. Example: Full Command**

```bash
pyinstaller --onefile --noconsole --icon=app.ico --add-data 'config.yaml;.' my_script.py
```

---

### **10. Test the Executable**

- Go to the `dist/` directory and run:
  ```bash
  ./your_script
  ```

---

### **Common Issues**

1. **Missing Modules**

   - Use `--hidden-import` to manually include hidden imports.

   ```bash
   pyinstaller --onefile --hidden-import=module_name script.py
   ```

2. **DLL/Library Not Found**
   - Use `--paths` to include the library path.
   ```bash
   pyinstaller --onefile --paths /path/to/library script.py
   ```

---

# **3. Simple Examples**

Let's walk through an example to package a simple Python script into an executable using PyInstaller.

---

### **Step 1: Create a Sample Python Script**

Create a script called `hello.py`:

```python
# hello.py
print("Hello, World!")
input("Press Enter to exit...")
```

---

### **Step 2: Install PyInstaller**

```bash
pip install pyinstaller
```

---

### **Step 3: Package the Script into an Executable**

Run the following command:

```bash
pyinstaller --onefile hello.py
```

- `--onefile` creates a single executable.
- The executable will be generated in the `dist/` directory.

---

### **Step 4: Test the Executable**

- On Windows:
  ```bash
  dist\hello.exe
  ```
- On Linux/Mac:
  ```bash
  ./dist/hello
  ```

---

### **Adding an Icon (Optional)**

1. Prepare an `.ico` file (for Windows) or `.icns` (for Mac).
2. Run:
   ```bash
   pyinstaller --onefile --icon=app_icon.ico hello.py
   ```

---

### **Suppress Console (For GUI Apps)**

If your script uses a GUI (like Tkinter), prevent the terminal from showing:

```bash
pyinstaller --onefile --noconsole hello.py
```

---

### **Include Additional Files**

Suppose `hello.py` uses a config file (`config.yaml`). Include it like this:

```bash
pyinstaller --onefile --add-data "config.yaml;." hello.py
```

---

### **Customizing the Build with .spec File**

After the first build, a `.spec` file is generated:

```bash
pyinstaller hello.py
```

- Modify the `.spec` file to add hidden imports, paths, etc.
- Rebuild using:

```bash
pyinstaller hello.spec
```

---

### **Check the Final Output**

Go to the `dist/` directory and run the executable:

```bash
dist/hello
```

---

# **4. What is Nuitka?**

Guide to using **Nuitka** to compile Python code into a standalone executable.

---

Nuitka is a **Python-to-C** compiler that compiles Python scripts into highly optimized executable binaries. It can also package everything (Python interpreter, dependencies) into a single file.

---

### **Step 1: Install Nuitka**

```bash
pip install nuitka
```

For Windows:

```bash
pip install nuitka --user
```

---

### **Step 2: Create a Simple Python Script**

Create a file `app.py`:

```python
# app.py
print("Hello from Nuitka!")
input("Press Enter to exit...")
```

---

### **Step 3: Compile the Script with Nuitka**

Run the following command:

```bash
nuitka --standalone --onefile app.py
```

- `--standalone` – Creates an independent folder with all dependencies.
- `--onefile` – Packs everything into a single executable.

---

### **Step 4: Run the Executable**

- Windows:
  ```bash
  dist\app.exe
  ```
- Linux/Mac:
  ```bash
  ./app
  ```

---

### **Advanced Options**

#### **Add Icon (Optional)**

```bash
nuitka --standalone --onefile --windows-icon-from-ico=app_icon.ico app.py
```

#### **Suppress Console (For GUI Apps)**

```bash
nuitka --standalone --onefile --windows-disable-console app.py
```

#### **Optimize Performance**

```bash
nuitka --standalone --onefile --lto --clang app.py
```

- `--lto` – Enables link-time optimization.
- `--clang` – Uses Clang for better optimization.

---

### **Include Additional Files**

To include extra files (like config files):

```bash
nuitka --standalone --onefile --include-data-file=config.yaml=./config.yaml app.py
```

---

### **Testing the Build**

Run the generated executable:

```bash
./dist/app
```

---

### **Advantages of Nuitka**

- Faster execution than PyInstaller.
- Full Python compliance (no bytecode, everything is compiled).
- Generates optimized C code.

---
