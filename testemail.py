import foodemail

# name of recipient
recipient = ["kl9@princeton.edu", "cloudsrpretty168@gmail.com"]

# get menu
import menus
[categories, foods] = menus.scrape('frist')

# Create the body of the message (a plain-text and an HTML version).
text = ', '.join(categories)
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are recipient?<br>
       Here is the <a href="http://www.python.org">link</a> recipient wanted.
    </p>
  </body>
</html>
"""
foodemail.send_email(recipient, text, html)