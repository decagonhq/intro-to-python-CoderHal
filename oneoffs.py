def sizes(*args, **kwargs):
  args = list(args)
  size_list = []
  for key, value in kwargs.items():
    size_list.append(value)
  for arg in args:
      print(f"{arg} is available in {', '.join(size_list)}")
  
# TESTING THE FUNCTION
cloths = ('Skirt', 'Gown', 'Shirt')
available_sizes = {'XS': 'Xtra-small', 'S': 'Small', 'L': 'Large', 'XL': 'Xtra-large'}
# sizes('Skirt', 'Gown', 'Shirt', XS= 'Xtra-small', S= 'Small', L= 'Large', XL= 'Xtra-large')
sizes(*cloths, **available_sizes)

# LOGS
# 
# Skirt is available in Xtra-small, Small, Large, Xtra-large
# Gown is available in Xtra-small, Small, Large, Xtra-large
# Shirt is available in Xtra-small, Small, Large, Xtra-large
# 
    
