import subprocess
import json

def parse_traceroute(traceroute_output):
  """Parses the output of a traceroute command and returns a list of dictionaries.

  Args:
    traceroute_output: The output of the traceroute command.

  Returns:
    A list of dictionaries, where each dictionary represents a hop in the traceroute.
  """
  hops = []
  for line in traceroute_output.splitlines():
    if line.startswith("="):
      continue
    hop = {}
    hop["hop_number"] = line.split()[0]
    hop["ip_address"] = line.split()[1]
    hop["rtt"] = line.split()[2]
    hops.append(hop)
  return hops

def main():
  # Get the destination IP address from the user.
  destination_ip_address = input("Enter the destination IP address: ")

  # Run the traceroute command.
  traceroute_command = ["traceroute", destination_ip_address]
  traceroute_output = subprocess.check_output(traceroute_command).decode("utf-8")

  # Parse the traceroute output and save the results to a JSON file.
  traceroute_results = parse_traceroute(traceroute_output)
  with open("traceroute_results.json", "w") as f:
    json.dump(traceroute_results, f, indent=2)

if __name__ == "__main__":
  main()