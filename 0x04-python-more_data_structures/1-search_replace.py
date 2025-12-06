"""Module documentation for 1-search_replace.py."""
#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """search_replace - Function documentation.
    
    Args:
        my_list: Description of my_list.
        search: Description of search.
        replace: Description of replace.
    
    Returns:
        Description of the return value.
    """
    def find_search(element):
        """find_search - Function documentation.
        
        Args:
            element: Description of element.
        
        Returns:
            Description of the return value.
        """
        return element if element != search else replace
    return list(map(find_search, my_list))
