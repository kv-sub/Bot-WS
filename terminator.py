import subprocess
import time

def run_commands_in_split_panes(command_list):
    subprocess.Popen(["terminator", "--maximize"])
    time.sleep(3)  
    if len(command_list)>1:
        for i, cmd in enumerate(command_list):
            if i % 2 == 1:
                subprocess.run(["xdotool", "key", "ctrl+shift+e"])
            else:
                subprocess.run(["xdotool", "key", "ctrl+shift+o"])
            time.sleep(1)  

            full_cmd = f"source ~/bot_ws/install/setup.bash && {cmd}" 
            subprocess.run(["xdotool", "type", "--delay", "1", full_cmd])
            subprocess.run(["xdotool", "key", "Return"])
            time.sleep(2)  
    else:
        for i,cmd in enumerate(command_list):
            full_cmd = f"source ~/bot_ws/install/setup.bash && {cmd}" 
            subprocess.run(["xdotool", "type", "--delay", "1", full_cmd])
            subprocess.run(["xdotool", "key", "Return"])
            time.sleep(2)

commands = {
    "commands": [
        "ros2 launch kv_bot launch_sim.launch.py world:=./src/kv_bot/worlds/obstacles.world",
        "ros2 launch kv_bot online_async_launch.py use_sim_time:=true",  
        "ros2 run rviz2 rviz2 -d src/kv_bot/config/main.rviz --ros-args -p use_sim_time:=true"
    ],
    "command2": [
        "ros2 run teleop_twist_keyboard teleop_twist_keyboard"
    ]
}

run_commands_in_split_panes(commands["commands"])
run_commands_in_split_panes(commands["command2"])
