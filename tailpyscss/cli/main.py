import argparse
from tailpyscss.cli.commands.init import init_project
from tailpyscss.cli.commands.build import build_project
from tailpyscss.cli.commands.watch import watch_project
from tailpyscss.cli.commands.setup import setup_windows_path

def main():
    parser = argparse.ArgumentParser(description="TailPySCSS CLI")
    parser.add_argument("command", choices=["init", "build", "watch", "setup-path"], help="Command to run")
    
    args = parser.parse_args()
    
    if args.command == "init":
        init_project()
    elif args.command == "build":
        build_project()
    elif args.command == "watch":
        watch_project()
    elif args.command == "setup-path":
        setup_windows_path()

if __name__ == "__main__":
    main()
