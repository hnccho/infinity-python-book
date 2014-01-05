#!/usr/bin/python

"""
Changes password of a user account of remote system via telnet.

Yong Choi <sk8er.choi@gmail.com>
"""

import pexpect, getopt, sys, time, os

def changepw(host, user, oldpw, newpw):
    child = pexpect.spawn('telnet %s' % host)
    child.expect('ogin:')
    child.sendline(user)
    child.expect('assword:')
    child.sendline(oldpw)
    child.sendline('sh')
    child.sendline('LANG=C')
    child.sendline('passwd')
    child.expect(['Current', 'Old'])
    child.sendline(oldpw)
    child.expect('New password:')
    child.sendline(newpw)
    child.expect(['Re-enter', 'again'])
    child.sendline(newpw)
    child.sendline('exit');
    child.sendline('exit');
    child.expect(pexpect.EOF);
    print(child.before)

def usage():
    filename = os.path.basename(sys.argv[0])
    print('usage: %s [-t] host user oldpw newpw' % filename)

def test(host, user, oldpw, newpw):
    print(host)
    #print(user)
    #print(oldpw)
    #print(newpw)

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'h:t', ["help"])
    except getopt.GetoptError, err:
        print(err)
        usage()
        sys.exit(2)
    testmode = False
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o == "-t":
            testmode = True

    try:
        host, user, oldpw, newpw = tuple(args)
    except:
        usage()
        sys.exit(2)

    if testmode:
        test(host, user, oldpw, newpw)
    else:
        changepw(host, user, oldpw, newpw)

if __name__ == "__main__":
    main()
