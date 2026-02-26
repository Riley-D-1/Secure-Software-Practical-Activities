import re
import html

def sanitise_comment(comment):
    comment = re.sub(r'<(script|img).*?>.*?</(script|img)>', '', comment, flags=re.I|re.S)
    return html.escape(comment)

# Extend this to also remove <img> tags before escaping.
print(sanitise_comment('<script>alert(1)</script>Hi!'))
# Completed