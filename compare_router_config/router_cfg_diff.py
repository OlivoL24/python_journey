import difflib

def compare_router_configs(config1, config2):
  """Compares two router configurations and returns a list of differences.

  Args:
    config1: The first router configuration.
    config2: The second router configuration.

  Returns:
    A list of differences between the two router configurations.
  """
  differences = []
  for line in difflib.unified_diff(
      config1.splitlines(),
      config2.splitlines(),
      "config1",
      "config2",
      lineterm=""):
    if line.startswith("+"):
      differences.append("Added: " + line[1:])
    elif line.startswith("-"):
      differences.append("Removed: " + line[1:])
  return differences

def main():
  # Get the names of the router configurations from the user.
  config1_name = input("Enter the name of the first router configuration: ")
  config2_name = input("Enter the name of the second router configuration: ")

  # Read the router configurations from files.
  with open(config1_name, "r") as f:
    config1 = f.read()
  with open(config2_name, "r") as f:
    config2 = f.read()

  # Compare the router configurations and print the differences.
  differences = compare_router_configs(config1, config2)
  for difference in differences:
    print(difference)

if __name__ == "__main__":
  main()