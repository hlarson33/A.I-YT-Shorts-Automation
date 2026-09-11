#manual clipper to cut video clips into shorts for YT
from pathlib import Path
import subprocess

#asks for user input on video clipping parameters
file = input("Enter the file path: ")
file_path = Path(file)
if not file_path.is_file():
    print("Error: File not found.")
    raise SystemExit
start_time = input("Enter the start time (in seconds): ")
end_time = input("Enter the end time (in seconds): ")

#prints it back to the user for confirmation
print(f"Clip: {file_path} from {start_time} to {end_time}")

#change times to numbers and calculate duration
try:
    start_time = float(start_time)
    end_time = float(end_time)
except ValueError:
    print("Error: Please enter valid numbers for the times.")
else:
    #validate the times
    if start_time < 0 or end_time < 0:
        print("Error: Start and end times must be non-negative.")

    elif start_time >= end_time:
        print("Error: Start time must be less than end time.")

    else:
        duration = end_time - start_time
        print(f"Duration: {duration} seconds")
        output_file = file_path.with_name("clip.mp4")
        if output_file.exists():
            print(f"Warning: {output_file} already exists ")
            raise SystemExit
        print(output_file)
        # Call ffmpeg to create the clip
        command = ["ffmpeg", "-n", "-ss", str(start_time), "-i", str(file_path), "-t", str(duration), str(output_file)]
        subprocess.run(command, check=True)

