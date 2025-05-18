import pkg_resources

   
def is_library_installed(library_name):
   installed_packages = pkg_resources.working_set
   installed_packages_list = [pkg.key for pkg in installed_packages]
   return library_name in installed_packages_list

# Example usage
library_name = 'numpy'
if is_library_installed(library_name):
   print(f"{library_name} is installed.")
else:
   print(f"{library_name} is not installed.")