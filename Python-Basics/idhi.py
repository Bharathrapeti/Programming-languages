def update_config():
 with open("config.txt", "r") as file:
  content = file.read()
  content = content.replace("mode=debug", "mode=production")
 with open("config.txt", "w") as file:
  file.write(content)
  print("Configuration updated!")
# Example Usage
update_config()
