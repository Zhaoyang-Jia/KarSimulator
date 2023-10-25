import sys
sys.path.insert(1, '/media/zhaoyang-new/workspace/KarSim/KarSimulator/Main')
from Main.Start_Genome import generate_raw_genome


new_genome = generate_raw_genome(1, ['all'], ['ChrY'],
                                 '../Metadata/Full_Genome_Indices.txt')
event_segments = new_genome.deletion(new_genome.full_KT['Chr17'][0].q_arm, 3894098, 5050321)
new_genome.append_history('deletion', event_segments, new_genome.full_KT['Chr17'][0], new_genome.full_KT['Chr17'][0])

new_genome.mark_history('NF1')
new_genome.output_KT('../Precompiled_Kar/23Y_NF1_microdeletion.kt.txt')
