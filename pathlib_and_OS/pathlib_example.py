from os import chdir
from pathlib import Path


# Path.cwd()            current working dir
# Path.home()           users home dir 

# Create paths
# path = Path(f"{cwd}/example ")   
# path = Path("/usr") / "bin" / "python3"  = /usr/bin/python3
# path = Path("/usr").joinpath("bin", "python3")

# create a file 
# new_file = Path.cwd() / "settings.yaml"
# new_file.touch()

# writing to a file
# new_file.write_text("Hello World!")

# deleting a file
# new_file.unlink()

# with new_file.open() as file:
    #print(new_file.read())
# or
# text_content = new_file.read_text() // reads with all the spacings and line break

# useful for loading in yaml file as is 

# import yaml
# path = Path.cwd() / "settings.yaml"
# pasred_yaml = yaml.safe_load(path.read_text()) 


# creating a directory
# new_dir = Path.cwd() / "new_dir"
# new_dir.mkdir()

# changing to the new directory
# chdir(new_dir)

# # deleting a directory
# new_dir.rmdir()

# path = Path("settings.yaml")  //pick a file in current script runnning dir and resolve full path 
# full_path = path.resolve()

# full_path                 = /Users/emmanuel/Documents/projects/python_field/features/settings.yaml
# full_path.parent          = /Users/emmanuel/Documents/projects/python_field/features
# full_path.parent.parent   = /Users/emmanuel/Documents/projects/python_field
# full_path.name            = settings.yaml
# full_path.stem            = settings
# full_path.suffix          = .yaml

# full_path.is_dir()        = Checks if a path is a directory 
# full_path.is_file()       = checks if a path is a file 
# full_path.exists()        = checks if a path exists



def main() -> None:
   pass


if __name__ == "__main__":
    main()