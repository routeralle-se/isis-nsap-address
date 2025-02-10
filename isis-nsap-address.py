import re
from jinja2 import Environment, FileSystemLoader

# load the template environment
env = Environment(loader=FileSystemLoader("."))

# testing the concept
def ip_address_to_isis_system_id(ip_address: str) -> str:
    """
    Convert an IP address to an ISIS system ID format.
    """
    padded_octets = [f"{x:>03}" for x in ip_address.split(".")]
    joined_octets = "".join(padded_octets)
    result = ".".join(re.findall("....", joined_octets))
    return result

# test concept with jinja2
def create_isis_nsap_address(ip_address: str, area_id: str, template_name: str) -> str:
    """
    Render a Jinja2 template with the given IP address.

    Args:
        area_id (str): The area ID for the NSAP address
        ip_address (str): The IP address to process.
        template_name (str): The Jinja2 template file name.

    Returns:
        str: Rendered template output.
    """
    template = env.get_template(template_name)
    return template.render(ip_address=ip_address, area_id=area_id)

def main():
    ip_address = input("Enter IP address to convert: ")
    isis_system_id_native = ip_address_to_isis_system_id(ip_address=ip_address)
    print(".".join(["49.0000", isis_system_id_native, "00"]))

    output_jinja2_template = create_isis_nsap_address(area_id="49.0000", ip_address=ip_address, template_name="dnac.j2")
    print(output_jinja2_template)

if __name__ == "__main__":
    main()