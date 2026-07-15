# ros2_ws

ROS 2 learning workspace for the **ROS 2 Fundamentals Tutorial** course.

This repository is separate from the course notes repository:

- Course repo: `Danncode10/ros2-fundamentals-tutorial`
- Workspace repo: `Danncode10/ros2_ws`

Use this repo for ROS 2 practice packages that need to be cloned and tested inside Ubuntu.

## Why This Repo Exists

The course notes can be edited comfortably on macOS with Codex or Claude. ROS 2 commands should be tested inside Ubuntu, because ROS 2 Jazzy targets Ubuntu 24.04 in this course.

This repo gives you a clean Git-based workflow:

1. Edit lesson notes or package code on macOS.
2. Commit, stash, push, pull, or fetch with Git.
3. Clone or pull this repo inside Ubuntu.
4. Run `colcon build` and ROS 2 commands inside Ubuntu.

Do not use a VM shared folder as the main ROS 2 build workspace. Shared folders are useful for screenshots and quick file transfer, but ROS 2 builds are easier to troubleshoot inside Ubuntu's normal filesystem.

## Recommended Ubuntu Location

Clone this repository in Ubuntu as:

```bash
cd ~
git clone git@github.com:Danncode10/ros2_ws.git
cd ros2_ws
```

The workspace layout should be:

```text
ros2_ws/
├── src/
├── README.md
├── CLAUDE.md
├── AGENTS.md
└── docs/
```

ROS 2 packages go inside:

```text
src/
```

Generated folders are ignored by Git:

```text
build/
install/
log/
```

## First Build Check

In Ubuntu:

```bash
source /opt/ros/jazzy/setup.bash
cd ~/ros2_ws
colcon build
source install/setup.bash
```

For an empty workspace, `colcon build` may report:

```text
Summary: 0 packages finished
```

That is okay. It means the workspace is empty but the build tool works.

## Course Direction

This repo supports learning ROS 2 fundamentals first:

- workspaces
- packages
- Python nodes
- topics
- services
- custom interfaces
- parameters
- launch files
- CLI debugging

Future rover work can grow from these basics, but this repo should stay beginner-friendly and low-storage aware.
