#!/opt/homebrew/bin/python3
import os
import argparse
import subprocess
import datetime

dt_now = datetime.datetime.now()
def read_file(path):
    with open(path) as f: 
        return f.read()

def write_fault_test_result(test_case,got,expect):
    with open("./result.txt","a") as f:
        f.write(
f"""
{"=" * 100}
{test_case} {datetime.datetime.now().time()}
{"=" * 100}
{got}


"""
        )
    pass

def red_s(s):
    return f"\033[31m{s}\033[0m"
def green_s(s):
    return f"\033[32m{s}\033[0m"

def check_test(test_in_file,test_out_file,binfile):
    stdin = read_file(test_in_file)
    expect = read_file(test_out_file)
    stdout=""
    return_code=0
    try:
        cp = subprocess.run(
            [binfile], 
            input=stdin,
            # capture_output=True, text=True, 
            stdout=subprocess.PIPE,
            encoding='UTF-8',
            timeout=1.5
        )
        stdout=cp.stdout 
        return_code = cp.returncode
    except subprocess.TimeoutExpired:
        print(f"{red_s("timeout")} :", test_in_file)
        return

    if return_code != 0:
        print(f"{red_s("return_code")}: ", return_code, test_in_file)
        return False
        
    if expect != stdout:
        print(f"{red_s("fault")} test:", test_in_file)
        write_fault_test_result(test_in_file,stdout,expect)
        return False
    else:
        print(f"{green_s("pass")} test:",test_in_file)
        return True

def get_num_tests(name):
    test_dir_files = os.listdir(f"./{name}/test")
    return len(test_dir_files) / 2

def compile(task,main_file):
    out_dir = "./.dist"
    os.makedirs(out_dir,exist_ok=True)

    outfile = f"{out_dir}/{task}.out"
    subprocess.run(
        ["c++",main_file,"-I","./mylib","-o",outfile]
    )
    
    print(green_s("success compile!!"))
    return outfile

def main(args):
    main_file = f"./{args.name}/main.cpp"
    num_tests = int(get_num_tests(args.name))
    
    bin_file = compile(args.name,main_file)

    for i in range(1,num_tests + 1):
        check_test(f"./{args.name}/test/sample-{i}.in",f"./{args.name}/test/sample-{i}.out",bin_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    
    args = parser.parse_args()
    main(args)