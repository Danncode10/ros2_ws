# Workflow

This repo exists so the ROS 2 practice workspace can be tested cleanly inside Ubuntu while the course notes can still be edited on macOS.

## Recommended Setup

Use two separate repos:

```text
~/ros2-fundamentals-tutorial   # lessons and course material
~/ros2_ws                      # ROS 2 build and test workspace
```

## macOS Editing

Use macOS for comfortable editing with Codex or Claude.

After editing, save work with Git:

```bash
git status
git add .
git commit -m "Describe the change"
git push
```

## Ubuntu Testing

Use Ubuntu for ROS 2 commands:

```bash
cd ~/ros2_ws
git pull
source /opt/ros/jazzy/setup.bash
colcon build
source install/setup.bash
```

## Why Not Build in a Shared Folder

Shared folders are useful for quick transfers and screenshots, but they can make ROS 2 builds harder to debug.

Possible issues:

- slower file access;
- permission differences;
- symlink behavior;
- paths with spaces;
- generated folders syncing when they do not need to.

Git gives a cleaner history and a cleaner transfer path between macOS and Ubuntu.

## What Goes in `src/`

ROS 2 packages go in:

```text
src/
```

For example:

```text
src/rover_core/
src/rover_interfaces/
```

These packages will be added as the course progresses.
