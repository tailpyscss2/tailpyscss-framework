
import sys
import subprocess
import site
import os

def setup_windows_path():
    """
    Adds the Python Scripts directory to the Windows PATH.
    """
    if sys.platform != "win32":
        print("Auto-setup is only for Windows.")
        return

    scripts_dir = os.path.join(site.getuserbase(), "Scripts")
    
    # Check if already in PATH
    current_path = os.environ.get("PATH", "")
    if scripts_dir.lower() in current_path.lower():
        print(f"[*] PATH check passed: {scripts_dir} is already in PATH.")
        return

    print(f"[*] Adding {scripts_dir} to User PATH...")
    
    # PowerShell command to persist the change
    ps_command = (
        f"[Environment]::SetEnvironmentVariable('Path', "
        f"[Environment]::GetEnvironmentVariable('Path', [EnvironmentVariableTarget]::User) + ';{scripts_dir}', "
        f"[EnvironmentVariableTarget]::User)"
    )
    
    try:
        subprocess.run(["powershell", "-Command", ps_command], check=True)
        print("[+] Success! Please restart your terminal to use 'tailpyscss'.")
    except subprocess.CalledProcessError as e:
        print(f"[-] Failed to update PATH: {e}")
