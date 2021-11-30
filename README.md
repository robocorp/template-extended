# README for the robot

Describe your robot here. E.g., what it does, what the requirements are, how to run it.

## Development guide

Run the robot locally:

```
rcc run
```

Provide access credentials for Control Room connectivity:

```
rcc configure credentials <your_credentials>
```

Upload to Control Room:

```
rcc cloud push --workspace <workspace_id> --robot <robot_id>
```

### Suggested directory structure

The directory structure given by the template:

```
├── devdata
├── keywords
│   └── keywords.robot
├── libraries
│   └── MyLibrary.py
├── variables
│   └── variables.py
├── conda.yaml
├── robot.yaml
└── tasks.robot
```

where

- `devdata`: A place for all data/material related to development, e.g., test data. Do not put any sensitive data here!
- `keywords`: Robot Framework keyword files.
- `libraries`: Python library code.
- `variables`: Define your robot variables in a centralized place. Do not put any sensitive data here!
- `conda.yaml`: Environment configuration file.
- `robot.yaml`: Robot configuration file.
- `tasks.robot`: Robot Framework task suite - high-level process definition.

In addition to these, you can create your own directories (e.g. `bin`, `tmp`). Add these directories to the `PATH` or `PYTHONPATH` section of `robot.yaml` if necessary.

Logs and artifacts are stored in `output` by default - see `robot.yaml` for configuring this.

Learn how to [handle variables and secrets](https://robocorp.com/docs/development-guide/variables-and-secrets/secret-management).

### Configuration

Give the task name and startup commands in `robot.yaml` with some additional configuration. See [Docs](https://robocorp.com/docs/setup/robot-structure#robot-configuration-file-robot-yaml) for more.

Put all the robot dependencies in `conda.yaml`. These are used for managing the execution environment.

### Additional documentation

See [Robocorp Docs](https://robocorp.com/docs/) for more documentation.
