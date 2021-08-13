from subprocess import check_output
import colorama


print(f"Setup for {colorama.Style.BRIGHT}BitBuild{colorama.Style.NORMAL}")
print("This is the setup application for BitBuild")


if should_continue.upper() == "Y":
    print("Continuing installation")
else:
    print("Installation terminated!")