# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser
    class here. You should generate an instance of
    your FastaParser class and assert that it properly
    reads in the example Fasta File.
    """
    fasta_parser = FastaParser("./data/test.fa")
    records = [rec for rec in fasta_parser]

    # check first 2 records
    assert records[0] == (">seq0", "TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCC"
                                   "TCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA")
    assert records[1] == (">seq1", "TCCGCCCGCTGTGCTGACGAGACTAGCAGGGAAATAAATAGAGGGTTTAG"
                                   "TTATACTCAGTAGGCAGTTCGATGGCTTATATCTAACTTCTTATTCCGAT")

    # check last 2 records
    assert records[-2] == (">seq98", "CGAGCGAGAAACGCGCTAACTAGCAACCGGAACAACAATGCTGGGTTGAA"
                                     "TTTGATTCGCACCCGACGATCACTAGAGAGTTTATCTGGGACTCCGGGAC")
    assert records[-1] == (">seq99", "CAAACCGGCGATGCGGGTACTCCCTACAAGTTGGACTCCGCAGCGAACGC"
                                     "CGCAGGGGCCATTATACGGCGGTCTTGGCGGCGTCGACCAGGCCGGTCCA")


def test_FastqParser():
    """
    Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    """
    fastq_parser = FastqParser("./data/test.fq")
    records = [rec for rec in fastq_parser]

    # check first 2 records
    assert records[0] == ("@seq0",
                          "TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGC"
                          "GTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG",
                          "*540($=*,=.062565,2>\'487\')!:&&6=,6,*7>:&132&83*8"
                          "(58&59>\'8!;28<94,0*;*.94**:9+7\"94(>7=\'(!5\"2/!%\"4#32=")
    assert records[1] == ("@seq1",
                          "CCCCGGACGACTGATCCCGATAGAGCTCACTCTTCGAGGCAAGCAGACCC"
                          "ATATCGTCCTGCTGGCAACGCTATCCGGGTGCGAGTAAATCGAAACCTCG",
                          "\'(<#/0$5&!$+,:=%7=50--1;\'(-7;0>=$(05*9,,:%0!<),%"
                          "646<8#%\".\"-\'*-0:.+*&$5!\'8)(%3*+9/&/%=363*,6$20($97,\"")

    # check last 2 records
    assert records[-2] == ("@seq98",
                           "AACCTGCCCGTAGCCTTTAGGTAGCCCGTCTACATGTCCTCCAGTACAGT"
                           "GGAAGCTCCTACATCAACTGATCAAATAACATCGCAGCACTATATGTCAC",
                           "39$$8\'\':7:0;0%/7$89-<3\',:)1\"0\'=2\'!#5><>+6/=9"
                           "9#>8-$76(6$2\'+=;$-))753#99,=+4+1=:5.08*$*:4=,>)/)\':8,<48")
    assert records[-1] == ("@seq99",
                           "CCGAGTTTTGTAGTGGGCTCAACTGAAATCCTATTCTTAGACGATTGGTC"
                           "ATAAAACCCTTTCACTGTACGGACGTAGACCCTGCTCCGTCTTCCAGCAG",
                           "2$7)*5:\"=+++!:.=>!5>79)8!566$!3*/4$=4.%=//;900$9)"
                           "!%)4%$=0\":02\"0=!0#/>+*1$1$39!.8+9<\'1$*1$321&<\'&9,)2")


