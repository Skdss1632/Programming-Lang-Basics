import imaplib
import email
import re
import pyperclip
import pyautogui

# Email credentials and settings
EMAIL = 'skdss1632@gmail.com.com'
PASSWORD = ''
IMAP_SERVER = 'imap.gmail.com'
IMAP_PORT = 993

# Connect to the email server
mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
mail.login(EMAIL, PASSWORD)
mail.select('inbox')

# Search for emails from a specific sender
status, messages = mail.search(None, '(FROM "ticketadmin@irctc.co.in")')

# Get the list of email IDs
email_ids = messages[0].split()

# Fetch the latest email
latest_email_id = email_ids[-1]
status, msg_data = mail.fetch(latest_email_id, '(RFC822)')

# Parse the email content
msg = email.message_from_bytes(msg_data[0][1])

# If the email is multipart, get the payload
if msg.is_multipart():
    for part in msg.walk():
        if part.get_content_type() == 'text/plain':
            email_body = part.get_payload(decode=True).decode()
else:
    email_body = msg.get_payload(decode=True).decode()

# Extract the OTP using a regular expression
otp_pattern = r'Your One Time Password \(OTP\) for eWallet booking on IRCTC is (\d+).'
match = re.search(otp_pattern, email_body)

if match:
    otp = match.group(1)
    print(f'OTP: {otp}')

    # Copy OTP to clipboard using pyperclip
    pyperclip.copy(otp)
    print("OTP copied to clipboard.")

    # Optionally, use pyautogui to paste the OTP somewhere
    # For example, move to a specific location and paste the OTP
    pyautogui.click(x=100, y=200)  # Change x and y to the location where you want to paste the OTP
    pyautogui.hotkey('ctrl', 'v')  # On Windows/Linux
    # pyautogui.hotkey('command', 'v')  # On macOS
else:
    print('OTP not found')

# Logout and close the connection
mail.logout()
