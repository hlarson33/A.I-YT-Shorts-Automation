#manual clipper to cut video clips into shorts for YT
from pathlib import Path
import subprocess
def get_output_path(file_path):
        while True:
            output_name = input("Enter the output file name (without extension): ").strip()

            # Remove the .mp4 extension if provided
            if output_name.lower().endswith(".mp4"):
                output_name = output_name[:-4]

            # Reject an empty name
            if output_name == "":
                print("Error: Output file name cannot be empty.")
                continue

            # Reject folder paths
            if "\\" in output_name or "/" in output_name:
                print("Error: Output file name cannot contain path separators.")
                continue

            output_file = file_path.with_name(f"{output_name}.mp4")

            # Ask again if the output already exists
            if output_file.exists():
                print(f"Warning: {output_file} already exists.")
                continue

            # All checks passed
            return output_file

def main():
    # Ask for the input video
    file = input("Enter the file path: ")
    file_path = Path(file)

    if not file_path.is_file():
        print("Error: File not found.")
        raise SystemExit

    start_time = input("Enter the start time (in seconds): ")
    end_time = input("Enter the end time (in seconds): ")

    print(f"Clip: {file_path} from {start_time} to {end_time}")

    # Convert times to numbers
    try:
        start_time = float(start_time)
        end_time = float(end_time)
    except ValueError:
        print("Error: Please enter valid numbers for the times.")
    else:
        # Validate the times
        if start_time < 0 or end_time < 0:
            print("Error: Start and end times must be non-negative.")

        elif start_time >= end_time:
            print("Error: Start time must be less than end time.")

        else:
            duration = end_time - start_time
            print(f"Duration: {duration} seconds")

            output_file = get_output_path(file_path)
            print(output_file)

            # Build the FFmpeg command
            command = [
                "ffmpeg",
                "-n",
                "-ss",
                str(start_time),
                "-i",
                str(file_path),
                "-t",
                str(duration),
                str(output_file),
            ]

            # Run the command and handle potential errors
            try:
                subprocess.run(command, check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error: ffmpeg failed with error: {e}")
                raise SystemExit
            except FileNotFoundError:
                print(
                    "Error: ffmpeg not found. Please ensure ffmpeg "
                    "is installed and in your PATH."
                )
                raise SystemExit
            else:
                print(f"Clip created successfully: {output_file}")
if __name__ == "__main__":
    main()