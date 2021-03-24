#! /usr/bin/env python3

import vcf

__author__ = 'XXX'


class Assignment2:
    
    def __init__(self):
        ## Check if pyvcf is installed
        print("PyVCF version: %s" % vcf.VERSION)
        

    def get_average_variant_quality_of_file(self):
        '''
        Get the average PHRED quality of all variants
        :return:
        '''    
        print("TODO")
        
        
    def get_total_number_of_variants_of_file(self):
        '''
        Get the total number of variants
        test with grep '^chr21'  <filename>  | wc -l
        :return: total number of variants
        '''
        print("TODO")
    
    
    def get_vcf_fileformat(self):
        '''
        Return the file format of the VCF file
        :return: 
        '''
        print("TODO")


    def get_number_of_indels(self):
        '''
        Return the number of identified INDELs
        :return:
        '''
        print("TODO")
        

    def get_number_of_snvs(self):
        '''
        Return the number of SNVs
        :return: 
        '''
        print("TODO")


    def get_number_of_heterozygous_variants(self):
        '''
        Return the number of heterozygous variants
        :return: 
        '''
        print("TODO")
        
    

    



