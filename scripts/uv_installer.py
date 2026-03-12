from platform import system
import subprocess

def detectar_sistema():
    os_name = system().lower()

    if os_name == 'nt' or os_name == 'windows':
        print(f'Sistema detectado {os_name}')
        windows_powershell = 'powershell -ExecutionPolicy ByPass -c "irm ' \
        'https://astral.sh/uv/install.ps1 | iex"'
        subprocess.run(windows_powershell,shell=True)
    else:
        # Comando Linux/Mac Os
        print(f'Sistema detectado {os_name}')
        command = 'curl -LsSf https://astral.sh/uv/install.sh | sh'
        subprocess.run(command,shell=True)

if __name__ == "__main__":
    detectar_sistema()