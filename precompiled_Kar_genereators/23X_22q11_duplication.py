from Main.Start_Genome import generate_raw_genome

new_genome = generate_raw_genome(1, ['all'], ['ChrX'],
                                 '../Metadata/Full_Genome_Indices.txt')
event_segments = new_genome.tandem_duplication(new_genome.full_KT['Chr22'][0].q_arm, 3967960, 6043837)
new_genome.append_history('tandem_duplication', event_segments, new_genome.full_KT['Chr22'][0], new_genome.full_KT['Chr22'][0])

new_genome.mark_history('22q11_duplication')
new_genome.output_KT('../Precompiled_Kar/23X_22q11_duplication.kt.txt')
