from pathlib import Path
import argparse
import turtle

def parse_arguments():
    parser = argparse.ArgumentParser(description="Копіювання файлів з вихідної папки в папку призначення із сортуванням по розширенню файлів")
    parser.add_argument("source", help="Шлях до вихідної папки")
    parser.add_argument("destination", nargs='?', default="dist", help="Шлях до папки призначення (default: dist)")
    return parser.parse_args()


def copy_file(src, dst):
    try:
        for item in src.iterdir():
            print(item)
            if item.is_dir():
                # Рекурсивно копіюємо директорію
                new_dst = dst / item.name
                new_dst.mkdir(exist_ok=True)
                copy_file(item, new_dst)
            else:
                # Копіюємо файл
                file_extension = item.suffix[1:]  # Отримуємо розширення файлу без крапки
                if file_extension:
                    dest_subdir = dst / file_extension
                    dest_subdir.mkdir(exist_ok=True)
                    with item.open('rb') as src_file, (dest_subdir / item.name).open('wb') as dst_file:
                        dst_file.write(src_file.read())
                    print(f"Copied {item} to {dest_subdir / item.name}")
    except Exception as e:
        print(f"Помилка при копіюванні: {e}")

def main():
    args = parse_arguments()
    source_dir = Path(args.source)
    dest_dir = Path(args.destination)

    if not source_dir.exists():
        print(f"Директорія {source_dir} не існує.")
        return

    if not dest_dir.exists():
        dest_dir.mkdir(parents=True)

    copy_file(source_dir, dest_dir)
    print("Копіювання завершено.")

if __name__ == "__main__":
    main()