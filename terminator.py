import subprocess

def run_command_in_terminator(command):
    """Run a command in a new Terminator window."""
    subprocess.Popen(['terminator', '-e', f'bash -c "source ~/bot_ws/install/setup.bash; {command}; exec bash"'])

# Define the different commands
commands = {
    "gazebo_simulation": [
        "ros2 launch kv_bot launch_sim.launch.py world:=./src/kv_bot/worlds/obstacles.world"
    ],
    "rviz_simulation": [
        "ros2 run rviz2 rviz2 -d src/kv_bot/config/main.rviz --ros-args -p use_sim_time:=true",
        "ros2 launch kv_bot online_async_launch.py use_sim_time:=true"
    ],
    "ball_tracking": [
        "ros2 launch kv_bot ball_tracker.launch.py sim_mode:=true"
    ],
    "navigation": [
        "ros2 launch kv_bot navigation_launch.py use_sim_time:=true"
    ],
    "teleop": [
        "ros2 run teleop_twist_keyboard teleop_twist_keyboard"
    ]
}

def execute_gazebo_simulation():
    for cmd in commands["gazebo_simulation"]:
        run_command_in_terminator(cmd)

def execute_rviz_simulation():
    for cmd in commands["rviz_simulation"]:
        run_command_in_terminator(cmd)

def execute_ball_tracking():
    for cmd in commands["ball_tracking"]:
        run_command_in_terminator(cmd)

def execute_navigation():
    for cmd in commands["navigation"]:
        run_command_in_terminator(cmd)

def execute_teleop():
    for cmd in commands["teleop"]:
        run_command_in_terminator(cmd)

# Example of executing commands in new terminator windows
execute_gazebo_simulation()
execute_rviz_simulation()
