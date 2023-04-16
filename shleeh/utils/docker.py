import docker as docker_api


def is_docker_running():
    try:
        client = docker_api.from_env()
        client.ping()
        return True
    except Exception:
        return False
