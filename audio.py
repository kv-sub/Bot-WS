import os
import pvporcupine
import pyaudio
import struct
import subprocess

# Path to your trained wake word model and PicoVoice access key
ACCESS_KEY = "KlH0k7A3ddN3WOIhK8ilbbPmeJDrw3dGvjry7FL19GRM76rAjb2q8g=="  # Replace with your actual access key
MODEL_PATH = "/home/kv/Desktop/Hey-Prabhu/Hey-Prabhu_en_linux_v3_0_0.ppn"  # Update with the correct path to your trained wake word model

# Path to the Python file to execute
PYTHON_FILE_PATH = "/home/kv/bot_ws/terminator.py"  # Replace with the actual path to the Python file

# Initialize Porcupine Wake Word Detection
def initialize_porcupine():
    return pvporcupine.create(
        access_key=ACCESS_KEY,
        keyword_paths=[MODEL_PATH]
    )

# Function to execute the Python file
def execute_python_file():
    """Execute the specified Python file when the wake word is detected."""
    subprocess.Popen(['python3', PYTHON_FILE_PATH])

# Main listening loop
def start_listening():
    porcupine = initialize_porcupine()
    pa = pyaudio.PyAudio()
    audio_stream = pa.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=porcupine.sample_rate,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    print("Listening for wake word...")
    try:
        while True:
            pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            # Process audio and detect wake word
            if porcupine.process(pcm) >= 0:
                print("Wake word detected!")

                # Execute the Python file when the wake word is detected
                execute_python_file()
                print("Executing Python file...")

                # Stop listening after executing the Python file
                break  # Breaks the loop and stops listening after execution

    except KeyboardInterrupt:
        print("Stopping...")
    except OSError as e:
        print(f"Error occurred: {e}")  # Gracefully handle the OSError
    finally:
        audio_stream.stop_stream()  # Ensure the stream is stopped
        audio_stream.close()  # Close the stream properly
        pa.terminate()  # Terminate the audio object
        porcupine.delete()  # Clean up Porcupine

if __name__ == "__main__":
    start_listening()
