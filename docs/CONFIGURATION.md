# Configuring your workspace with BitBuild
Configuring BitBuild with your Project is easier than you think.
First of all, you need to create a configuration file named `Bitfile` in the root Directory of your project.
The configuration would be in a `JSON` Format.This expects two properties.
1) `type`: type of the target. Should be a value `dir` or `file`.
2) `targets`: This is an array which expects values in this order. 
```swift
["Target-file", (On_Modified_Action | On_Created_Action), (On_Deleted_Action)]
```

Example Configuration for watching a Directory.
- Type: Sets the type of target
- Targets[0] is the Path to watch changes
- Targets[1] Should be a command to run for a on_created event
- Targets[2] Should be a command to run for a on_deleted event
```json
{
    "type": "dir",
    "targets": [
        "./lib",
        "python file_created.py",
        "python file_deleted.py"
    ]
}
```

Example Configuration for watching a file.
- Type: Sets the type of target
- Targets[0] the Path to watch changes
- Targets[1] Should be a command to run for a on_created event
- Targets[2] Should be a command to run for a on_deleted event
```json
{
    "type": "file", 
    "targets": [
        "./main.py" ,
        "python Program.py", 
        "python Delete_Program.py" 
    ]
}
```

Supportive Links:
- See Supported File Extensions [here](https://github.com/Bit-Build/bitbuild/blob/main/Examples/CONFIGURATION.md#Supported-Files-Types).

# Supported-Files-Types
- `Bitfile`
- `Config.bitfile`
- `config.bitfile`
