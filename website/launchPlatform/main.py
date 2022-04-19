import smtplib, ssl, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    
    receiver_email = str(environ.get('QUERY_STRING'))
    receiver_email = receiver_email.replace("email=", "")
    receiver_email = receiver_email.replace("%40", "@")
    
    port = 465 #SSL PORT
    smtp_server = "www.maxprudhomme.com"
    sender_email = "rick@maxprudhomme.com"
    password = "TimeToRickNRoll"
    
    message = MIMEMultipart("alternative")
    message["Subject"] = "Time to Rick N' Roll freaking nerds"
    message["From"] = sender_email
    message["To"] = receiver_email
    
    #Plain Text Version

    text = """\
    Gotcha !

    https://youtu.be/dQw4w9WgXcQ

    Have a good day,
    Jacky
    """

    #HTML Version

    html = """\
    <!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <meta name="x-apple-disable-message-reformatting">
    <title></title>
    <!--[if mso]>
  <noscript>
    <xml>
      <o:OfficeDocumentSettings>
        <o:PixelsPerInch>96</o:PixelsPerInch>
      </o:OfficeDocumentSettings>
    </xml>
  </noscript>
  <![endif]-->
    <style>
        table,
        td,
        div,
        h1,
        p {
            font-family: Arial, sans-serif;
        }
    </style>
</head>

<body style="margin:0;padding:0;">
    <table role="presentation"
        style="width:100%;border-collapse:collapse;border:0;border-spacing:0;background:#ffffff;">
        <tr>
            <td align="center" style="padding:0;">
                <table role="presentation"
                    style="width:602px;border-collapse:collapse;border:1px solid #cccccc;border-spacing:0;text-align:left;">
                    <tr>
                        <td align="center" style="padding:40px 0 30px 0;background:rgb(41, 37, 43);">
                            <svg width="500" height="225" xmlns="http://www.w3.org/2000/svg">
                                <rect x="2" y="2" width="496" height="221"
                                    style="fill:#dedede;stroke:#555555;stroke-width:2" /><text x="50%" y="50%"
                                    font-size="18" text-anchor="middle" alignment-baseline="middle"
                                    font-family="monospace, sans-serif" fill="#555555">Jacky Industry Logo</text>
                            </svg>
                        </td>
                    </tr>
                    <tr>
                        <td style="padding:36px 30px 42px 30px;background: rgb(51, 51, 51);">
                            <table role="presentation"
                                style="width:100%;border-collapse:collapse;border:0;border-spacing:0;">
                                <tr>
                                    <td style="padding:0 0 36px 0;color:white;">
                                        <h1
                                            style="font-size:30px;margin:0 0 2px 0; text-align: center; font-family:Arial,sans-serif;">
                                            Rick Rolling since 1969</h1>

                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding:0;">
                                        <table role="presentation"
                                            style="width:100%;border-collapse:collapse;border:0;border-spacing:0;">
                                            <tr>
                                            <p style="color: white; text-align: center">Momma never told ya that you should never give your adress to stranger ?</p>
                                                <img src="https://www.maxprudhomme.com/whyDidUSavedThisPicture.jpg"
                                                    style="margin: 0 51px 0 51px;">
                                                <p style="color: white;text-align: center;"><br>Gratz on making it this far !<br> Hope you enjoyed our project, thanks for your support !</p>
                                                <p style="color:white;text-align: center;">Click <a
                                                        style="text-decoration: none; color: lightblue"
                                                        href="https://bit.ly/3vxgUem">here</a>
                                                    to unsubscribe !</p>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                    <tr>
                        <td style="padding:30px;background:rgb(41, 37, 43);">
                            <table role="presentation"
                                style="width:100%;border-collapse:collapse;border:0;border-spacing:0;font-size:9px;font-family:Arial,sans-serif;">
                                <tr>
                                    <td style="padding:0;width:50%;" align="left">
                                        <p
                                            style="margin:0;font-size:14px;line-height:16px;font-family:Arial,sans-serif;color:#ffffff;">
                                            &reg; Jacky Industry, 69 Cartman Street,<br>South Park 2022
                                        </p>
                                    </td>
                                    <td style="padding:0;width:50%;" align="right">
                                        <table role="presentation"
                                            style="border-collapse:collapse;border:0;border-spacing:0;">
                                            <tr>
                                                <td style="padding:0 0 0 10px;width:38px;">
                                                    <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" style="color:#ffffff;">
                                                        <svg xmlns="http://www.w3.org/2000/svg"
                                                            enable-background="new 0 0 32 32" viewBox="0 0 32 32"
                                                            style="filter: invert(100%) sepia(2%) saturate(7%) hue-rotate(348deg) brightness(101%) contrast(103%);">
                                                            <rect width="539" height="176" x="-18" y="-20"
                                                                fill="#F3EEE9" display="none" />
                                                            <path
                                                                d="M22,3H10c-3.86,0-7,3.14-7,7v12c0,3.86,3.14,7,7,7h12c3.86,0,7-3.14,7-7V10C29,6.14,25.86,3,22,3z M27,22c0,2.757-2.243,5-5,5H10c-2.757,0-5-2.243-5-5V10c0-2.757,2.243-5,5-5h12c2.757,0,5,2.243,5,5V22z M16,10c-3.309,0-6,2.691-6,6s2.691,6,6,6s6-2.691,6-6S19.309,10,16,10z M16,20c-2.206,0-4-1.794-4-4s1.794-4,4-4s4,1.794,4,4S18.206,20,16,20z M24,9.5c0,0.828-0.672,1.5-1.5,1.5S21,10.328,21,9.5S21.672,8,22.5,8S24,8.672,24,9.5z" />
                                                        </svg>
                                                    </a>
                                                </td>
                                                <td style="padding:0 0 0 10px;width:38px;">
                                                    <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" style="color:#ffffff;">
                                                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
                                                            style="filter: invert(100%) sepia(2%) saturate(7%) hue-rotate(348deg) brightness(101%) contrast(103%);">
                                                            <path
                                                                d="M8.145 21.449c-2.15 0-4.638-.552-7.39-2.097-.208-.117-.304-.364-.23-.59s.297-.375.533-.342c1.814.208 3.795-.217 5.275-1.086-1.695-.398-3.065-1.499-3.788-3.098a.499.499 0 0 1 .08-.536c.13-.148.334-.205.522-.148.218.067.435.113.644.138-1.287-.768-2.665-2.238-2.665-4.441a.5.5 0 0 1 .814-.389c.16.13.331.239.508.325a5.362 5.362 0 0 1-.869-1.817c-.332-1.282-.139-2.582.557-3.756a.501.501 0 0 1 .821-.057c1.472 1.839 4.088 4.061 8.294 4.466-.078-1.331.322-3.512 2.16-4.585 2.261-1.32 4.436-1.15 6.305.487.828-.184 2.135-.752 2.406-.941a.5.5 0 0 1 .77.538c-.125.471-.408.995-.76 1.463.279-.083.514-.167.639-.231a.5.5 0 0 1 .652.711c-.588.93-1.539 1.796-2.174 2.266.343 4.225-2.126 8.946-6.089 11.577-1.47.975-3.886 2.143-7.015 2.143zM3.15 19.406c5.351 2.195 9.403.428 11.456-.935 3.756-2.494 6.067-6.988 5.62-10.929a.498.498 0 0 1 .222-.474c.269-.177.68-.502 1.094-.905-.407.088-.802.147-1.089.148-.276-.033-.447-.169-.492-.405a.498.498 0 0 1 .306-.559c.283-.113.665-.454.995-.872-.566.219-1.178.413-1.628.478a.497.497 0 0 1-.413-.131c-1.578-1.482-3.362-1.658-5.306-.524-1.745 1.02-1.784 3.397-1.6 4.148a.499.499 0 0 1-.513.619C7.331 8.829 4.427 6.719 2.68 4.773a3.808 3.808 0 0 0-.132 2.344c.294 1.133 1.034 2.002 1.596 2.33a.5.5 0 0 1-.153.922 3.106 3.106 0 0 1-1.752-.185c.521 2.085 2.689 3.067 3.299 3.135a.501.501 0 0 1 .268.879c-.437.369-1.091.547-1.828.51.836 1.114 2.132 1.754 3.681 1.788a.5.5 0 0 1 .323.872c-1.228 1.1-2.99 1.823-4.832 2.038z" />
                                                        </svg>
                                                    </a>
                                                </td>
                                                <td style="padding:0 0 0 10px;width:38px;">
                                                    <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" style="color:#ffffff;">
                                                        <svg xmlns="http://www.w3.org/2000/svg"
                                                            enable-background="new 0 0 512 512" viewBox="0 0 512 512"
                                                            style="filter: invert(100%) sepia(2%) saturate(7%) hue-rotate(348deg) brightness(101%) contrast(103%);">
                                                            <polygon fill="none"
                                                                points="222.1 313.9 322.3 256 222.1 198.1" />
                                                            <path fill="none"
                                                                d="M443.2,98.2c-55.9-3.7-146.9-7.1-187.2-7.1s-131.3,3.5-187.2,7.1c-24,1.6-42.8,21.6-42.8,45.7v224.2
                                                            c0,24,18.8,44.1,42.8,45.7c55.9,3.7,146.9,7.1,187.2,7.1s131.3-3.5,187.2-7.1c24-1.6,42.8-21.6,42.8-45.7V143.9
                                                            C486,119.9,467.2,99.8,443.2,98.2z M347.3,264.7l-130.2,75.2c-1.5,0.9-3.3,1.3-5,1.3s-3.5-0.4-5-1.3c-3.1-1.8-5-5.1-5-8.7V180.8
                                                            c0-3.6,1.9-6.9,5-8.7s6.9-1.8,10,0l130.2,75.2c3.1,1.8,5,5.1,5,8.7C352.3,259.6,350.4,262.9,347.3,264.7z" />
                                                            <path d="M444.5,78.3c-56.3-3.7-147.9-7.2-188.5-7.2s-132.3,3.5-188.5,7.2C33,80.5,6,109.4,6,143.9v224.2
                                                            c0,34.5,27,63.4,61.5,65.6c56.3,3.7,147.9,7.2,188.5,7.2s132.3-3.5,188.5-7.2c34.5-2.3,61.5-31.1,61.5-65.6V143.9
                                                            C506,109.4,479,80.5,444.5,78.3z M486,368.1c0,24-18.8,44.1-42.8,45.7c-55.9,3.7-146.9,7.1-187.2,7.1s-131.3-3.5-187.2-7.1
                                                            c-24-1.6-42.8-21.6-42.8-45.7V143.9c0-24,18.8-44.1,42.8-45.7c55.9-3.7,146.9-7.1,187.2-7.1s131.3,3.5,187.2,7.1
                                                            c24,1.6,42.8,21.6,42.8,45.7V368.1z" />
                                                            <path d="M347.3,247.3l-130.2-75.2c-3.1-1.8-6.9-1.8-10,0s-5,5.1-5,8.7v150.4c0,3.6,1.9,6.9,5,8.7
                                                            c1.5,0.9,3.3,1.3,5,1.3s3.5-0.4,5-1.3l130.2-75.2c3.1-1.8,5-5.1,5-8.7C352.3,252.4,350.4,249.1,347.3,247.3z M222.1,313.9V198.1
                                                            L322.3,256L222.1,313.9z" />
                                                        </svg>
                                                    </a>
                                                </td>
                                                <td style="padding:0 0 0 10px;width:38px;">
                                                    <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" style="color:#ffffff;">
                                                        <svg xmlns="http://www.w3.org/2000/svg"
                                                            enable-background="new 0 0 100 100" viewBox="0 0 100 100"
                                                            style="filter: invert(100%) sepia(2%) saturate(7%) hue-rotate(348deg) brightness(101%) contrast(103%);">
                                                            <path
                                                                d="M64.193 47.63c2.334 0 4.465 1.302 5.698 3.484.256.452.726.706 1.21.706 1.029.026 1.747-1.183 1.208-2.074-1.708-3.019-4.818-4.894-8.117-4.894-12.607.418-12.524 19.726 0 20.216 5.312 0 9.473-4.44 9.473-10.108-.033-1.828-2.747-1.825-2.779 0 0 4.11-2.94 7.329-6.695 7.329C55.358 61.976 55.299 47.89 64.193 47.63zM44.737 54.982c.211-5.297-4.149-10.216-9.474-10.131-12.608.419-12.523 19.727 0 20.215C40.576 65.067 44.737 60.627 44.737 54.982zM28.569 54.959c-.157-6.239 7.012-9.771 11.312-5.363 4.305 4.223 1.52 12.82-4.618 12.693C31.573 62.288 28.569 59.001 28.569 54.959z" />
                                                            <path
                                                                d="M86.094,24.562c-10.864-8.869-24.123-9.672-24.451-8.483c0,0-1.11,1.268-1.11,1.268c-0.669,0.722-0.299,1.989,0.647,2.245
                                                            c0.674,0.202,1.328,0.409,1.965,0.62c-9.388-1.933-19.11-1.551-28.487,0.298c1.233-0.426,2.539-0.838,3.918-1.229
                                                            c0.946-0.234,1.333-1.5,0.688-2.227c-0.411-0.44-1.054-1.537-1.83-1.45c-0.02-0.083-12.775,0.089-23.438,8.957
                                                            c-0.078,0.141-1.943,3.515-4.18,9.224c-0.626,1.723,1.884,2.697,2.587,1.014c1.821-4.647,3.413-7.747,3.883-8.63
                                                            c4.241-3.105,8.396-4.973,11.883-6.096c-7.792,3.468-11.499,6.977-11.703,7.174c-1.146,1.104,0.232,2.987,1.629,2.22
                                                            c18.938-10.094,43.589-10.543,62.559,0.004c1.369,0.775,2.794-1.151,1.615-2.231c-0.222-0.211-4.747-4.436-14.232-8.206
                                                            c4.014,0.839,9.827,2.756,15.764,7.133c1.277,2.416,10.979,21.53,11.101,44.45c-1.563,2.222-8.137,10.217-22.156,10.904
                                                            c-0.682-0.818-2.069-2.485-3.488-4.216c9.308-3.242,12.995-9.069,13.157-9.332c0.773-1.24-0.729-2.707-1.947-1.889
                                                            C62.612,77.828,38.071,77.51,20.207,66.105c-1.166-0.879-2.784,0.641-1.983,1.861c0.156,0.257,3.703,5.949,12.729,9.243
                                                            c-1.455,1.805-2.906,3.551-3.608,4.393c-8.549-0.112-18.133-4.802-22.157-10.959c0.048-9.99,1.869-20.379,5.411-30.886
                                                            c0.569-1.73-2.029-2.612-2.632-0.888c-3.59,11.159-5.989,22.27-5.37,32.881c0.288,0.493,7.253,12.084,25.33,12.656
                                                            c0.424,0.014,0.834-0.168,1.107-0.494c0.03-0.035,2.975-3.538,5.339-6.532c0.612-0.734,0.225-1.943-0.693-2.192
                                                            c4.547,1.498,20.09,4.356,32.365,0.304c-0.616,0.444-0.728,1.402-0.237,1.981c2.357,2.907,5.217,6.324,5.245,6.358
                                                            c0.275,0.327,0.651,0.51,1.11,0.497c16.405-0.52,23.844-10.359,25.241-12.444C98.707,47.531,86.21,24.87,86.094,24.562z" />
                                                        </svg>
                                                    </a>
                                                </td>
                                            </tr>



                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>

</html>
    """
    
    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)
    
    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    return "You should not see that. Don't know how you ended up here."