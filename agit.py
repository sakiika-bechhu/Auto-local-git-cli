import json
from pathlib import Path
from typing import List

import click
import subprocess


def run_cmds(cmd_list: List):
    for cmd in cmd_list:
        res = subprocess.run(cmd, stdout=subprocess.PIPE)
        if res.stderr is not None:
            raise RuntimeError(res.stderr)


def get_config(cwd='./'):
    name_res = subprocess.run(["git", "config", "--get", "user.name"], cwd=cwd, stdout=subprocess.PIPE).stdout.decode("utf-8").replace('\n', '')
    email_res = subprocess.run(["git", "config", "--get", "user.email"], cwd=cwd, stdout=subprocess.PIPE).stdout.decode("utf-8").replace('\n', '')
    print(f'changed to {name_res} and {email_res}')


def read_config():
    filename = Path.home() / '.agit.json'
    if not filename.exists():
        raise RuntimeError("Create .git.json first")
    json_open = open(filename, 'r')
    config_dict = json.load(json_open)
    return config_dict


def change_local(items, cwd='.'):
    for key, value in items.items():
        cmd = ["git", "config", "--local", f"user.{key}", f"{value}"]
        res = subprocess.run(cmd, cwd=cwd, stdout=subprocess.PIPE)
        if res.stderr is not None:
            raise RuntimeError(res.stderr)


def set_local_name(cwd='.'):
    res = subprocess.run(["git", "config", "--get", "remote.origin.url"], cwd=cwd, stdout=subprocess.PIPE)
    remote_url = res.stdout.decode('utf-8')
    print(remote_url)
    if res.stderr is not None or remote_url == '':
        click.echo("Invalid directory")

    config_dict = read_config()
    change_keys = config_dict.keys()
    for change_key in change_keys:
        if change_key in remote_url:
            change_local(config_dict[change_key], cwd)


@click.group()
def cmd():
    pass


@cmd.command()
def local():
    set_local_name()


@cmd.command()
@click.argument('url', type=str, nargs=-1)
def clone(url):
    url = url[0]
    if url is None or url == '':
        raise RuntimeError('Specify url')
    subprocess.run(["git", "clone", url], stdout=subprocess.PIPE)
    dst = url.split('/')[-1].split('.git')[0]
    set_local_name(cwd=dst)
    get_config(cwd=dst)



