td_version: str = "2023.12120"
project_file: str = "./TouchDesigner/dev-env.toe"
dest_dir: str = "release"
log_file: str = f"{dest_dir}/latest/log.txt"
latest_dir: str = f"{dest_dir}/latest"

env_vars: dict = {
    "SM_BUILD": "TRUE",
    "SM_PRIVACY": "FALSE",
    "SM_SAVE_PATH": latest_dir
}
