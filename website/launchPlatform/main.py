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
        td,Elmao Industry
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
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 402.43 302"><defs><style>.cls-1,.cls-2{fill:#1d1d1b;stroke-width:2px;}.cls-1{stroke:#e30613;}.cls-1,.cls-2,.cls-3,.cls-4,.cls-5{stroke-miterlimit:10;}.cls-2{stroke:#f39200;}.cls-3{font-size:80px;font-family:Mexicanfiesta, Mexican fiesta;letter-spacing:0.1em;}.cls-3,.cls-4{fill:#f7ac63;stroke:#fbf5b7;}.cls-5{fill:#e41814;stroke:#e41814;}.cls-6{fill:#fbf4b0;}.cls-7{fill:#068537;}</style></defs><g id="Calque_2" data-name="Calque 2"><path class="cls-1" d="M700,401.62c-6.58-1.43-14.47-6.71-20-14.52-4.56-6.43-5.86-12-10-19.35-2.83-5.06-7.34-9.14-20-14.52V329c-48.38,6.13-79.68-6-100-14.52-10.4-4.34-27.81-14.24-50-14.52-20.93-.26-42.18,11.47-50,14.52-21.85,8.55-48.14,18-100,14.52v24.19c-5.42,1.24-14.53,8.38-20,14.52-7,7.9-3.49,10.32-10,19.35-5.71,7.93-19.05,14.1-20,14.52,2.83,12.57,4.87,30,5,48.38a208.5,208.5,0,0,1-5,48.38c8.77,3.41,15.51,8.2,20,14.52s5.86,12,10,19.35c2.83,5.07,7.34,9.15,20,14.52V571c48.38-6.12,79.68,6,100,14.52,10.4,4.34,27.81,14.24,50,14.52,20.93.26,42.18-11.46,50-14.52,21.85-8.54,48.14-18,100-14.52V546.77c5.42-1.24,14.53-8.37,20-14.52,7-7.89,3.49-10.32,10-19.35,3.19-4.42,9-10.5,20-14.52-3.48-11.89-5.06-28.17-5-48.38C695.06,430.25,696.57,413.35,700,401.62Z" transform="translate(-298.84 -299)"/><path class="cls-2" d="M685,406.45c-6.09-1.28-13.38-6-18.5-13.06-4.22-5.78-5.42-10.77-9.25-17.42-2.62-4.55-6.79-8.22-18.5-13.06V341.13c-44.75,5.52-73.7-5.43-92.5-13.06-9.62-3.9-25.72-12.81-46.25-13.07-19.36-.23-39,10.32-46.25,13.07-20.21,7.69-44.53,16.17-92.5,13.06v21.78c-5,1.11-13.44,7.54-18.5,13.06-6.51,7.12-3.23,9.29-9.25,17.42-5.28,7.13-17.62,12.69-18.5,13.06,2.62,11.32,4.51,27,4.62,43.55A182.83,182.83,0,0,1,315,493.55c8.11,3.06,14.35,7.37,18.5,13.06s5.42,10.77,9.25,17.42c2.62,4.55,6.79,8.23,18.5,13.06v21.78c44.75-5.52,73.7,5.43,92.5,13.06,9.62,3.9,25.72,12.81,46.25,13.07,19.36.23,39-10.32,46.25-13.07,20.21-7.68,44.53-16.16,92.5-13.06V537.09c5-1.11,13.44-7.53,18.5-13.06,6.51-7.11,3.23-9.29,9.25-17.42,3-4,8.33-9.45,18.5-13.06-3.21-10.71-4.68-25.36-4.62-43.55C680.43,432.22,681.83,417,685,406.45Z" transform="translate(-298.84 -299)"/><text class="cls-3" transform="translate(110.33 138.59)">Elmao<tspan x="-65.88" y="74">Industries</tspan></text><path class="cls-4" d="M445.73,541.26c1.24.13-.56,9,4.22,12a7.29,7.29,0,0,0,6.07.66c6.65-2.36,3.53-14.1,12.39-25.18a25,25,0,0,1,10.55-8c1.17-.43,7.75-2.71,14.51.13,2,.86,5.47,2.3,6.33,5.54a7,7,0,0,1-1.19,5.8c-2.95,3.87-8,1-14.11,3.7-3.62,1.6-2.85,3-12.4,14.24-6,7-8.33,8.85-11.2,10.15-2.16,1-6.16,2.72-10.69,1.32a11.51,11.51,0,0,1-6.06-4.22C439.68,551,444.41,541.13,445.73,541.26Z" transform="translate(-298.84 -299)"/><path class="cls-4" d="M554.27,541.26c-1.24.13.56,9-4.22,12a7.29,7.29,0,0,1-6.07.66c-6.65-2.36-3.53-14.1-12.39-25.18a25,25,0,0,0-10.55-8c-1.17-.43-7.75-2.71-14.51.13-2,.86-5.47,2.3-6.33,5.54a7,7,0,0,0,1.19,5.8c2.95,3.87,8,1,14.11,3.7,3.62,1.6,2.85,3,12.4,14.24,6,7,8.33,8.85,11.2,10.15,2.16,1,6.16,2.72,10.69,1.32a11.51,11.51,0,0,0,6.06-4.22C560.32,551,555.59,541.13,554.27,541.26Z" transform="translate(-298.84 -299)"/><path class="cls-4" d="M436.67,361.89a45.63,45.63,0,0,1-2.39-3.91,29,29,0,0,1-1.73-4c-.09-.27,0,0-.73-2.55-.4-1.37-.68-2.27-.29-3.27a2.46,2.46,0,0,1,.21-.43c12.06,1.67,22.53,2.7,30.88,3.38,8.7.69,20.62,1.63,36.39,1.65,5.7,0,14.17-.1,24.36-.69,8.32-.47,14.73-1.09,21.76-1.77,0,0,4.51-.43,23.44-2.5a14.79,14.79,0,0,1,.07,2.1,6.46,6.46,0,0,1-.57,2.15c-.81,2.07-1.22,3.11-1.8,4.27a40.72,40.72,0,0,1-4.85,7.44,3.77,3.77,0,0,1-1.61,1.14,5.12,5.12,0,0,1-1.38.25,3.74,3.74,0,0,1-1.16,0,3.06,3.06,0,0,1-1.51-.92s-1.16-1.09-2.23-2a9.81,9.81,0,0,0-3.24-1.79,9.14,9.14,0,0,0-2.81-.43,8.56,8.56,0,0,0-3.66,1,8,8,0,0,0-2.57,1.79,10.28,10.28,0,0,1-1.41,1.44,4.05,4.05,0,0,1-1.41.78,3.93,3.93,0,0,1-1.31.14,4.36,4.36,0,0,1-1.56-.28c-.53-.22-.64-.43-1.63-1.35-.85-.77-1.5-1.28-1.78-1.5a8.5,8.5,0,0,0-1.71-1.14,7.87,7.87,0,0,0-1.86-.51,9.84,9.84,0,0,0-2.24-.29,8.45,8.45,0,0,0-2.28.34,8.67,8.67,0,0,0-2.15,1,12.42,12.42,0,0,0-1.51,1.14c-.9.78-1,1-1.8,1.63a4.32,4.32,0,0,1-1.39.75,4.56,4.56,0,0,1-3-.19,7.6,7.6,0,0,1-1.49-1.15l-1.23-1.11a11,11,0,0,0-1.08-.94,6.53,6.53,0,0,0-1.35-.66,10.86,10.86,0,0,0-1.88-.62,8.14,8.14,0,0,0-1.92-.21,8.62,8.62,0,0,0-2.07.28,9.19,9.19,0,0,0-2,.79,10.64,10.64,0,0,0-1.89,1.36c-.7.6-.63.65-1.38,1.27A5.44,5.44,0,0,1,496,365a4.65,4.65,0,0,1-3.16-.24c-.58-.29-.53-.48-1.56-1.44a16.29,16.29,0,0,0-1.61-1.32,9.55,9.55,0,0,0-1.76-1.1,9,9,0,0,0-2-.6,9.33,9.33,0,0,0-1.83-.21,8.19,8.19,0,0,0-3.36.78,9.59,9.59,0,0,0-2.35,1.42c-.8.66-.88,1-1.91,1.79a4.61,4.61,0,0,1-1.73,1,3.89,3.89,0,0,1-2.1-.1,5.62,5.62,0,0,1-2.07-1.2c-.92-.73-.84-.94-1.74-1.65a9.92,9.92,0,0,0-1.93-1.16,9.47,9.47,0,0,0-5.33-.78,8.61,8.61,0,0,0-2.6.83,10,10,0,0,0-2.13,1.55,15.69,15.69,0,0,1-2.12,1.84,4.55,4.55,0,0,1-1.29.64,3.66,3.66,0,0,1-1.79.1,4.39,4.39,0,0,1-1.92-1.07c-.56-.45-.52-.55-1.26-1.25a10.44,10.44,0,0,0-1.78-1.44,8.63,8.63,0,0,0-2.37-1,9.43,9.43,0,0,0-2.37-.28,8.75,8.75,0,0,0-2.27.25,7.15,7.15,0,0,0-2.14.87Z" transform="translate(-298.84 -299)"/><path class="cls-4" d="M439.85,365.78a4,4,0,0,1,2.15-.54,4.11,4.11,0,0,1,1.93.61,15.62,15.62,0,0,1,1.48,1.25l.89.77a13.07,13.07,0,0,0,1.72,1.32,7.41,7.41,0,0,0,2.12.85,9.82,9.82,0,0,0,2.39.29,9.33,9.33,0,0,0,2-.2,7.24,7.24,0,0,0,2.25-.79,8,8,0,0,0,1.43-1.06c.1-.08.13-.11,1.38-1.26a8.59,8.59,0,0,1,1.18-1,3.58,3.58,0,0,1,.88-.5,3.73,3.73,0,0,1,1.42-.22,3.94,3.94,0,0,1,1.19.12,4,4,0,0,1,1.51.86c.31.26.25.26.86.85s1,.89,1.18,1.05a9.43,9.43,0,0,0,1.28.95,8.82,8.82,0,0,0,1.12.55,7.55,7.55,0,0,0,1.32.48,7.87,7.87,0,0,0,1.32.2,8.79,8.79,0,0,0,1.79,0,9.26,9.26,0,0,0,1.91-.44,10.34,10.34,0,0,0,1.41-.62,9.91,9.91,0,0,0,1.21-.75,9,9,0,0,0,.94-.83c.62-.57.66-.66,1.15-1.1a5.83,5.83,0,0,1,1-.79,3.38,3.38,0,0,1,.92-.4,3.75,3.75,0,0,1,1.05-.12,3.9,3.9,0,0,1,1.17.17,4,4,0,0,1,1.1.53,7.09,7.09,0,0,1,1.08.95c.47.45.84.81,1.31,1.19a12,12,0,0,0,1.43,1,8.76,8.76,0,0,0,1.54.77,10,10,0,0,0,4.44.37,10.82,10.82,0,0,0,3.18-1.21A10.29,10.29,0,0,0,501,368c.75-.65,1.33-1.21,1.33-1.21a6,6,0,0,1,1-.8,5.53,5.53,0,0,1,.55-.33,4,4,0,0,1,2.9-.14,5.42,5.42,0,0,1,1.82,1.22c.64.53.61.64,1.33,1.26a10.12,10.12,0,0,0,1.71,1.26,9,9,0,0,0,2.1.85,9.8,9.8,0,0,0,2.54.27,8.07,8.07,0,0,0,4-1.05,11,11,0,0,0,2-1.53c.92-.8,1.31-1.17,1.31-1.17a4.36,4.36,0,0,1,1-.84,3.73,3.73,0,0,1,1.11-.38,4.09,4.09,0,0,1,1.87,0,4.39,4.39,0,0,1,1.73,1c.27.22.16.15,1.14,1.06.83.76,1.09,1,1.32,1.15a7.2,7.2,0,0,0,1,.7,7.47,7.47,0,0,0,1.45.6,10.81,10.81,0,0,0,1.72.36,10.6,10.6,0,0,0,2.21.05,7.15,7.15,0,0,0,1.74-.33,7.3,7.3,0,0,0,1.46-.66,10.73,10.73,0,0,0,1.46-1,15.85,15.85,0,0,0,1.21-1.07c.48-.47.47-.52.83-.83a5.05,5.05,0,0,1,1.2-.81,2.92,2.92,0,0,1,1-.3,3.34,3.34,0,0,1,.67,0,5.86,5.86,0,0,1,1.24.13,3.77,3.77,0,0,1,1.19.7,13.06,13.06,0,0,1,1,.88c.73.68.7.74,1.25,1.23a7.57,7.57,0,0,0,1.24.94,4.82,4.82,0,0,0,.91.45c.34.13.42.12.45.18.12.34-2.12,1.46-4.14,2.24a24.17,24.17,0,0,1-2.79.91c-1,.25-1.53.31-3.32.61s-2.71.48-3.34.59c-9.26,1.6-20.34,2.46-20.34,2.46a290.71,290.71,0,0,1-41.66.1c-5.26-.4-1.13-.25-16.81-2,0,0-10.4-1.18-16.81-4.15a14.93,14.93,0,0,1-5.05-3.63A13.31,13.31,0,0,1,439.85,365.78Z" transform="translate(-298.84 -299)"/><path class="cls-4" d="M479,345.24a108.38,108.38,0,0,0,21,2.07,109.62,109.62,0,0,0,21.22-2,36.59,36.59,0,0,0-6.43-18.21c-4.75-6.7-9.95-8.87-11.63-9.05-1.3-.13-2.71-.15-2.71-.15s-1.58,0-2.88.11c-2,.18-5.5,1.85-9.18,5.7a32.17,32.17,0,0,0-6.49,10.18A38.57,38.57,0,0,0,479,345.24Z" transform="translate(-298.84 -299)"/></g><g id="Calque_3" data-name="Calque 3"><path class="cls-5" d="M378.34,376.63c-2.51-.75-4.83.8-7.19,2.37-2,1.35-3.76,2.51-4.48,4.68a13.69,13.69,0,0,0-.26,4.09,42.53,42.53,0,0,0,.33,5.08,67.9,67.9,0,0,0,1.31,7.18,66.25,66.25,0,0,0,2,7.39,50.72,50.72,0,0,0,4.82,9.76,81.34,81.34,0,0,0,5.6,8.24,69.86,69.86,0,0,0,7,7.91,54.29,54.29,0,0,0,7,5.87c1.28.89.49.25,8.17,4.68a18.68,18.68,0,0,0,6.14,2.64,17.46,17.46,0,0,0,4.41-.14l-3.95-3a78.09,78.09,0,0,1-6.73-5.45,34.79,34.79,0,0,1-3-3.51,41.34,41.34,0,0,1-2.42-3.66c-.75-1.23-1-1.78-1.93-3.41-2.23-4-2.21-3.5-3.29-5.71-.89-1.84-2.11-3.52-2.87-5.41a4,4,0,0,0-2.74-2.77,6,6,0,0,0-1.86-.2c-1.43,0-2.15-.06-2.32-.32-.33-.52.41-1.79,1.38-2.57,1.52-1.23,3-.83,3.22-1.56s-1.53-2.08-2.3-2.52-2.48-1.43-4.18-.87c-.82.27-1.33.81-2,.57a1.18,1.18,0,0,1-.82-.87c0-.38.24-.92,2.82-2.35s3.4-1.47,3.78-2.34a3.16,3.16,0,0,0-.62-3.14,3.33,3.33,0,0,0-1.33-.89c-1.5-.63-2.42-.08-3-.7s-.16-1.52-.12-1.65c.39-1.25,1.54-1.24,2.3-2.57a5.1,5.1,0,0,0,.49-2,14.17,14.17,0,0,0-.1-3.88c-.53-4.58.5-5.47-.62-7.07A5.06,5.06,0,0,0,378.34,376.63Z" transform="translate(-298.84 -299)"/><path class="cls-6" d="M374.43,380.37c.05-.4.67-.6,1.09-.74a3.17,3.17,0,0,1,1.73-.2,3.49,3.49,0,0,1,2.08,2c.28.5.26.62.93,3.31.43,1.77.7,2.74.27,3a.51.51,0,0,1-.3.09c-1.33-.08-1.86-6.79-3.43-7a4.16,4.16,0,0,0-1,0c-.51.07-.76.23-1,.08A.61.61,0,0,1,374.43,380.37Z" transform="translate(-298.84 -299)"/><path class="cls-6" d="M378.51,400.76c-.34-.44.05-1.38.56-1.88,1-1,3-.8,3.26-.2.14.35-.28,1-.79,1.19s-.65-.12-1.16,0c-.77.23-.89,1.12-1.45,1.09A.59.59,0,0,1,378.51,400.76Z" transform="translate(-298.84 -299)"/><path class="cls-6" d="M380.75,410.19c.45.14.77-.81,1.84-1.42s2.2-.31,2.28-.66-1-1.16-2.11-1.15a2.6,2.6,0,0,0-1.81.79,2,2,0,0,0-.63,1.55C380.33,409.41,380.4,410.08,380.75,410.19Z" transform="translate(-298.84 -299)"/><path class="cls-6" d="M383.52,414.84a2.58,2.58,0,0,1,1.94-.07,7.38,7.38,0,0,1,3.83,2.7c1.44,2.14.29,2.95,1.84,5.48.22.35,1,1.63,2,3,.64.95.81,1.17.76,1.22s-2.95-1.68-4.75-4.75a41.24,41.24,0,0,0-2.34-4c-.74-1.07-1.22-1.61-2-1.88-1.14-.41-2.1.08-2.31-.33S382.86,415.17,383.52,414.84Z" transform="translate(-298.84 -299)"/><path d="M368.91,384.6c.33,0,.52,3.1,1.45,8.18a93.64,93.64,0,0,0,3.1,12.53,78.48,78.48,0,0,0,5,11.47c3.06,6.08,4.84,9.61,8.37,13.65a51,51,0,0,0,9.23,8.11,64.45,64.45,0,0,0,9.5,5.67,53.36,53.36,0,0,1-19-12.07c-7.12-7.06-10.09-14.16-14.06-23.65a46.59,46.59,0,0,1-4-15.84C368.22,388.77,368.53,384.62,368.91,384.6Z" transform="translate(-298.84 -299)"/><path class="cls-7" d="M355.59,382.23c-.18.3.72,1.44,2,1.91a3.52,3.52,0,0,0,2.18.13c1.28-.36,1.22-1.2,2.77-2.24s2.27-.58,3.16-1.65c.61-.72.44-1.13,1.19-1.78a2.78,2.78,0,0,1,2.17-.79c.65.15.83.64,1.19.53s.67-.92.46-1.52c-.05-.15-.23-.58-1.18-1a6,6,0,0,0-3.63-.27,6,6,0,0,0-3,1.45c-.14.13-.62.79-1.59,2.11-.57.79-.86,1.19-1.05,1.52-.42.73-.42,1-.79,1.32a2.55,2.55,0,0,1-1.58.39C356.4,382.43,355.73,382,355.59,382.23Z" transform="translate(-298.84 -299)"/><path class="cls-7" d="M356.12,372c.29.22,1.23-1.5,2.77-1.45,1.08,0,1.19.9,2.57,1.06a4.36,4.36,0,0,0,2.6-.54,6.19,6.19,0,0,1,1.42-.85,1.8,1.8,0,0,1,1.26-.13c.67.26.91,1.15,1,1.45.2.77-.07,1,.19,1.45s.75.44,1.38.88c1.15.78,1.06,2,1.46,2,.6,0,1.62-2.8.59-4.75a7.31,7.31,0,0,0-1.32-1.65,4.95,4.95,0,0,0-3.1-1.78,3.82,3.82,0,0,0-2.57.2c-.69.38-.64.8-1.21.91s-.74-.24-1.69-.39a5.3,5.3,0,0,0-1.45,0,5.39,5.39,0,0,0-2.11.66C356.46,369.94,355.84,371.8,356.12,372Z" transform="translate(-298.84 -299)"/><path class="cls-7" d="M366.08,355.66c.14,1.54,1.88,1.52,2.83,3.43.53,1.06,0,1.12.6,4.61a16.8,16.8,0,0,0,.65,2.84c.42,1.22,1.27,3.13,1.72,3,.25-.05.32-.7.33-2.24,0-4.24-.57-4.94-.53-7.71,0-2.34.47-3.29-.2-4.95a3,3,0,0,0-1.58-1.91,2.84,2.84,0,0,0-2.83.66A2.91,2.91,0,0,0,366.08,355.66Z" transform="translate(-298.84 -299)"/><path class="cls-7" d="M382.43,366.21c-.74.74-.46,1.37-1.12,2a3.48,3.48,0,0,1-2.24.79c-1.51.19-1.81-.3-3.17,0a6.39,6.39,0,0,0-1.65.66,3.48,3.48,0,0,0-1.51,1.32,6.4,6.4,0,0,0-.27,2.05,3.6,3.6,0,0,0,.13,1.51c.12.34.25.69.53.79.59.23,1.43-.74,1.58-.92a7.69,7.69,0,0,0,1-1.85,4.68,4.68,0,0,1,1.72-2.11c.79-.4,1.18,0,3.36.07,1.67.05,2.52.06,3-.46s.08-.78.33-2.64c.17-1.25.38-1.7.13-1.91S383,365.65,382.43,366.21Z" transform="translate(-298.84 -299)"/><path class="cls-5" d="M621.64,378c2.52-.74,4.83.8,7.19,2.38,2,1.34,3.76,2.5,4.49,4.68a13.61,13.61,0,0,1,.26,4.08,47.08,47.08,0,0,1-.33,5.08,65.86,65.86,0,0,1-1.32,7.19,61.94,61.94,0,0,1-2,7.38,51.29,51.29,0,0,1-4.81,9.76,79.67,79.67,0,0,1-5.61,8.24,69.44,69.44,0,0,1-7,7.92,54.37,54.37,0,0,1-7,5.86c-1.29.9-.49.26-8.18,4.68a18.42,18.42,0,0,1-6.13,2.64,17.69,17.69,0,0,1-4.42-.13l4-3a77.63,77.63,0,0,0,6.72-5.45,34.63,34.63,0,0,0,3-3.51,42.41,42.41,0,0,0,2.43-3.66c.75-1.24,1-1.78,1.93-3.41,2.22-4,2.21-3.51,3.28-5.71.9-1.84,2.12-3.52,2.87-5.42a4.73,4.73,0,0,1,1.83-2.37,5,5,0,0,1,.92-.4,6.3,6.3,0,0,1,1.85-.2c1.44,0,2.16-.05,2.33-.32.33-.52-.42-1.78-1.39-2.57-1.51-1.22-3-.82-3.21-1.56s1.52-2.07,2.3-2.52,2.47-1.42,4.18-.86c.82.27,1.32.8,2,.57a1.2,1.2,0,0,0,.83-.87c0-.38-.25-.92-2.82-2.35s-3.4-1.47-3.78-2.35a3.17,3.17,0,0,1,.62-3.14,3.45,3.45,0,0,1,1.33-.89c1.49-.63,2.42-.08,2.94-.69a2,2,0,0,0,.13-1.66c-.4-1.24-1.55-1.23-2.3-2.57a4.83,4.83,0,0,1-.5-2,14.6,14.6,0,0,1,.1-3.88c.54-4.57-.49-5.46.63-7.06A5,5,0,0,1,621.64,378Z" transform="translate(-298.84 -299)"/><path class="cls-6" d="M625.55,381.74c0-.39-.66-.6-1.09-.74a3.14,3.14,0,0,0-1.73-.2,3.52,3.52,0,0,0-2.07,2c-.29.5-.27.62-.93,3.32-.44,1.76-.7,2.74-.27,3a.49.49,0,0,0,.29.08c1.34-.07,1.87-6.78,3.44-7a4,4,0,0,1,1,0c.51.07.76.24,1,.09A.62.62,0,0,0,625.55,381.74Z" transform="translate(-298.84 -299)"/><path class="cls-6" d="M621.48,402.13c.33-.43-.05-1.37-.56-1.88-1-1-3-.79-3.26-.19-.15.35.28,1,.79,1.18s.65-.11,1.15,0c.77.23.89,1.12,1.45,1.08A.59.59,0,0,0,621.48,402.13Z" transform="translate(-298.84 -299)"/><path class="cls-6" d="M619.24,411.56c-.45.14-.77-.81-1.85-1.42s-2.19-.3-2.27-.65,1-1.16,2.11-1.16a2.62,2.62,0,0,1,1.81.79,2,2,0,0,1,.63,1.55C619.66,410.79,619.59,411.45,619.24,411.56Z" transform="translate(-298.84 -299)"/><path class="cls-6" d="M616.47,416.21a2.6,2.6,0,0,0-2-.07,7.37,7.37,0,0,0-3.82,2.71c-1.45,2.13-.29,2.95-1.85,5.47-.22.36-1,1.63-2,3-.64.95-.81,1.18-.76,1.22s3-1.67,4.74-4.74a40.6,40.6,0,0,1,2.35-4c.74-1.07,1.22-1.61,2-1.88,1.14-.41,2.11.07,2.31-.33S617.12,416.54,616.47,416.21Z" transform="translate(-298.84 -299)"/><path d="M631.07,386c-.33,0-.52,3.1-1.45,8.18a92,92,0,0,1-3.1,12.52,78.21,78.21,0,0,1-4.94,11.48c-3.06,6.08-4.84,9.61-8.37,13.64a50.94,50.94,0,0,1-9.24,8.11,64.06,64.06,0,0,1-9.49,5.67,53.33,53.33,0,0,0,19-12.06c7.11-7.07,10.08-14.16,14-23.65a46.48,46.48,0,0,0,4-15.85C631.76,390.14,631.45,386,631.07,386Z" transform="translate(-298.84 -299)"/><path class="cls-7" d="M644.39,383.61c.18.29-.72,1.43-2,1.91a3.48,3.48,0,0,1-2.17.13c-1.29-.36-1.23-1.21-2.77-2.24s-2.27-.59-3.17-1.65c-.61-.73-.43-1.13-1.18-1.78a2.77,2.77,0,0,0-2.18-.79c-.64.15-.82.64-1.19.53s-.66-.92-.46-1.52c.06-.15.24-.58,1.19-1a6.1,6.1,0,0,1,3.63-.26,5.89,5.89,0,0,1,3,1.45c.13.13.62.79,1.58,2.11.58.79.87,1.19,1.06,1.51.42.74.41,1,.79,1.32a2.54,2.54,0,0,0,1.58.4C643.59,383.8,644.25,383.38,644.39,383.61Z" transform="translate(-298.84 -299)"/><path class="cls-7" d="M643.86,373.39c-.28.22-1.22-1.5-2.76-1.45-1.09,0-1.19.9-2.58,1.05a4.32,4.32,0,0,1-2.59-.53,5.81,5.81,0,0,0-1.43-.85,1.77,1.77,0,0,0-1.25-.14c-.68.27-.91,1.15-1,1.45-.2.77.06,1-.2,1.46s-.75.44-1.38.88c-1.14.78-1.06,2-1.45,1.95-.61,0-1.62-2.79-.6-4.75a7.86,7.86,0,0,1,1.32-1.64,6,6,0,0,1,1.52-1.26,5.34,5.34,0,0,1,1.58-.53,4,4,0,0,1,2.57.2c.7.39.65.8,1.22.91s.74-.23,1.68-.38a4.92,4.92,0,0,1,1.45,0,5.18,5.18,0,0,1,2.11.66C643.53,371.31,644.14,373.17,643.86,373.39Z" transform="translate(-298.84 -299)"/><path class="cls-7" d="M633.91,357c-.14,1.55-1.89,1.52-2.84,3.43-.52,1.07,0,1.13-.59,4.62a16.48,16.48,0,0,1-.66,2.83c-.42,1.23-1.26,3.14-1.71,3-.25-.06-.33-.7-.33-2.24,0-4.24.57-4.94.52-7.72,0-2.33-.46-3.28.2-4.94a3.11,3.11,0,0,1,1.58-1.92,2.87,2.87,0,0,1,2.84.66A3,3,0,0,1,633.91,357Z" transform="translate(-298.84 -299)"/><path class="cls-7" d="M617.56,367.58c.74.75.45,1.37,1.12,2.05a3.46,3.46,0,0,0,2.24.79c1.5.18,1.81-.3,3.16,0a5.89,5.89,0,0,1,1.65.66,3.51,3.51,0,0,1,1.52,1.32,6.49,6.49,0,0,1,.26,2,3.49,3.49,0,0,1-.13,1.52c-.12.34-.24.68-.53.79-.59.22-1.42-.74-1.58-.92a8.06,8.06,0,0,1-1-1.85,4.61,4.61,0,0,0-1.71-2.11c-.79-.4-1.19,0-3.36.07-1.68.05-2.53.06-3-.47s-.08-.78-.33-2.63c-.17-1.26-.39-1.71-.13-1.92S617,367,617.56,367.58Z" transform="translate(-298.84 -299)"/></g></svg>
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
                                                <img src="https://project.maxprudhomme.com/launchPlatform/whyDidUSavedThisPicture.jpg"
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
                                            &reg; Elmao Industries, 69 Cartman Street,<br>South Park 2022
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