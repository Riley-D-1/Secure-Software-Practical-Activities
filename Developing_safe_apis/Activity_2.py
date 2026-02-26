def check_api_key(key):
    if key == "mysecret" or key == "key2" or key == "key1":
        return True
    else:
        return False

# Modify so it accepts any key from: ["key1", "key2", "mysecret"]
print(check_api_key("wrongkey"))  # False

#Completed
 