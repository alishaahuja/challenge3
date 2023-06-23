def get_value_from_nested_object(obj, key):
    keys = key.split('/')
    current_obj = obj
    try:
        for k in keys:
            current_obj = current_obj[k]
        return current_obj
    except (KeyError, TypeError):
        return None

# Example usage:
object1 = {"a": {"b": {"c": "d"}}}
key1 = "a/b/c"
value1 = get_value_from_nested_object(object1, key1)
print(value1)  # Output: d

object2 = {"x": {"y": {"z": "a"}}}
key2 = "x/y/z"
value2 = get_value_from_nested_object(object2, key2)
print(value2)  # Output: a
