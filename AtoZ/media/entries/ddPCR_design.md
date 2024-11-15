**ddPCR primer and probes design**

**ddPCR assay**

**For full guidance on assay design, see page 11 of** [**https://www.bio-rad.com/webroot/web/pdf/lsr/literature/Bulletin_6407.pdf**](https://www.bio-rad.com/webroot/web/pdf/lsr/literature/Bulletin_6407.pdf)

Hydrolysis probe has fluorescent reporter at 5’ end and quencher at 3’ end. During annealing the hydrolysis probe binds to the target sequence. When the probe is intact, the fluorescence of the reporter is quenched due to its proximity to the quencher. During extension, the probe is partially displaced and the reporter is cleaved – the free reporter fluoresces. TaqMan assays exploit the 5’ exonuclease activity of polymerases. dsDNA-specific 5’ to 3’ exonuclease activity of Taq cleaves off the reporter. As a result the reporter is separated from the quencher, resulting in a fluorescence signal that is proportional to the amount of amplified product in the sample.

**Amplicon**

- Plan to amplify 60-200bp product
- Avoid regions with secondary structure
- Choose region that has GC content of 40-60%

**Primers:**

- Equal/Similar Tm (+/ - 2˚C), Tm are normally 58-60˚C
- Aim for 15-30 bases in length
- GC 35-65%, ideally 50%, avoid runs of >4 Gs to prevent formation of G quadruplexes.
- G or C bases at the 3’ of the primer but not more than 2 in the last 5 bases.
- There should be more Cs than Gs, and not a G at the 5' end.
- Low probability of dimer or hairpin formation
- Check forward and reverse primer sequences to ensure no 3’ complementarity (avoid primer-dimers)
- Blast primers to check specificity, ncbi.nlm.nih.gov/tools/primer-blast/
- Check for secondary structure of the amplicon using Mfold program (<http://mfold.rna.albany.edu/?q=mfold>)
- Use [IDT oligo analyzer](https://eu.idtdna.com/calc/analyzer), change modifications to be dNTP 0.8, divalent cation conc 3.8 (Mg2+), 0.3uM primer conc, 50mM salt. (from Biorad ddPCR booklet).
- None/1 primer can overlap with ssDNA oligo – this lasts long in cells so don’t want to be amplifying this in PCR.

**Probe (qPCR from sigma)**

- Biorad QX100 or QX200 system. QX100 is compatible with TaqMan hydrolysis probes only
- Probe labelled with fluourescent reporter at 5’ end and a quencher at 3’ end. FAM on mutant probe, HEX on wt probe. Black Hole Quencher or other nonfluorescent quenchers are recommended.
- Probe within amplicon, can not overlap with primer sequences although can be directly next to one another.
- Tm should be 4-10˚C higher than that of the primers (only).
- Limit probe length to 30 bases. Distance between quencher and fluorophore affects baseline signal intensity.
- GC 30-80%, avoid consecutive Gs. Design the probe to anneal to the strand that has more Gs than Cs (so the probe contains more Cs than Gs)
- Avoid a G at the 5’ end as this quenches the fluorescence signal even after hydrolysis
- Absence of 4 G repeats
- Low probability of dimer or hairpin formation (hairpin Tm should be lower than the annealnig tempearture for the reaction)
- Tm enhancers for probes are recommended for SNPs and rare mutation detection assays in order to keep the background fluorescence to a minimum. Shorter probes discriminate better between single base differences in the target amplicon.
- Shorter probes for mismatch dicrimination. Can add stabilizing modifications such as locked nucleic acid (LNA) residues to raise probe Tm (IDT offer online tool to calculate Tm of modified probes).

**LNA locked nucelic acid bases**

- Modified RNA monomers. Locked – methylene bridge bond linking the 2’ oxygen to the 4’ carbon of the RNA pentose ring. The bridge bond fixes the pentose ring in the 3’-endo conformation.
- Heighted structural stability, increased hybridizatization melting temp ™. Resistance to nucleases.
- Due to increaed Tm qPCR probes can be designed with shorter lengths – more effective quenched signal and therefore have higher signal-to-noise ratio.
- Each LNA increases the Tm by 3-6 degrees. Multiple LNC (up to 6) can result in >15 degrees.
- Check secondary structure of probes
- Recommend using up to 6 affinity plus locked nucleic acid bases in qPCR probe.
- LNA should be placed at the SNP site, and on each of the adjacent bases. The SNP should be in the center of the probe. Avoid placing LNA on first or last bases of probe sequence.
- Recommend not placing more than 4 LNA bases sequentially.
- Amplicon of up to 150bp is recommended for standard qPCR. 80-100 bp recommended for ddPCR.

**LNA probe design:**

- Place a triplet of LNA modifications with the central base of the triplet at the mismatch site, unless the probe contains the guanine base of a G-T mismatch.
- LNA modification of the guanine nucleotide or either of its nearest-neighbour bases should be avoided in a G-T mismatch site.
- Shorter probes improve mismatch discrimination
- Avoid consecutive sequence of more than four LNA residues
- Better discrimination when position of the mismatch site is close to the center of the probe.
- Probes should not fold into stable, undesired self-complementary secondary structures or form self-dimers, especially when these structures contain LNA-LNA pairs.

**Ordering ddPCR primers and probes:**

Sigma/Merk can be used for the primers and probes

Primers: _Pure and Simple Primers_

_Coupa>Merk Punchout Catalogue>Products>Molecular Biology & Functional Genomics>_ _Oligos, qPCR Probes & Peptides>Custom & Predesigned DNA Oligos and qPCR Probes>_ _Pure & Simple Primers_

Guaranteed Yield: 3 OD

Ships within 24 - 48 hours

Price (Nov 2022): roughly £9 per primer

Probes: _Dual-Labeled Probes_

_Coupa>Merk Punchout Catalogue>Products>Molecular Biology & Functional Genomics>_ _Oligos, qPCR Probes & Peptides>Custom & Predesigned DNA Oligos and qPCR Probes>_ _Dual-Labeled Probes_

5’ Reporter / 3’ Quencher combiaation, choose between:

- 6-FAM / BHQ-1 (usually mutant)
- HEX / BHQ-1 (usually WT)

Yield: 1 to 3 OD is enough for most projects

Shipping: 9-14 days

Price (Nov 2022): roughly £165 per probe