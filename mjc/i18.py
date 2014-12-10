"""Script to test internationisation"""
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

    print gettext.find('messages')

    langEN_US = gettext.translation('messages', 'locale', languages=['en_US'])
    langEN_US.install()
    _ = langEN_US.gettext

    print _('test')
    print langEN_US.gettext('test-a')

    pass

if __name__ == '__main__':
    print "main"
    sys.exit(main())

