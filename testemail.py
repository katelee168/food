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
  <body style="font-family: &quot;HelveticaNeue-Light&quot;, &quot;Helvetica Neue&quot;;">
    <div class="outside">
      <div id="greeting" style="color: white;font-size: 24px;font-family: &quot;HelveticaNeue-Light&quot;, &quot;Helvetica Neue&quot;;background-color: #F76609;padding: 50px 15px 20px 15px;">
        Good morning, Sunshine
      </div>
      </div>
      <div class="container dhall" style="padding: 20px 15px;margin-bottom: 15px;margin-left: 10%;width: -webkit-calc(80% - 30px);font-family: &quot;HelveticaNeue-Light&quot;, &quot;Helvetica Neue&quot;;font-size: 14px;">
        <p class="dhall-header" style="-webkit-margin-before: 0em;-webkit-margin-after: 0em;color: #4AA176;font-size: 24px;">Frist</p>
        Ants on a log</br>
        Yule Log
      </div>

    <div id="footer" style="background-color: #34425C;color: white;padding: 15px;font-size: 13px;">
      Learn more or unsubscribe: dining.princeton@gmail.com
    </div>
  </body>
</html>
"""
foodemail.send_email(recipient, text, html)