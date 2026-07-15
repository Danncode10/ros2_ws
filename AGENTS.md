# Agent Instructions

This repository is a ROS 2 learning workspace used alongside the course repository:

```text
Danncode10/ros2-fundamentals-tutorial
```

Follow the course teaching priorities:

- Teach ROS 2 fundamentals before advanced robotics tools.
- Keep examples practical, hands-on, and beginner-friendly.
- Assume the learner is new to ROS 2.
- Prefer lightweight, low-storage workflows.
- Avoid Gazebo, Navigation2, MoveIt, Docker, YOLO, AI packages, large simulation worlds, or full desktop robotics stacks in beginner work unless clearly marked as future work.
- Use ROS 2 Jazzy on Ubuntu 24.04.
- Prefer Python beginner nodes with `rclpy`.
- Use `colcon` workspaces.

Workspace rules:

- Put ROS 2 source packages in `src/`.
- Do not commit generated `build/`, `install/`, or `log/` folders.
- Build and test inside Ubuntu, not inside a VM shared folder.
- Keep this repo focused on ROS 2 practice packages and small runnable examples.

When creating package examples, explain what to run, why it matters, and how to verify it with ROS 2 CLI commands.
