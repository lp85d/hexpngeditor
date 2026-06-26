import os
import ctypes
import sys

# Указываем путь к cairo.dll вручную перед импортом cairosvg
cairo_dll_path = r"C:\Windows\System32\cairo.dll"

if os.path.exists(cairo_dll_path):
    # Загружаем cairo.dll вручную
    ctypes.CDLL(cairo_dll_path)
    print(f"Loaded: {cairo_dll_path}")
    
    # Пробуем переименовать для совместимости
    new_path = r"C:\Windows\System32\libcairo-2.dll"
    if not os.path.exists(new_path):
        try:
            import shutil
            shutil.copy2(cairo_dll_path, new_path)
            print(f"Copied to: {new_path}")
        except Exception as e:
            print(f"Could not copy: {e}")
            print("Please manually copy cairo.dll to libcairo-2.dll in C:\\Windows\\System32\\")
else:
    print("cairo.dll not found in System32")

# Теперь пробуем импортировать
try:
    import cairosvg
    print("cairosvg imported successfully!")
    
    # Конвертируем
    svg_path = r"C:\s6\horse-head.svg"
    output_dir = r"C:\s6"
    
    sizes = [16, 32, 48, 64, 128, 256]
    
    for size in sizes:
        output_path = os.path.join(output_dir, f"horse-head-{size}.png")
        cairosvg.svg2png(
            url=svg_path,
            write_to=output_path,
            output_width=size,
            output_height=size
        )
        print(f"Created {size}x{size} PNG: {output_path}")
    
    print("\nDone!")

except Exception as e:
    print(f"Still error: {e}")
    print("\nLet's try parsing SVG directly...")
    
    # Запасной вариант с парсингом SVG
    exec(open(r"D:\deepseek_python_20260626_fallback.py").read() if os.path.exists(r"D:\deepseek_python_20260626_fallback.py") else "print('Fallback not found')")