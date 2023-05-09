import argparse
import datetime
import os
import pathlib
import pickle
from dataclasses import dataclass
from typing import Optional


@dataclass
class Task(object):
    """
    タスク管理(ID、説明、作成日、完了日を情報として持つ)
    """

    task_id: int
    description: str
    created_date: datetime.datetime = datetime.datetime.now()
    completed_date: Optional[datetime.datetime] = None


def parse_args(prog: Optional[str] = None) -> argparse.Namespace:
    # パーサを作る
    parser = argparse.ArgumentParser(
        prog=prog,
        description="Task manager app",
    )
    parser.add_argument(
        "--task-pkl",
        type=pathlib.Path,
        default=pathlib.Path(__file__).resolve().parent / "task.pkl",
        help="Path to the task information",
    )

    subparsers = parser.add_subparsers(dest="command")

    # タスクの追加
    add_parser = subparsers.add_parser(
        "add",
        help="Add a task",
    )
    add_parser.add_argument(
        "description",
        type=str,
        help="Task description",
    )

    # タスクの表示
    subparsers.add_parser(
        "show",
        help="Show all tasks",
    )

    # タスクの完了処理
    done_parser = subparsers.add_parser(
        "done",
        help="Mark a task as done",
    )
    done_parser.add_argument(
        "id",
        type=int,
        help="Task ID",
    )
    return parser.parse_args()


def main(prog: Optional[str] = None) -> None:
    args = parse_args(prog=prog)

    if args.task_pkl.exists():
        with args.task_pkl.open("rb") as rf:
            task_dict = pickle.load(rf)
        tasks = task_dict["tasks"]
        next_task_id = task_dict["next_task_id"]
    else:
        tasks = []
        next_task_id = 1

    # サブコマンドの処理
    if args.command == "add":
        task = Task(next_task_id, args.description)
        tasks.append(task)
        next_task_id += 1
        print("Task added")

    elif args.command == "show":
        for task in tasks:
            status = "done" if task.completed_date else "not done"
            print(f"{task.task_id}: {task.description} ({status})")

    elif args.command == "done":
        for task in tasks:
            if task.task_id == args.id:
                task.completed_date = datetime.datetime.now()
                print(f"Task {task.task_id} marked as done")
                break
    else:
        print("Task not found")

    # 保存
    with args.task_pkl.open("wb") as wf:
        pickle.dump({"tasks": tasks, "next_task_id": next_task_id}, wf)
