class MyTxtParser(object):
    def __new__(cls):
        from robot.parsing.txtreader import TxtReader
        print 'Creating user defined parser "MyTxtParser"'
        return TxtReader()

    