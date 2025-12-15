from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install
import sys
import os
import subprocess
import site

def post_install_setup():
    """
    Automagically add Python Scripts to Windows PATH if missing.
    Feature requested to ensure 'tailpyscss' command works immediately.
    """
    if sys.platform != "win32":
        return

    try:
        # Get the User Base Scripts directory
        # e.g. C:\Users\name\AppData\Roaming\Python\Python313\Scripts
        user_base = site.getuserbase()
        scripts_dir = os.path.join(user_base, "Scripts")

        if not os.path.isdir(scripts_dir):
            return

        # Check current PATH
        current_path = os.environ.get("PATH", "")
        
        # Normalize for comparison
        norm_scripts = os.path.normcase(scripts_dir)
        norm_path = os.path.normcase(current_path)

        if norm_scripts not in norm_path:
            print(f"[*] TailPySCSS Auto-Setup: Adding {scripts_dir} to User PATH...")
            
            # Use PowerShell to persistently set the User Environment Variable
            # [Environment]::SetEnvironmentVariable("Path", $newPath, "User")
            
            ps_command = (
                f"$current = [Environment]::GetEnvironmentVariable('Path', 'User');"
                f"$new = $current + ';{scripts_dir}';"
                f"[Environment]::SetEnvironmentVariable('Path', $new, 'User')"
            )
            
            result = subprocess.run(
                ["powershell", "-Command", ps_command],
                capture_output=True, text=True
            )
            
            if result.returncode == 0:
                print(f"[*] SUCCESS: Added to PATH. Please RESTART your terminal to use 'tailpyscss'.")
            else:
                print(f"[!] Warning: Failed to update PATH automatically. Error: {result.stderr}")
        else:
            print("[*] PATH check passed: Scripts directory already in PATH.")
            
    except Exception as e:
        print(f"[!] Auto-Setup Warning: Could not check/update PATH: {e}")

class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        develop.run(self)
        post_install_setup()

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        post_install_setup()

setup(
    name="tailpyscss",
    version="0.5.0",
    packages=find_packages(),
    install_requires=[
        "libsass>=0.22.0",
        "watchdog>=2.1.0",
    ],
    entry_points={
        "console_scripts": [
            "pywind=tailpyscss.cli:main",
            "tailpyscss=tailpyscss.cli:main",
        ],
    },
    cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand,
    },
    author="Abdi Abdikarim",
    description="A Python-native utility-first CSS generator and compiler.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tailpyscss2/tailpyscss-framework",
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Flask",
        "Framework :: Django",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    project_urls={
        "Source": "https://github.com/tailpyscss2/tailpyscss-framework",
    },
    keywords=[
        "css",
        "scss",
        "tailwind",
        "utility",
        "design system",
        "python css",
        "jinja css",
        "no node css",
        "python tailwind alternative",
        "style framework",
        "ui framework",
        "python styling framework"
    ],
)
