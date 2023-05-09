# シンプルなコマンドラインタスク管理くん🐶

## 環境構築

- pyenv と pyenv-virtualenv を使用します

```shell
cd /path/to/habit_app
pyenv virtualenv 3.9.9 habit_app
pyenv local habit_app

pip install -U pip setuptools wheel poetry
```

```shell
poetry install
```

## 動かし方

```
🐱❯ habit-app --help
usage: habit-app [-h] [--task-pkl TASK_PKL] {add,show,done} ...

Task manager app

positional arguments:
  {add,show,done}
    add                Add a task
    show               Show all tasks
    done               Mark a task as done

optional arguments:
  -h, --help           show this help message and exit
  --task-pkl TASK_PKL  Path to the task information
```

### タスクの追加

```shell
🐱❯ habit-app add "test task 1"
Task added
```

### タスクの確認

```shell
🐱❯ habit-app show
1: test task 1 (not done)
```

### タスクの完了

```shell
🐱❯ habit-app done 1
Task 1 marked as done

# 指定した task id が `done` となっている
🐱❯ habit-app show
1: test task 1 (done)
```

### Optional: タスク情報を指定する

- `--task-pkl` にタスク情報を保存する場所を指定

```shell
🐱❯ habit-app --task-pkl my-task.pkl add "my task 1"
Task added

🐱❯ habit-app --task-pkl my-task.pkl show
1: my task 1 (not done)
```