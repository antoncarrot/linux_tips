#!/usr/bin/env python

import re
import subprocess
import sys

SYNC_DIR = sys.argv[1]

_RCLONE_CMD = f"rclone bisync gdrive: {SYNC_DIR} -Mv --compare size,modtime,checksum --conflict-resolve newer --conflict-loser delete --recover --color NEVER"
RCLONE_CMD = _RCLONE_CMD.split()

_NOTIFY_CMD = "notify-send -u normal -t 10000 -a rclone"
NOTIFY_CMD = _NOTIFY_CMD.split()

NEW_FILE_MATCH = re.compile(r".*File is new\s+-\s(?P<file>.*)")
DEL_FILE_MATCH = re.compile(r".*File was deleted\s+-\s(?P<file>.*)")
MODIFY_FILE_MATCH = re.compile(r".*File changed.*-\s(?P<file>.*)")

MATCHES = {"New": NEW_FILE_MATCH, "Deleted": DEL_FILE_MATCH, "Modified": MODIFY_FILE_MATCH}


def get_changes(lines: str):
    ret = {name: [] for name in MATCHES.keys()}
    has_changes = False

    for line in lines.splitlines():
        for name, match in MATCHES.items():
            res = re.match(match, line)
            if res:
                ret[name].append(res.group("file"))
                has_changes = True
                continue
    return ret, has_changes


def main():
    proc = subprocess.run(RCLONE_CMD, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, text=True)
    print(proc.stdout, end="")
    if proc.returncode != 0:
        subprocess.run([*NOTIFY_CMD, "Syncing failed"])
        sys.exit(proc.returncode)

    changes, has_changes = get_changes(proc.stdout)
    if has_changes:
        changes_str = ";\n".join([f"{k}: {','.join(v)}" for k, v in changes.items() if v])
        subprocess.run([*NOTIFY_CMD, changes_str])


main()
