#!/opt/homebrew/bin/python3
import os
import argparse
import subprocess

def red_s(s):
    return f"\033[31m{s}\033[0m"
def green_s(s):
    return f"\033[32m{s}\033[0m"

def write_preprocessed_main(out_file):
    main_file_content = ""
    with open(f"main.cpp") as f:
        main_file_content = f.read()

    lib_file_content = ""
    with open(f"../mylib/mylib.cpp") as f:
        lib_file_content = f.read()

    main_file_content = main_file_content.replace(
        "#include <../mylib/mylib.hpp>",
        lib_file_content
    )
    

    with open(out_file,"w") as f:
        f.write(main_file_content)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("task")
    args = parser.parse_args()
    
    
    out_dir = "./.dist"
    os.makedirs(out_dir,exist_ok=True)

    os.chdir(args.task)
    out_file = f"../.dist/submit-{args.task}.cpp"
    write_preprocessed_main(out_file)
    cp = subprocess.run(
        ["acc","submit",out_file,"--","--no-open"],
        input=f"abc{args.task}",
        encoding='UTF-8',
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    
    if cp.returncode == 0:
        print(green_s("success submit!"))
    else:
        print(green_s("fail submit!"))
        print(cp.stdout,cp.stderr)

    

main()