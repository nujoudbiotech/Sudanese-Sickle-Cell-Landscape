# Day 2: Darfur vs Khartoum HbS Frequency
# Author: Nujoud Basheer - Sudanese SCD Landscape

import matplotlib.pyplot as plt

# Data from literature - Sudanese tribes
regions = ['Darfur\n(Messeriya, Rizeigat)', 'Khartoum\n(Mixed)']
hbs_freq = [15, 3]  # HbS %
hba_freq = [85, 97] # HbA %

# Plot
fig, ax = plt.subplots(figsize=(8,5))
ax.bar(regions, hbs_freq, label='HbS (Sickle)', color='#d32f2f')
ax.bar(regions, hba_freq, bottom=hbs_freq, label='HbA (Normal)', color='#388e3c')

ax.set_ylabel('Frequency %')
ax.set_title('HbS vs HbA Frequency: Darfur vs Khartoum\nSudanese Landscape')
ax.legend()
ax.set_ylim(0,100)

# Add percentage labels
for i, v in enumerate(hbs_freq):
    ax.text(i, v/2, f"{v}%", ha='center', color='white', fontweight='bold')
    ax.text(i, v + hba_freq[i]/2, f"{hba_freq[i]}%", ha='center', color='white', fontweight='bold')

plt.tight_layout()
plt.savefig('darfur_vs_khartoum.png', dpi=300)
print("Plot saved! Darfur 15% HbS vs Khartoum 3% - High risk in Darfur tribes")
plt.show()
