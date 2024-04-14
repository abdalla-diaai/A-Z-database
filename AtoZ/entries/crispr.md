# CRISPR-RNP nucleofection in glioblastoma cells protocol

## Background

The goal of this protocol is to produce bi- or multi-allelic loss of gene function in cell populations via insertion-deletion (indel) or near-precise deletion mutations triggered by CRISPR-Cas9 targeting. This protocol represents our current preferred method, which utilizes in vitro-formed Cas9:sgRNA ribonucleoprotein (RNP) complexes composed of one to three chemically synthesized 2'-O-methyl 3’phosphorothioate-modified sgRNAs and purified Cas9 protein. We currently purchase our sgRNAs from Synthego (<https://www.synthego.com/>).

These sgRNAs are a single RNA molecule that contains both the custom-designed short crRNA sequence fused to the scaffold tracrRNA sequence. Synthego’s 2'-O-methyl 3’phosphorothioate-modifications occur in the first and last 3 nucleotides. Other companies also provide sgRNA synthesis services, including IDT, Horizon Discovery, Thermo Fisher Scientific, and Sigma-Aldrich. In addition, sgRNAs can be synthesized in vitro, e.g. using in vitro transcription reactions and short DNA templates (although this usually results in inferior editing efficiency).

The Amaxa Nucleofector System uses proprietary electrical parameters and buffer formulations. This protocol is optimized for glioblastoma stem-like cells (GSCs) and human neural stem cells (NSCs) (with nucleofection program based on conditions described for mouse NSCs in Bressan et al. 2017). However, this protocol can be successfully employed CRISPR in other cell types as well using this method. Nucleofection conditions (i.e. nucleofection buffer and program) should be optimized for other cell types. Lonza can provide guidance for many cell lines/types (<https://knowledge.lonza.com/>).

## Designing sgRNAs

a. There are many sgRNA design resources available. The Broad Institute’s GPP Web Portal (Doench et al. 2016, <https://portals.broadinstitute.org/gpp/public/analysis-tools/sgrna-design>) in combination with Synthego’s design tool (<https://design.synthego.com/#/>) can be used to identify potential top sgRNAs for a particular gene. These lists from both tools can be curated manually by evaluating ontarget score versus predicted off-target effects in order to identify ~3-4 top sgRNAs per gene for experiments. When using nucleofection of RNPs, about 60-70% of such sgRNAs result in high editing efficiency (>80% indel efficiency). Total editing efficiency can usually also be increased by simultaneously nucleofecting with multiple sgRNAs targeting the same gene.

b. If a near-precise deletion is desired, typically two sgRNAs spaced ~50-300bp apart are designed. Up to 1000bp spacing between two gRNAs works well, although efficiencies for deletions <300bp can be more easily assessed (compared to larger deletions), via simple Sanger sequencing. When the goal is a gene KO, both sgRNAs can be designed to be in exons (or the same exon), so that even alleles that do not receive a deletion still have a good chance of resulting in gene KO via small indels.

c. By necessity, available sgRNA design tools list possible sgRNA sequences based on a reference genome for the species you are using. It is a good idea to check the genomic sequence of your particular cells for polymorphisms (and mutations in the case of cancer cell lines) that may exist and may cause some sgRNA sequences created by design tools to have mismatches in your particular cells. In other words, it is best to ensure that the exact sgRNA sequence you decide to use is actually intact in your cells’ genome.

## Reagents

- SpCas9 2NLS Nuclease, Synthego, Lot# S-M22968-01.
- SOX2 gRNA#1: cauguacaacaugauggaga, SOX2 gRNA#2: ccucucacacaugugagggc, Synthego.
- Non-targeting control: cat# 1079138, Lot# 0000561275, IDT.
- HPRT (positive control): cat# 1079132, Lot# 0000563628, IDT.
- Tracr-RNA: cat# 1073189, Lot# 000553669, IDT.
- SG Cell Line 4DX Kit, Lonza, cat# V4XC-3024, lot# F-14402.
- 4D-nucleofactor, Lonza.

## CRISPR-RNP nucleofection

**_a. Reconstitute your synthetic RNA (and dilute it if desired):_**

1. Briefly centrifuge your tubes or plates containing synthetic modified single guide RNA (sgRNA) oligos to ensure that the dried RNA pellet is collected at the bottom.
2. Carefully dissolve sgRNA in the provided nuclease-free 1X TE Buffer (Tris-EDTA, pH 8.0) by adding 15 μL buffer to 1.5 nmoL of dried sgRNA. (This will result in a final concentration of 100 μM (100 pmoL/μL)). Flick the bottom of the tube gently so the liquid covers the bottom, then pulse vortex the tube for ~30 seconds and quick spin reconstituted RNA down. Dissolved RNA should be stored at -20 °C when not in use. Under these conditions, RNA will be stable for at least one year.
3. If desired, to create a working stock, make a 30 μM sgRNA dilution (e.g. 14 μL nuclease-free water + 3 μL of each reconstituted 100μM sgRNA, creating a total of 20 μL of 30 μM (30pmoL/μL) sgRNA). Use diluted sgRNA immediately or store at -20 °C for up to three months. Keep RNA on ice while in use. (If you will make larger master mixes of RNPs using the same sgRNA(s), it may not be necessary to dilute your sgRNA. sgRNAs are diluted primarily to allow for easier pipetting volumes.)

**_b. Dilute Cas9:_**

1. Briefly centrifuge the stock Cas9 (Synthego sNLS-SpCas9-sNLS, 20 μM) to ensure that all liquid is at the bottom. To make a working stock, make a 1:2 Cas9:PBS dilution (e.g. 5 μL PBS (pH 7.4) + 5 μL Cas9, creating 10 μL of 10 μM (10 pmoL/μL) Cas9).
2. Keep diluted/undiluted Cas9 on ice. Only make the amount of diluted Cas9 that you will need at any given time since it is best not to freeze the diluted Cas9.

**_c. Assemble RNP complexes:_**

1. Create complete Nucleofector Solution by mixing SG Cell Line Solution (or other solution specific to your cell type) with the provided Supplement at a 4.5:1 ratio (e.g. for one nucleofection, combine 16.4 μL Cell Line Solution + 3.6 μL Supplement). Make a master mix for multiple nucleofections. (Once combined, the complete Nucleofector Solution is stable for three months.)
2. Assemble RNP complexes in complete Nucleofector solution, adding reagents in the order shown below. The amounts below will allow for 15 pmoL total RNPs to be nucleofected into one cell sample (with 10% extra volume), at an sgRNA:Cas9 ratio of 2:1. You may make a master mix for multiple nucleofections using identical RNPs.

| Reagent | Volume (μL) |
| --- | --- |
| Complete Nucleofector Solution | 19.28 |
| Synthego gRNA (30 pmol/ μL) | 1.10 |
| Cas9 (10.17 pmol/ μL) | 1.62 |
| Total | 22  |

1. Mix by pipetting and briefly centrifuge the sample so all the liquid is at the bottom.
2. Incubate RNPs for 10-20 minutes at room temperature and then keep on ice (or at 4°C) until shortly before use. Immediately before using complexed RNPs to resuspend cells (see below), make sure to re-equilibrate RNPs back to room temperature.

**_d. Collect and prepare cells:_**

1. Cells were harvested with Accutase (2 mL per T75 flask) as described in the attached cell culture protocol.
2. Cells were counted by trypan blue exclusion.
3. Cells were adjusted to 20 x 10<sup>4</sup> cells/mL in 1 mL complete media.
4. Laminin was removed from the plate and 4 mL of prewarmed media was added to each well. The plate was kept in the incubator till cell electroporation.

| Cells | Passage | Viability | Concentration | Volume required for 20 x 10<sup>4</sup> cells/mL in 1 mL (µL) |
| --- | --- | --- | --- | --- |
| E13 | 16  | 88% | 1.06 x 10<sup>6</sup> /mL | 188 |
| E35 | 17  | 89% | 1.33 x 10<sup>6</sup> /mL | 151 |

1. For each sample to be nucleofected, aliquot 2 x 10<sup>5</sup> cells into a separate 1.5 mL microcentrifuge tube and centrifuge at 300g for 5 minutes.
2. Resuspend cells in PBS to wash, and centrifuge at 300g for 7 minutes.
3. Aspirate the liquid as completely as possible. Resuspend the cell pellet in 20 μL of RNP complexes. Work quickly, but carefully, and avoid leaving cells in Nucleofector Solution for longer than 30 minutes total (from the time you resuspend them to the time nucleofection is complete). Avoid bubble formation.
4. Transfer all of the cell-RNP solution to one well of a 16-well Nucleocuvette strip, and cover with the provided strip lid. Make sure there are no bubbles in your Nucleocuvette.

**_e. Nucleofect cells:_**

1. If using the Amaxa 4D Nucleofector X unit, turn on the core unit and then use the touch screen to select the appropriate options for nucleofecting a 16-well strip.
2. Visually inspect the Nucleocuvette Vessel to make sure that the sample covers the bottom of the cuvette and that there are no bubbles in the cuvette. If you notice problems, gently tap the Nucleocuvette Vessel against your hand and/or use a thin sterile pipet tip to pop any bubbles.
3. If using a 16-well Nucleocuvette strip, insert the strip into the open Nucleofector 4D X unit. Make sure the larger gap in the strip lid is at the top of the strip rather than at the bottom, so that the yellow indicator in the X unit fits through the large gap at the top of the lid. Alternatively, if using the 96-well Shuttle Unit, place the Nucleocuvette Vessel with plate lid into the retainer of the 96-well Shuttle Unit. Check for proper orientation of the plate (A1 should be at the top left).
4. Run nucleofection program **EN-138** (or other cell-type specific program). After run completion, the screen should display a “+” over the wells that were successfully electroporated. Remove the cuvette strips/plate from the machine.
5. Carefully resuspend the cells in each well of the Nucleocuvette with 80μl of prewarmed growth media and mix very slowly and gently by pipetting up and down 3-4 times.
6. Transfer all 100μl to one well of the pre-warmed, media-containing cell culture plate
7. and gently pipet up and down a few times.
8. Shake the plate to distribute the cells. Leave the plate at room temperature for ~20-25 minutes and then place in incubator. (This helps distribute cells evenly.)

Optional: change the media 12-24 hours after nucleofection to remove dead cells and debris.

1. Three days after nucleofection, cells may be collected for indel analysis and/or phenotypic analysis, or cells may be expanded if creating a stable line. If studying an essential gene, phenotypic analysis may need to be done sooner as the majority of editing happens within 24 hours and the stability of the particular remaining protein will determine how quickly a phenotype can be observed.
2. Cells were incubated for 4 days at 37 °C, 5% CO2.
3. Cells can be analysed by ICC, western blotting or by PCR followed by Sanger sequencing (detailed in a separate protocol).

