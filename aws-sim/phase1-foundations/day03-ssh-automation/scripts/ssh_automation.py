import paramiko
import logging

# Enable logging
logging.basicConfig(
    filename="ssh.log",
    level=logging.INFO,
    format="%(asctime)s %(message)s"
)

hosts = [
    "192.168.179.131",
    "192.168.179.132"
]

username = "clouduser"
command = "hostname && uptime"


def connect(host):
    logging.info(f"Connecting to {host}")
    print(f"\nConnecting to {host}")

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(
            hostname=host,
            username=username,
            timeout=10,
            allow_agent=True,
            look_for_keys=True
        )

        logging.info(f"Connected to {host}")

        stdin, stdout, stderr = ssh.exec_command(command)

        output = stdout.read().decode()
        error = stderr.read().decode()

        if output:
            print("OUTPUT:")
            print(output)

        if error:
            print("ERROR:")
            print(error)

        ssh.close()

    except Exception as e:
        logging.error(f"Failed {host}: {e}")
        print(f"Failed {host}: {e}")


for host in hosts:
    connect(host)
