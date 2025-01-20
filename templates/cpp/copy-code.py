#!/opt/homebrew/bin/python3
import argparse
import subprocess
def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("task")
    args = parser.parse_args()



    main_file_content = ""
    with open(f"./{args.task}/main.cpp") as f:
        main_file_content = f.read()

    lib_file_content = ""
    with open(f"./mylib/mylib.cpp") as f:
        lib_file_content = f.read()

    main_file_content = main_file_content.replace(
        "#include <../mylib/mylib.hpp>",
        lib_file_content
    )
    subprocess.run("pbcopy", input=main_file_content, text=True)


main()