import subprocess

def run_flyway_migration():
    cmd = ["/usr/local/bin/flyway", "-configFiles=/app/flyway.conf", "migrate"]
    subprocess.run(cmd, check=True)
