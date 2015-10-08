__author__ = "J_Hack92"


class FileHandler:

    def __init__(self, fname, crap):

        self.fname = fname

        """
        self.crap is the data being written to the file
        """
        self.crap = crap

    def write2file(self):

        """
        open(xxxxxx, 'a' <==== the 'a' means to append; options: 'w': write; 'r': read-only;
        """

        with open(self.fname, 'a') as txtfile:
            txtfile.write(self.crap)
            txtfile.close()