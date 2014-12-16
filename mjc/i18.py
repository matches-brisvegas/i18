"""Script to test internationalisation"""
import sys
import gettext 


def mjc_test():
    pass


def main():
    """Main entry point for the script."""

# Set up message catalog access
    #t = gettext.translation('messages', './po', fallback=True)
    t = gettext.translation('messages', 'locale', ['en_US'])
    #_ = t.ugettext

    #gettext.bindtextdomain('messages', './po')
    #print gettext.bindtextdomain('messages')

    #gettext.textdomain('messages')
    #print gettext.textdomain()

    _ = t.gettext

    print _('test')
    print _('test-a')

    print gettext.find('messages')

    en_us = gettext.translation('messages', 'locale', languages=['en_US'])
    en_us.install()
    _ = en_us.gettext

    print _('test')
    print _('test-a')
    print en_us.gettext('test-a')
    print en_us.gettext('test-b')

    pass

if __name__ == '__main__':
    print "main"
    sys.exit(main())
