import re

def parse_log(log_line):
    pattern = r"\[from:(.+?)\] \[to:(.+?)\] \[flags:(.+?)\]"
    match = re.search(pattern, log_line)
    if match:
        sender, receiver, flags = match.groups()
        return f"{sender},{receiver},{flags}"
    else:
        return "No match found"

# Test the function with one of your log lines
log_line = 'Feb 1 11:00:00 ip-10-0-0-11 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE1] [SVC:] [ACT:] [BINF:] [FID:] [from:Google] [to:+16474951758] [flags:-1:0:-1:0:-1] [msg:127:This planet has - or rather had - a problem, which was this: most of the people on it were unhappy for pretty much of the time.] [udh:0:]'
print(parse_log(log_line))
