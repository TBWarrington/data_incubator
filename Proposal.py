import pandas as pd
import numpy
import matplotlib.pyplot as plt

data = pd.read_csv('GSE112356_RNA_counts.txt', sep='\t')

print(data['H1H'])



plt.plot(
	data['H1H'], "Red", label='Heart 1')
plt.plot(
	data['H2H'], "green", label='Heart 2')
plt.plot(
	data['H3H'], "blue", label='Heart 3')
plt.plot(
	data['H4H'], "black", label='Heart 4')
plt.title('Heart Methylation Variation')
plt.xlabel('Gene')
plt.ylabel('Methylation Abundance')
#plt.legend(bbox_to_anchor=(1, 1))

plt.show()

plt.plot(
	data['H1K'], "Red", label='Kidney 1')
plt.plot(
	data['H2K'], "green", label='Kidney 2')
plt.plot(
	data['H3K'], "blue", label='Kidney 3')
plt.plot(
	data['H4K'], "black", label='Kidney 4')
plt.title('Kidney Methylation Variation')
plt.xlabel('Gene')
plt.ylabel('Methylation Abundance')
#plt.legend(bbox_to_anchor=(1, 1))

plt.show()