import argparse
import datetime
import os
import pickle

# パーサを作る
parser = argparse.ArgumentParser(description="Task manager app")
parser.add_argument(
    "--task-pkl", default="./task.pkl", type=str, help="Path to the task information"
)

subparsers = parser.add_subparsers(dest="command")

# タスクの追加
add_parser = subparsers.add_parser("add", help="Add a task")
add_parser.add_argument("description", type=str, help="Task description")

# タスクの表示
show_parser = subparsers.add_parser("show", help="Show all tasks")

# タスクの完了処理
done_parser = subparsers.add_parser("done", help="Mark a task as done")
done_parser.add_argument("id", type=int, help="Task ID")

args = parser.parse_args()


# タスク管理(ID、説明、作成日、完了日を情報として持つ)


class Task:
    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.created_date = datetime.datetime.now()
        self.completed_date = None


if os.path.exists(args.task_pkl):
    with open(args.task_pkl, "rb") as rf:
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
        print(f"{task.id}: {task.description} ({status})")
elif args.command == "done":
    for task in tasks:
        if task.id == args.id:
            task.completed_date = datetime.datetime.now()
            print(f"Task {id} marked as done")
            break
else:
    print("Task not found")

# 保存
with open(args.task_pkl, "wb") as wf:
    pickle.dump({"tasks": tasks, "next_task_id": next_task_id}, wf)
