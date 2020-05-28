#utf8

#轻量级配置文件，配置文件应该以utf8编码存储

import toml
toml_string = """
# This is a TOML document.

title = "TOML Example"

[owner]
name = "Tom Preston-Werner"
dob = 1979-05-27T07:32:00-08:00 # First class dates

[database]
server = "192.168.1.1"
ports = [ 8001, 8001, 8002 ]
connection_max = 5000
enabled = true

[servers]

# Indentation (tabs and/or spaces) is allowed but not required
[servers.alpha]
ip = "10.0.0.1"
dc = "eqdc10"

[servers.beta]
ip = "10.0.0.2"
dc = "eqdc10"

[clients]
data = [ ["gamma", "delta"], [1, 2] ]

# Line breaks are OK when inside arrays
hosts = [
  "中文又何妨",
  "omega"
]
"""

parsed_toml = toml.loads(toml_string)

#with open("test.toml") as f:
#    toml_string=f.read()
#
#toml.load(f)
#toml.load("./test.toml")



