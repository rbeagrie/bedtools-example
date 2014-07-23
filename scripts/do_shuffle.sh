#! /bin/bash


for i in {1..100}
do
    bedtools shuffle -chrom -i data/cpg.bed -g data/genome.txt > shuffled_cpg/cpg.shuffled${i}.bed
done

